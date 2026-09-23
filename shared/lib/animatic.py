"""Assemble an animatic (rough-cut explainer video) from a shot list.

Usage:  python3 shared/lib/animatic.py <experiment>/video/shots.json [--vertical]

shots.json:
{
  "title": "…",
  "shots": [
    {"type": "title", "text": "Big card text", "sub": "smaller line", "narration": "…", "seconds": 4},
    {"type": "image", "src": "output/foo.png", "narration": "…", "seconds": 6},
    {"type": "clip",  "src": "output/bar.mp4", "narration": "…", "seconds": 8}   # seconds optional
  ]
}

Writes <experiment>/video/build/{animatic.mp4, captions.srt} (or *_vertical.mp4 for 9:16).
Narration is written to the .srt so the cut can be voiced over or uploaded with captions.
ffmpeg is required; no drawtext/libass needed (cards are rendered with matplotlib).
"""
from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

FPS = 30


def ff(*args):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *args], check=True)


def probe_seconds(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def render_card(text: str, sub: str | None, path: Path, size) -> None:
    sv.apply_style()
    fig = plt.figure(figsize=size)
    wrap = 28 if size[0] < size[1] else 40
    fig.text(0.5, 0.55, "\n".join(textwrap.wrap(text, wrap)), ha="center", va="center",
             fontsize=34 if size[0] < size[1] else 40, weight="bold", color=sv.FG)
    if sub:
        fig.text(0.5, 0.30, "\n".join(textwrap.wrap(sub, wrap + 20)), ha="center", va="center",
                 fontsize=20, color=sv.C["yellow"])
    fig.text(0.5, 0.06, "a thought experiment · no conclusions, just observations", ha="center",
             fontsize=13, color=sv.MUTED)
    fig.savefig(path, dpi=100)
    plt.close(fig)


def vf(vertical: bool) -> str:
    if vertical:
        return (f"scale=720:-2:force_original_aspect_ratio=decrease,"
                f"pad=720:1280:(ow-iw)/2:(oh-ih)/2:color=0x0d1117,fps={FPS},format=yuv420p")
    return (f"scale=1280:720:force_original_aspect_ratio=decrease,"
            f"pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=0x0d1117,fps={FPS},format=yuv420p")


def srt_time(t: float) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def build(shots_file: Path, vertical: bool = False) -> Path:
    exp = shots_file.resolve().parent.parent
    spec = json.loads(shots_file.read_text())
    build_dir = shots_file.parent / "build"
    seg_dir = build_dir / ("segments_v" if vertical else "segments")
    seg_dir.mkdir(parents=True, exist_ok=True)
    size = sv.TALL if vertical else sv.WIDE
    segs, srt, t = [], [], 0.0

    for i, shot in enumerate(spec["shots"]):
        seg = seg_dir / f"{i:03d}.mp4"
        kind = shot["type"]
        if kind == "title":
            card = seg_dir / f"{i:03d}.png"
            render_card(shot["text"], shot.get("sub"), card, size)
            dur = shot.get("seconds", 4)
            ff("-loop", "1", "-t", str(dur), "-i", str(card), "-vf", vf(vertical), "-c:v", "libx264", str(seg))
        elif kind == "image":
            dur = shot.get("seconds", 6)
            ff("-loop", "1", "-t", str(dur), "-i", str(exp / shot["src"]), "-vf", vf(vertical),
               "-c:v", "libx264", str(seg))
        elif kind == "clip":
            src = exp / shot["src"]
            natural = probe_seconds(src)
            dur = shot.get("seconds", natural)
            pad = max(0.0, dur - natural)
            filt = vf(vertical) + (f",tpad=stop_mode=clone:stop_duration={pad:.2f}" if pad > 0 else "")
            ff("-i", str(src), "-t", f"{dur:.2f}", "-vf", filt, "-an", "-c:v", "libx264", str(seg))
        else:
            raise ValueError(f"unknown shot type {kind}")
        dur = probe_seconds(seg)
        if shot.get("narration"):
            srt.append(f"{len(srt)+1}\n{srt_time(t)} --> {srt_time(t + dur)}\n{shot['narration']}\n")
        segs.append(seg)
        t += dur

    listing = seg_dir / "concat.txt"
    listing.write_text("".join(f"file '{s.name}'\n" for s in segs))
    name = "animatic_vertical" if vertical else "animatic"
    out = build_dir / f"{name}.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(out))
    (build_dir / f"{name}.srt").write_text("\n".join(srt))
    print(f"  wrote {out}  ({t:.0f} s, {len(segs)} shots) + {name}.srt")
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build(Path(args[0]), vertical="--vertical" in sys.argv)
