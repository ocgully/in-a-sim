"""Sim 2 — Delayed-choice quantum eraser, run as an event log.

Idealised Kim et al. (1999)-style setup. Each entangled pair produces:
  * a SIGNAL photon that hits a screen at position x  (recorded FIRST)
  * an IDLER photon that is measured LATER, and a random beam-splitter "choice"
    decides whether its detector reveals which slit (D3/D4) or erases that
    information (D1/D2).

Joint state (far-field, equal slits):  |Ψ> = (ψ1(x)|a> + ψ2(x)|b>)/√2

This sim deliberately generates events in TIME ORDER: sample x from the signal
marginal first, write it to the log, and only afterwards sample the idler
outcome conditional on the already-written x. No rewind. No editing of the
screen log. Yet sorting the log by the later idler result reveals fringes.

What this demonstrates (and what it does not):
  * The raw screen pattern is identical whatever is chosen later (no signalling).
  * The "retroactive" fringes only exist in the JOIN of two logs (coincidence
    counting) — like a server-side annotation no client ever sees on its own.
  * A sequential sampler with access to the joint record reproduces the stats
    with no rollback at all. That is a point AGAINST a literal rewind, and a
    point FOR "some global joint record exists" — see findings.md.

Outputs:
  output/eraser_sorted.png    raw screen vs. screen sorted by later idler result
  output/eraser_relabel.mp4   dots accumulate grey, then get retroactively coloured
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import animation  # noqa: E402

OUT = sv.out_dir(__file__)

X = np.linspace(-10, 10, 2001)          # screen coordinate (arbitrary units)
ENV = np.exp(-(X / 5.0) ** 2)           # single-slit envelope (amplitude)
K = 1.6                                  # fringe wavenumber ~ k d / D


def amplitudes(x):
    env = np.interp(x, X, ENV)
    psi1 = env * np.exp(+0.5j * K * x)
    psi2 = env * np.exp(-0.5j * K * x)
    return psi1, psi2


def run(n: int, seed: int = 1999):
    rng = np.random.default_rng(seed)
    # 1) SIGNAL photon lands first: marginal p(x) ∝ (|ψ1|²+|ψ2|²)/2 — no fringes.
    p = ENV ** 2
    p = p / p.sum()
    x = rng.choice(X, size=n, p=p) + rng.uniform(-0.005, 0.005, n)

    # 2) LATER: random beam-splitter choice for each idler.
    eraser = rng.random(n) < 0.5            # True -> D1/D2 (erase), False -> D3/D4 (which-path)

    # 3) Idler outcome sampled conditional on the ALREADY-WRITTEN x (Born rule).
    psi1, psi2 = amplitudes(x)
    norm = np.abs(psi1) ** 2 + np.abs(psi2) ** 2
    p_plus = np.abs(psi1 + psi2) ** 2 / (2 * norm)   # P(D1 | x, eraser)
    p_a = np.abs(psi1) ** 2 / norm                   # P(D3 | x, which-path)
    u = rng.random(n)
    det = np.where(eraser, np.where(u < p_plus, "D1", "D2"), np.where(u < p_a, "D3", "D4"))
    return x, eraser, det


def fringe_contrast(xs):
    """Strength of the cos(Kx) fringe component: ~1 = perfect fringes, ~0 = none."""
    return 2 * abs(np.mean(np.exp(1j * K * xs)))


def static_figure(x, eraser, det):
    bins = np.linspace(-8, 8, 121)
    fig, axes = plt.subplots(2, 3, figsize=sv.WIDE, sharex=True)
    panels = [
        ("Screen, ALL hits\n(what the signal side can ever see)", np.ones_like(x, bool), sv.FG),
        ("Screen, later chose ERASE", eraser, sv.MUTED),
        ("Screen, later chose WHICH-PATH", ~eraser, sv.MUTED),
        ("…sorted by later D1", det == "D1", sv.C["blue"]),
        ("…sorted by later D2", det == "D2", sv.C["orange"]),
        ("…sorted by later D3 / D4", (det == "D3") | (det == "D4"), sv.C["green"]),
    ]
    stats = {}
    for ax, (title, mask, col) in zip(axes.flat, panels):
        ax.hist(x[mask], bins=bins, color=col, alpha=0.9)
        ax.set_title(title, fontsize=12)
        ax.set_yticks([])
        stats[title.split("\n")[0]] = fringe_contrast(x[mask])
    fig.suptitle("Delayed-choice eraser: the screen log never changes — the pattern lives in the JOIN",
                 fontsize=16, weight="bold")
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    sv.save(fig, OUT / "eraser_sorted.png")
    return stats


def no_signalling_check(x, eraser):
    """Is the screen distribution different depending on the LATER choice? (Should not be.)"""
    bins = np.linspace(-8, 8, 41)
    h1, _ = np.histogram(x[eraser], bins)
    h2, _ = np.histogram(x[~eraser], bins)
    # two-sample chi-square
    k1, k2 = np.sqrt(h2.sum() / h1.sum()), np.sqrt(h1.sum() / h2.sum())
    m = (h1 + h2) > 0
    chi2 = np.sum((k1 * h1[m] - k2 * h2[m]) ** 2 / (h1[m] + h2[m]))
    return chi2, m.sum() - 1


def relabel_animation(x, det, fps=30):
    n_show = 3000
    x, det = x[:n_show], det[:n_show]
    rng = np.random.default_rng(3)
    y = rng.uniform(0, 1, n_show)
    phase1, phase2, hold = 150, 150, 60           # frames: accumulate, relabel, hold
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.set_xlim(-8, 8)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_xlabel("screen position")
    title = ax.set_title("")
    sc = ax.scatter([], [], s=6)
    colours = {"D1": sv.C["blue"], "D2": sv.C["orange"], "D3": "#2a2f37", "D4": "#2a2f37"}
    final = np.array([colours[d] for d in det])

    def frame(i):
        if i < phase1:
            k = int(n_show * (i + 1) / phase1)
            sc.set_offsets(np.c_[x[:k], y[:k]])
            sc.set_color([sv.FG] * k)
            title.set_text(f"t₁: signal photons hit the screen — {k} hits, no fringes")
        else:
            j = min(i - phase1, phase2)
            k = int(n_show * j / phase2)
            cols = np.array([sv.FG] * n_show, dtype=object)
            cols[:k] = final[:k]
            sc.set_offsets(np.c_[x, y])
            sc.set_color(list(cols))
            title.set_text("t₂ (later): idler results arrive → colour each old dot by its partner's detector\n"
                           "blue = D1, orange = D2, dark = which-path.  The dots did not move.")
        return (sc, title)

    anim = animation.FuncAnimation(fig, frame, frames=phase1 + phase2 + hold)
    sv.save_anim(anim, OUT / "eraser_relabel.mp4", fps=fps)


if __name__ == "__main__":
    sv.apply_style()
    x, eraser, det = run(120_000)
    stats = static_figure(x, eraser, det)
    for k, v in stats.items():
        print(f"  fringe contrast — {k:<35s} {v:.2f}")
    chi2, dof = no_signalling_check(x, eraser)
    print(f"  no-signalling check: chi² = {chi2:.1f} on {dof} dof "
          f"(≈ dof means the later choice left NO trace on the screen)")
    relabel_animation(x, det)
