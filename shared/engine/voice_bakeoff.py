"""Voice bake-off: render the same narration lines with several voices so you can pick a narrator.

    python3 shared/engine/voice_bakeoff.py                 # all providers with keys available
    python3 shared/engine/voice_bakeoff.py --list-eleven   # show your ElevenLabs voice library ids

Writes build/bakeoff/<provider>_<voice>.mp3 (all lines back to back) plus index.md.
Edit CANDIDATES to add or remove voices. Lines are taken from Episode 001, so you hear real material.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tts  # noqa: E402

LINES = [
    "You're sprinting for cover. You make it. You're safe. And then… you drop.",
    "Neither screen is reality. Reality lives on the server, the computer running the match.",
    "In that game, you were never behind cover. Nothing looks wrong. There is nothing to be angry about.",
    "Games slow time where there's too much going on. So does the universe. Coincidence, or the same engineering?",
]
NARRATOR = ("Documentary narrator for a curious, smart general audience. Warm, grounded, a little wry. "
            "Build intrigue with pacing; land reveals with a short pause before the key phrase. Never hype.")

CANDIDATES = [
    {"provider": "say", "voice": "Daniel", "rate": 168},
    # OpenAI: gpt-4o-mini-tts is steerable with `instructions`. The newest voices (cedar, marin) are the
    # closest to ChatGPT's own voice; the app's Advanced Voice isn't exposed 1:1 via the API.
    *[{"provider": "openai", "model": "gpt-4o-mini-tts", "voice": v, "instructions": NARRATOR}
      for v in ("cedar", "marin", "ash", "onyx", "sage", "verse")],
    # ElevenLabs: fill in voice ids from `--list-eleven` (voices in your library / Voice Library).
    # {"provider": "elevenlabs", "model": "eleven_multilingual_v2", "voice": "<voice_id>", "label": "name"},
]

OUT = Path(__file__).resolve().parents[2] / "build" / "bakeoff"


def main():
    if "--list-eleven" in sys.argv:
        for vid, name, desc in tts.list_elevenlabs_voices():
            print(f"{vid}  {name:<24s} {desc}")
        return
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for c in CANDIDATES:
        label = f"{c['provider']}_{c.get('label', c['voice'])}"
        try:
            wavs = [tts.synth(line, c, OUT / "cache") for line in LINES]
        except RuntimeError as e:
            print(f"  skip {label}: {e}")
            continue
        listing = OUT / f"{label}.txt"
        listing.write_text("".join(f"file '{w.resolve()}'\n" for w in wavs))
        mp3 = OUT / f"{label}.mp3"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
                        "-af", "apad=pad_dur=0.6", "-c:a", "libmp3lame", "-q:a", "3", str(mp3)], check=True)
        rows.append(f"| {label} | [{mp3.name}]({mp3.name}) |")
        print(f"  wrote {mp3}")
    (OUT / "index.md").write_text("| voice | sample |\n|---|---|\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
