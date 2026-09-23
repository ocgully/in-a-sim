"""Generate the animated detector-screen textures for the double-slit lab shots.

Runs with normal python3 (PIL + numpy) before Blender. Writes PNG sequences plus a
schedule.json that the Blender scene reads so flying particles and screen dots line up.

Physics: same model as sims/delayed_choice_eraser.py (far-field two-slit pattern,
Gaussian envelope). 'stripes' = no which-path record, 'observed' = which-path record,
'delayed' = eraser log sorted by the partner photon's later result.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1024, 320                       # screen texture (8 m x 2.5 m plane)
Y_SPAN = 8.0                           # metres across the screen
OUT = Path(__file__).resolve().parent / "build" / "tex"
LAUNCH_EVERY, FLIGHT, N_SLOW = 8, 24, 24   # frames between particles, gun->screen frames, individually shown
FAST_FRAMES, N_TOTAL, HOLD = 110, 2600, 60

rng = np.random.default_rng(1801)      # Young's double-slit year


def env(y):
    return np.exp(-(y / 1.6) ** 2)


def sample(mode, n):
    ys = np.linspace(-4, 4, 4001)
    if mode == "stripes":
        p = env(ys) ** 2 * np.cos(2.6 * ys) ** 2
    elif mode == "observed":
        p = np.exp(-((ys - 1.0) / 0.55) ** 2) + np.exp(-((ys + 1.0) / 0.55) ** 2)
        p *= env(ys * 0.7)
    else:
        p = env(ys) ** 2
    p /= p.sum()
    y = rng.choice(ys, n, p=p) + rng.normal(0, 0.01, n)
    z = rng.uniform(0.35, 2.15, n)
    return y, z


def to_px(y, z):
    return (y + Y_SPAN / 2) / Y_SPAN * W, H - (z / 2.5) * H


def draw(dots, colours, flash=None):
    img = Image.new("RGB", (W, H), (4, 6, 12))
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    d, g = ImageDraw.Draw(img), ImageDraw.Draw(glow)
    for (px, pz), c in zip(dots, colours):
        d.ellipse([px - 2, pz - 2, px + 2, pz + 2], fill=c)
        g.ellipse([px - 4, pz - 4, px + 4, pz + 4], fill=c)
    if flash:
        for px, pz in flash:
            g.ellipse([px - 12, pz - 12, px + 12, pz + 12], fill=(255, 255, 255))
            d.ellipse([px - 5, pz - 5, px + 5, pz + 5], fill=(255, 255, 255))
    glow = glow.filter(ImageFilter.GaussianBlur(4))
    return Image.blend(img, glow, 0.35).point(lambda v: min(255, int(v * 1.8)))


def build_accumulate(mode, colour):
    d = OUT / mode
    d.mkdir(parents=True, exist_ok=True)
    y, z = sample(mode, N_TOTAL)
    slit = np.sign(y) if mode == "observed" else np.zeros_like(y)
    px = [to_px(a, b) for a, b in zip(y, z)]
    arrive = [k * LAUNCH_EVERY + FLIGHT for k in range(N_SLOW)]
    f_fast0 = arrive[-1] + 10
    n_frames = f_fast0 + FAST_FRAMES + HOLD
    for f in range(1, n_frames + 1):
        if f < f_fast0:
            n = sum(a <= f for a in arrive)
            flash = [px[k] for k in range(N_SLOW) if 0 <= f - arrive[k] < 4]
        else:
            frac = min(1.0, (f - f_fast0) / FAST_FRAMES)
            n = int(N_SLOW + (N_TOTAL - N_SLOW) * frac ** 1.5)
            flash = None
        draw(px[:n], [colour] * n, flash).save(d / f"{f:04d}.png")
    return {"frames": n_frames, "launch_every": LAUNCH_EVERY, "flight": FLIGHT, "n_slow": N_SLOW,
            "slit": [int(s) for s in slit[:N_SLOW]], "y": [float(v) for v in y[:N_SLOW]],
            "z": [float(v) for v in z[:N_SLOW]]}


def build_delayed():
    """Hits already on the screen; later partner results colour them; sorting reveals stripes."""
    d = OUT / "delayed"
    d.mkdir(parents=True, exist_ok=True)
    n = 3000
    y, z = sample("none", n)
    k = 2.6
    p_d1 = np.cos(k * y) ** 2                       # P(D1 | y) when the path info is erased
    d1 = rng.random(n) < p_d1
    px = [to_px(a, b) for a, b in zip(y, z)]
    white, blue, orange = (225, 235, 255), (70, 170, 255), (255, 130, 40)
    fin = [blue if a else orange for a in d1]
    keep = rng.random(n)                            # per-dot fade threshold (no flicker)
    P1, P2, P3, P4 = 50, 100, 70, 90                # show, recolour, hide orange, hold stripes
    frames = P1 + P2 + P3 + P4
    for f in range(1, frames + 1):
        if f <= P1:
            cols = [white] * n
            shown = list(range(n))
        elif f <= P1 + P2:
            m = int(n * (f - P1) / P2)
            cols = fin[:m] + [white] * (n - m)
            shown = list(range(n))
        else:
            fade = min(1.0, (f - P1 - P2) / P3)
            cols, shown = [], []
            for i in range(n):
                if d1[i]:
                    cols.append(blue)
                    shown.append(i)
                elif keep[i] > fade:
                    cols.append(orange)
                    shown.append(i)
        draw([px[i] for i in shown], cols).save(d / f"{f:04d}.png")
    return {"frames": frames, "phases": [P1, P2, P3, P4]}


if __name__ == "__main__":
    sched = {"stripes": build_accumulate("stripes", (80, 190, 255)),
             "observed": build_accumulate("observed", (255, 150, 60)),
             "delayed": build_delayed()}
    (OUT / "schedule.json").write_text(json.dumps(sched))
    print("textures:", {k: v["frames"] for k, v in sched.items()})
    sys.exit(0)
