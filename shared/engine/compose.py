"""Episode compositor: rendered frames + a story script → narrated, captioned video.

    python3 shared/engine/compose.py <episode.json> [--vertical] [--no-vo] [--only seg_id,...]

episode.json
{
  "title": "...", "voice": "Daniel", "rate": 172,
  "frames_dir": "build/frames",            # relative to episode.json; one subdir per rendered shot
  "segments": [
    {"id": "hook",
     "vo": "Narration for this beat.",       # spoken (macOS `say`) and burned in as captions
     "ops": [                                # what to show, in order
        {"src": "arena_game", "play": [1, "f_notify"], "speed": 1},
        {"src": "arena_game", "rewind": ["end", "f_seen"], "speed": 2},
        {"src": "arena_game", "hold": "f_seen", "n": 30},
        {"card": {"title": "...", "sub": "..."}, "n": 90}
     ],
     "overlays": [ {"type": "banner", "text": "HIT", "op": 2, "from": 0, "to": 30}, ... ]
    }
  ]
}
Frame refs may be integers or names from build/frames/<src>/meta.json ("f_notify", "end", "f_seen+10").
If the narration runs longer than the ops, the last frame is held until it finishes.

Overlay types: tag, label, banner, crosshair, vignette, tint, ring, line, counter, timer.
Every overlay may carry "op" (index of the op it belongs to) and "from"/"to" (frames within that op).
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import textwrap
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tts as voice  # noqa: E402

FPS = 30
W, H = 1280, 720
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
COL = {"cyan": (80, 200, 255), "orange": (255, 140, 40), "pink": (255, 80, 170), "green": (80, 255, 130),
       "red": (255, 50, 40), "yellow": (255, 210, 60), "white": (235, 240, 255), "purple": (170, 110, 255)}


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def col(c):
    return COL.get(c, (255, 255, 255)) if isinstance(c, str) else tuple(c)


# ------------------------------------------------------------------ frame refs
class Source:
    def __init__(self, d: Path):
        self.dir = d
        self.meta = json.loads((d / "meta.json").read_text()) if (d / "meta.json").exists() else {}
        self.n = len(list(d.glob("f_*.png")))
        self._cache = {}

    def ref(self, r):
        if isinstance(r, int):
            return r
        m = re.fullmatch(r"(\w+)\s*([+-]\s*\d+)?", str(r))
        name, off = m.group(1), int(m.group(2).replace(" ", "")) if m.group(2) else 0
        base = self.n if name == "end" else int(self.meta[name])
        return max(1, min(self.n, base + off))

    def frame(self, i):
        if i not in self._cache:
            if len(self._cache) > 400:
                self._cache.clear()
            self._cache[i] = Image.open(self.dir / f"f_{i:04d}.png").convert("RGB")
        return self._cache[i]


# ------------------------------------------------------------------ cards
def card(title, sub=None, accent="cyan"):
    img = Image.new("RGB", (W, H), (5, 7, 14))
    d = ImageDraw.Draw(img)
    # perspective grid floor
    a = col(accent)
    for i in range(-20, 21):
        d.line([(W / 2 + i * 12, H * 0.62), (W / 2 + i * 140, H)], fill=tuple(v // 5 for v in a), width=2)
    y = H * 0.62
    k = 0
    while y < H:
        d.line([(0, y), (W, y)], fill=tuple(v // 5 for v in a), width=2)
        k += 1
        y += 6 * k
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    g = ImageDraw.Draw(glow)
    lines = textwrap.wrap(title, 24)
    f = font(62)
    yy = H * 0.38 - 40 * len(lines)
    for ln in lines:
        w = d.textlength(ln, font=f)
        g.text(((W - w) / 2, yy), ln, font=f, fill=a)
        d.text(((W - w) / 2, yy), ln, font=f, fill=(245, 248, 255))
        yy += 80
    if sub:
        fs = font(26, bold=False)
        for ln in textwrap.wrap(sub, 60):
            w = d.textlength(ln, font=fs)
            d.text(((W - w) / 2, yy + 20), ln, font=fs, fill=col("yellow"))
            yy += 38
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    return Image.fromarray(np.clip(np.asarray(img, np.int16) + np.asarray(glow, np.int16), 0, 255).astype(np.uint8))


# ------------------------------------------------------------------ overlays
def pill(d, xy, text, f, fg, bg=(0, 0, 0), pad=10, alpha_img=None):
    x, y = xy
    w = d.textlength(text, font=f)
    hgt = f.size + pad
    d.rounded_rectangle([x - pad, y - pad / 2, x + w + pad, y + hgt], radius=8, fill=bg)
    d.text((x, y), text, font=f, fill=fg)


def world_px(meta, xy):
    s = W / meta["ortho"]
    return (W / 2 + (xy[0] - meta["cx"]) * s, H / 2 - (xy[1] - meta["cy"]) * s)


def apply_overlays(img, ovs, k, src, src_frame, n_op):
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    base = img
    for ov in ovs:
        a, b = ov.get("from", 0), ov.get("to", 10**9)
        if a < 0:
            a = n_op + a
        if b < 0:
            b = n_op + b
        if not (a <= k < b):
            continue
        t = ov["type"]
        c = col(ov.get("color", "white"))
        if t == "tint":
            arr = np.asarray(base, np.float32)
            tint = np.array(col(ov.get("color", "cyan")), np.float32)
            arr = arr * 0.55 + tint * 0.25
            arr[::3] *= 0.75                       # scanlines
            base = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        elif t == "vignette":
            strength = ov.get("strength", 0.6)
            yy, xx = np.mgrid[0:H, 0:W]
            r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
            m = np.clip((r - 0.45) / 0.9, 0, 1)[..., None] * strength
            arr = np.asarray(base, np.float32)
            arr = arr * (1 - m) + np.array(c, np.float32) * m
            base = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        elif t == "tag":
            f = font(22)
            d.rectangle([24, 24, 32, 60], fill=c)
            pill(d, (44, 28), ov["text"], f, (255, 255, 255), bg=(0, 0, 0, 170))
        elif t == "label":
            f = font(ov.get("size", 28))
            x, y = ov.get("pos", [W / 2, 90])
            if ov.get("right"):
                x -= d.textlength(ov["text"], font=f)
            elif ov.get("center", True):
                x -= d.textlength(ov["text"], font=f) / 2
            pill(d, (x, y), ov["text"], f, c, bg=(0, 0, 0, 170))
        elif t == "banner":
            f = font(ov.get("size", 78))
            txt = ov["text"]
            w = d.textlength(txt, font=f)
            pop = min(1.0, (k - a + 1) / 4)
            y = ov.get("y", H * 0.36)
            glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(glow).text(((W - w) / 2, y), txt, font=f, fill=(*c, int(255 * pop)))
            over.alpha_composite(glow.filter(ImageFilter.GaussianBlur(10)))
            over.alpha_composite(glow)
            d = ImageDraw.Draw(over)
            d.text(((W - w) / 2, y), txt, font=f, fill=(255, 255, 255, int(230 * pop)))
        elif t == "crosshair":
            x, y = ov.get("pos", [W / 2, H / 2])
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                d.line([(x + 8 * dx, y + 8 * dy), (x + 26 * dx, y + 26 * dy)], fill=(*c, 255), width=3)
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(*c, 255))
        elif t in ("ring", "line"):
            if t == "ring":
                x, y = world_px(src.meta, ov["xy"]) if "xy" in ov else ov["px"]
                r = ov.get("r", 26) + 4 * math.sin(k / 3)
                d.ellipse([x - r, y - r, x + r, y + r], outline=(*c, 255), width=5)
            else:
                p1 = world_px(src.meta, ov["xy1"])
                p2 = world_px(src.meta, ov["xy2"])
                d.line([p1, p2], fill=(*c, 230), width=4)
        elif t == "counter":
            step = ov.get("step", 24)
            n = min(ov.get("max", 512), 2 ** max(0, (src_frame - 1) // step))
            f = font(ov.get("size", 44))
            txt = ov["text"].format(n=n)
            x, y = ov["pos"]
            pill(d, (x, y), txt, f, c, bg=(0, 0, 0, 170))
        elif t == "timer":
            m = src.meta
            ms = (m["t0"] + (src_frame - 1) / (m["slowmo"] * FPS)) * 1000
            f = font(26)
            pill(d, (W - 330, 30), ov.get("text", "server time {ms:5.0f} ms").format(ms=ms), f, c, bg=(0, 0, 0, 170))
    out = base.convert("RGBA")
    out.alpha_composite(over)
    return out.convert("RGB")


def draw_caption(img, text):
    if not text:
        return img
    d = ImageDraw.Draw(img, "RGBA")
    f = font(30, bold=False)
    lines = textwrap.wrap(text, 58)
    y = H - 40 - 42 * len(lines)
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.rounded_rectangle([(W - w) / 2 - 14, y - 6, (W + w) / 2 + 14, y + 38], radius=8, fill=(0, 0, 0, 185))
        d.text(((W - w) / 2, y), ln, font=f, fill=(255, 255, 255))
        y += 42
    return img


def caption_chunks(vo, n_frames):
    """Split narration into caption chunks timed by character count."""
    if not vo:
        return []
    parts = re.split(r"(?<=[.!?…])\s+", vo.strip())
    chunks = []
    for p in parts:
        chunks.extend(textwrap.wrap(p, 110) or [p])
    total = sum(len(c) for c in chunks)
    out, t = [], 0.0
    for c in chunks:
        dur = n_frames * len(c) / total
        out.append((int(t), int(t + dur), c))
        t += dur
    return out


# ------------------------------------------------------------------ audio
# ------------------------------------------------------------------ build
def op_frames(op, sources):
    """Yield (image, src, src_frame) for one op."""
    if "card" in op:
        im = card(op["card"]["title"], op["card"].get("sub"), op["card"].get("accent", "cyan"))
        for _ in range(op.get("n", 90)):
            yield im, None, 0
        return
    src = sources[op["src"]]
    spd = op.get("speed", 1)
    if "play" in op or "rewind" in op:
        a, b = (src.ref(x) for x in op.get("play", op.get("rewind")))
        step = 1 if b >= a else -1
        pos = float(a)
        while (pos <= b) if step > 0 else (pos >= b):
            i = int(round(pos))
            yield src.frame(i), src, i
            pos += step * spd
    elif "hold" in op:
        i = src.ref(op["hold"])
        for _ in range(op.get("n", 30)):
            yield src.frame(i), src, i


def build(ep_path: Path, vertical=False, with_vo=True, only=None, tts_override=None):
    ep = json.loads(ep_path.read_text())
    tts_cfg = tts_override or ep.get("tts") or {"provider": "say", "voice": ep.get("voice", "Daniel"), "rate": ep.get("rate", 172)}
    root = ep_path.parent
    fdir = root / ep.get("frames_dir", "build/frames")
    out_dir = root / "build" / "episode"
    seg_dir = out_dir / ("seg_v" if vertical else "seg")
    seg_dir.mkdir(parents=True, exist_ok=True)
    sources = {p.name: Source(p) for p in fdir.iterdir() if p.is_dir()}
    seg_files, total = [], 0.0
    for si, seg in enumerate(ep["segments"]):
        if only and seg["id"] not in only:
            continue
        vo = seg.get("vo")
        wav, vo_sec = (voice.synth_with_duration(vo, tts_cfg, root / "build" / "vo_cache")
                       if (vo and with_vo) else (None, 0.0))
        # collect frames
        frames = []
        for oi, op in enumerate(seg["ops"]):
            op_list = list(op_frames(op, sources))
            for k, (im, src, sf) in enumerate(op_list):
                frames.append((oi, k, len(op_list), im, src, sf))
        lead = int(seg.get("vo_at", 0.25) * FPS)
        need = int((vo_sec + seg.get("tail", 0.5)) * FPS) + lead
        while len(frames) < need:
            oi, k, n, im, src, sf = frames[-1]
            frames.append((oi, k + 1, n, im, src, sf))
        n_seg = len(frames)
        caps = caption_chunks(vo, max(1, int(vo_sec * FPS))) if vo else []
        mp4 = seg_dir / f"{si:02d}_{seg['id']}.mp4"
        vf = ("scale=720:-2,pad=720:1280:0:(oh-ih)/2:color=0x05070e" if vertical else "null")
        enc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-vf", vf,
                                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", str(mp4)], stdin=subprocess.PIPE)
        for j, (oi, k, n, im, src, sf) in enumerate(frames):
            ovs = [o for o in seg.get("overlays", []) if o.get("op", 0) == oi]
            img = apply_overlays(im, ovs, k, src, sf, n)
            cap = next((c for a, b, c in caps if a <= j - lead < b), None)
            if cap and seg.get("captions", True):
                img = draw_caption(img, cap)
            enc.stdin.write(img.tobytes())
        enc.stdin.close()
        enc.wait()
        dur = n_seg / FPS
        # audio for this segment, padded to the segment length
        seg_wav = seg_dir / f"{si:02d}_{seg['id']}_pad.wav"
        if vo_sec > 0:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-af",
                            f"adelay={int(lead / FPS * 1000)},apad", "-t", f"{dur:.3f}", "-ar", "48000", "-ac", "1",
                            str(seg_wav)], check=True)
        else:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
                            "-t", f"{dur:.3f}", str(seg_wav)], check=True)
        seg_files.append((mp4, seg_wav))
        total += dur
        print(f"  [{seg['id']:<14s}] {dur:5.1f}s  (vo {vo_sec:4.1f}s)")

    vlist = out_dir / "v.txt"
    alist = out_dir / "a.txt"
    vlist.write_text("".join(f"file '{m.resolve()}'\n" for m, _ in seg_files))
    alist.write_text("".join(f"file '{a.resolve()}'\n" for _, a in seg_files))
    name = ep_path.stem + ("_vertical" if vertical else "") + (f"_{'-'.join(only)}" if only else "") \
        + (f"_{tts_cfg['provider']}-{tts_cfg.get('voice')}" if tts_cfg.get("provider") != "say" else "")
    final = out_dir / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(vlist),
                    "-f", "concat", "-safe", "0", "-i", str(alist), "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", str(final)], check=True)
    print(f"  wrote {final}  ({total:.0f} s)")
    return final


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only = None
    for a in sys.argv:
        if a.startswith("--only="):
            only = a.split("=", 1)[1].split(",")
    override = None
    for a in sys.argv:
        if a.startswith("--tts="):                       # e.g. --tts=openai:cedar  or  --tts=elevenlabs:<voice_id>
            prov, v = a.split("=", 1)[1].split(":", 1)
            override = {"provider": prov, "voice": v}
    build(Path(args[0]), vertical="--vertical" in sys.argv, with_vo="--no-vo" not in sys.argv, only=only,
          tts_override=override)
