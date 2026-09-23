"""Animated "every tile is a clock" floor textures for Episode 002.

Each tile blinks once per local tick. Colour encodes tick rate (cyan = full speed, violet/red = slow).
The rate field is the lag field from sims/lag_field.py (1/r outside a lump), exaggerated
so the difference is visible, with the real number stated in narration.

Sequences (build/tex/<name>/NNNN.png) + schedule.json:
  ripple   planet arrives at the centre; the slowdown spreads outward and settles into 1/r
  steady   settled field, tiles keep blinking at their own rates (backdrop for the marchers)
  sync     "the tick is a signal": a sync wave sweeps each region; near the planet the tiles
           subdivide (more space) and the wave takes longer to cross (slower tick)
"""
from __future__ import annotations

import colorsys
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUT = Path(__file__).resolve().parent / "build" / "tex"
PX, N = 1024, 48                 # texture px, tiles per side (plane is 48 m → 1 m tiles)
TILE = PX / N
F0 = 1.2                         # full-speed blinks per second (video time)
FPS = 30
DEPTH, SOFT = 0.55, 2.2          # exaggerated max slowdown, softening radius (tiles)


def field(cx=N / 2, cy=N / 2):
    y, x = np.mgrid[0:N, 0:N] + 0.5
    d = np.hypot(x - cx, y - cy)
    return 1 - DEPTH * SOFT / np.sqrt(d**2 + SOFT**2), d


def rate_colour(r, flash):
    """r in [1-DEPTH, 1] → hue from violet (slow) to cyan (fast); flash in [0,1] brightens."""
    u = np.clip((r - (1 - DEPTH)) / DEPTH, 0, 1) ** 4      # stretch contrast in the mid-field
    h = 0.78 - 0.26 * u          # 0.78 violet → 0.52 cyan
    v = 0.38 + 0.62 * flash
    rgb = colorsys.hsv_to_rgb(h, 0.9 - 0.35 * flash, v)
    return tuple(int(255 * c) for c in rgb)


def render(rate, phase, subdiv=None, wave=None):
    img = Image.new("RGB", (PX, PX), (3, 4, 10))
    d = ImageDraw.Draw(img)
    flash = np.clip(1 - (phase % 1.0) / 0.22, 0, 1) ** 2
    for j in range(N):
        for i in range(N):
            x0, y0 = i * TILE, j * TILE
            c = rate_colour(rate[j, i], flash[j, i])
            k = subdiv[j, i] if subdiv is not None else 1
            s = TILE / k
            for a in range(k):
                for b in range(k):
                    d.rectangle([x0 + a * s + 1.5, y0 + b * s + 1.5, x0 + (a + 1) * s - 1.5, y0 + (b + 1) * s - 1.5], fill=c)
    if wave is not None:
        d2 = ImageDraw.Draw(img, "RGBA")
        for (cx, cy, rad) in wave:
            d2.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=(255, 255, 255, 170), width=5)
    glow = img.filter(ImageFilter.GaussianBlur(5))
    return Image.blend(img, glow, 0.3).point(lambda v: min(255, int(v * 1.35)))


def seq_ripple(frames=240):
    final, dist = field()
    rate = np.ones((N, N))
    phase = np.zeros((N, N))
    out = OUT / "ripple"
    out.mkdir(parents=True, exist_ok=True)
    for f in range(1, frames + 1):
        t = f / FPS
        front = max(0.0, (t - 1.0) * 9.0)                  # planet lands at t=1s; slowdown spreads ~9 tiles/s
        reach = np.clip((front - dist) / 3.0, 0, 1)
        rate = 1 + (final - 1) * reach
        phase += rate * F0 / FPS
        render(rate, phase).save(out / f"{f:04d}.png")
    return frames


def seq_steady(frames=300):
    rate, _ = field()
    phase = np.random.default_rng(0).random((N, N)) * 0.0
    out = OUT / "steady"
    out.mkdir(parents=True, exist_ok=True)
    for f in range(1, frames + 1):
        phase += rate * F0 / FPS
        render(rate, phase).save(out / f"{f:04d}.png")
    return frames, rate.tolist()


def seq_sync(frames=300):
    rate, dist = field()
    out = OUT / "sync"
    out.mkdir(parents=True, exist_ok=True)
    phase = np.zeros((N, N))
    for f in range(1, frames + 1):
        t = f / FPS
        grow = np.clip((t - 1.0) / 3.0, 0, 1)            # tiles subdivide over 3 s: more space near the planet
        k = np.where(dist < 4, 4, np.where(dist < 9, 2, 1))
        subdiv = np.where(grow > 0.5, k, np.where(grow > 0.2, np.minimum(k, 2), 1))
        phase += rate * F0 / FPS
        # sync waves: one expanding ring per region pulse, centred on the planet; slower where cells are finer
        waves = []
        period = 1.6
        for n in range(4):
            age = (t - n * period / 4) % period
            rad_tiles = 22 * (age / period) ** 1.6       # the wave slows as it crosses the finer, denser middle
            waves.append((PX / 2, PX / 2, rad_tiles * TILE))
        render(rate, phase, subdiv=subdiv, wave=waves if t > 4.2 else None).save(out / f"{f:04d}.png")
    return frames


if __name__ == "__main__":
    sched = {"ripple": {"frames": seq_ripple()}, "steady": {"frames": seq_steady()[0]}, "sync": {"frames": seq_sync()}}
    rate, _ = field()
    sched["field"] = {"N": N, "depth": DEPTH, "soft": SOFT}
    (OUT / "schedule.json").write_text(json.dumps(sched))
    print("textures:", {k: v.get("frames") for k, v in sched.items() if "frames" in v})
