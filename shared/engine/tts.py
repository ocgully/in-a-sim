"""Pluggable narration voices for compose.py, with an on-disk cache.

Providers
  say         macOS built-in (free, draft quality)
  openai      OpenAI speech API (model e.g. gpt-4o-mini-tts; supports style "instructions")
  elevenlabs  ElevenLabs text-to-speech (model e.g. eleven_multilingual_v2 / eleven_v3)

Keys come from the environment or a repo-root `.env` file (gitignored):
  OPENAI_API_KEY=...
  ELEVENLABS_API_KEY=...

Episode config (episode.json):
  "tts": {"provider": "openai", "model": "gpt-4o-mini-tts", "voice": "cedar",
          "instructions": "Warm, curious documentary narrator…", "speed": 1.0}
  "tts": {"provider": "elevenlabs", "model": "eleven_multilingual_v2", "voice": "<voice_id>",
          "stability": 0.45, "similarity": 0.8, "style": 0.3}

Audio is cached under <episode>/build/vo_cache/<hash>.wav, keyed on provider + voice + model +
settings + text, so re-composing never re-bills unchanged lines.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def _env(name):
    if os.environ.get(name):
        return os.environ[name]
    env = REPO / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def _post(url, headers, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.read()
    except urllib.error.HTTPError as e:  # surface the provider's error message
        raise RuntimeError(f"{url} → HTTP {e.code}: {e.read().decode(errors='replace')[:500]}") from None


def _to_wav(src: Path, dst: Path):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-ar", "48000", "-ac", "1", str(dst)], check=True)


def _duration(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout)


def synth(text: str, cfg: dict, cache_dir: Path) -> Path:
    """Return a 48 kHz mono wav of `text` spoken with `cfg`. Cached."""
    cfg = dict(cfg or {"provider": "say", "voice": "Daniel"})
    key = hashlib.sha256(json.dumps([cfg, text], sort_keys=True).encode()).hexdigest()[:20]
    cache_dir.mkdir(parents=True, exist_ok=True)
    wav = cache_dir / f"{key}.wav"
    if wav.exists():
        return wav
    raw = cache_dir / f"{key}.raw"
    p = cfg.get("provider", "say")
    if p == "say":
        aiff = raw.with_suffix(".aiff")
        subprocess.run(["say", "-v", cfg.get("voice", "Daniel"), "-r", str(cfg.get("rate", 170)), "-o", str(aiff),
                        text.replace("…", "...").replace("—", ", ")], check=True)
        _to_wav(aiff, wav)
        aiff.unlink()
        return wav
    if p == "openai":
        k = _env("OPENAI_API_KEY")
        if not k:
            raise RuntimeError("OPENAI_API_KEY not set (env or repo .env)")
        body = {"model": cfg.get("model", "gpt-4o-mini-tts"), "voice": cfg.get("voice", "cedar"),
                "input": text, "response_format": "wav"}
        if cfg.get("instructions"):
            body["instructions"] = cfg["instructions"]
        if cfg.get("speed"):
            body["speed"] = cfg["speed"]
        audio = _post("https://api.openai.com/v1/audio/speech",
                      {"Authorization": f"Bearer {k}", "Content-Type": "application/json"}, body)
    elif p == "elevenlabs":
        k = _env("ELEVENLABS_API_KEY")
        if not k:
            raise RuntimeError("ELEVENLABS_API_KEY not set (env or repo .env)")
        body = {"text": text, "model_id": cfg.get("model", "eleven_multilingual_v2"),
                "voice_settings": {"stability": cfg.get("stability", 0.45),
                                   "similarity_boost": cfg.get("similarity", 0.8),
                                   "style": cfg.get("style", 0.3), "use_speaker_boost": True}}
        audio = _post(f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['voice']}?output_format=mp3_44100_128",
                      {"xi-api-key": k, "Content-Type": "application/json", "Accept": "audio/mpeg"}, body)
    else:
        raise ValueError(f"unknown tts provider {p}")
    raw.write_bytes(audio)
    _to_wav(raw, wav)
    raw.unlink()
    return wav


def synth_with_duration(text, cfg, cache_dir):
    w = synth(text, cfg, cache_dir)
    return w, _duration(w)


def list_elevenlabs_voices():
    k = _env("ELEVENLABS_API_KEY")
    req = urllib.request.Request("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": k})
    with urllib.request.urlopen(req, timeout=60) as r:
        return [(v["voice_id"], v["name"], (v.get("labels") or {}).get("description", ""))
                for v in json.loads(r.read())["voices"]]
