"""Shared visual style + output helpers for every experiment.

Every figure in the project goes through here so that social posts, thumbnails
and video clips look like one series. Dark background, high contrast, 16:9 or
9:16 framing.
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import animation  # noqa: E402

BG = "#0d1117"
FG = "#e6edf3"
MUTED = "#8b949e"
GRID = "#30363d"

# Categorical palette (colour-blind friendly ordering).
C = {
    "blue": "#58a6ff",
    "orange": "#f0883e",
    "green": "#3fb950",
    "pink": "#db61a2",
    "yellow": "#d29922",
    "red": "#f85149",
    "purple": "#a371f7",
}

WIDE = (12.8, 7.2)  # 16:9 at 100 dpi -> 1280x720
TALL = (7.2, 12.8)  # 9:16 for Shorts / Reels / TikTok
SQUARE = (8, 8)


def apply_style() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": BG,
            "axes.facecolor": BG,
            "savefig.facecolor": BG,
            "axes.edgecolor": GRID,
            "axes.labelcolor": FG,
            "axes.titlecolor": FG,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "text.color": FG,
            "grid.color": GRID,
            "axes.grid": True,
            "grid.alpha": 0.6,
            "font.size": 13,
            "axes.titlesize": 17,
            "axes.titleweight": "bold",
            "legend.frameon": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def out_dir(experiment_file: str) -> Path:
    """Return <experiment>/output for a sim living in <experiment>/sims/."""
    d = Path(experiment_file).resolve().parent.parent / "output"
    d.mkdir(parents=True, exist_ok=True)
    return d


def save(fig, path: Path, *, watermark: str | None = "we-are-in-a-simulation · thought experiment") -> Path:
    if watermark:
        fig.text(0.99, 0.01, watermark, ha="right", va="bottom", fontsize=9, color=MUTED, alpha=0.8)
    fig.savefig(path, dpi=100, bbox_inches=None)
    plt.close(fig)
    print(f"  wrote {path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path}")
    return path


def save_anim(anim: animation.FuncAnimation, path: Path, fps: int = 30) -> Path | None:
    """Write mp4 via ffmpeg. Skipped (returns None) if NO_VIDEO=1 or ffmpeg missing."""
    if os.environ.get("NO_VIDEO") == "1" or not animation.writers.is_available("ffmpeg"):
        print(f"  skipped video {path.name} (NO_VIDEO=1 or ffmpeg unavailable)")
        plt.close(anim._fig)
        return None
    writer = animation.FFMpegWriter(fps=fps, bitrate=4000, extra_args=["-pix_fmt", "yuv420p"])
    anim.save(str(path), writer=writer, dpi=100)
    plt.close(anim._fig)
    print(f"  wrote {path.name}")
    return path
