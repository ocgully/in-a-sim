"""Sim G1 — A distributed engine whose regional clock rates obey Poisson's equation.

Engine rule (a toy "consensus clock" scheduler on a 3-D grid of regions):

    each tick, every region sets its tick rate to the AVERAGE of its six
    neighbours' rates (so adjacent regions stay close enough in time to keep
    exchanging boundary/halo data), MINUS a penalty proportional to its own
    compute load. Far-away empty space is pinned at full speed (rate = 1).

    r_i  <-  mean(r_neighbours) - alpha * load_i

That is a Jacobi relaxation step. Its fixed point satisfies the discrete
Poisson equation  ∇²r ∝ load  — the same equation Newtonian gravity obeys
(∇²Φ = 4πGρ), and in weak-field GR a clock's rate is  ≈ 1 + Φ/c².

So: IF load ∝ mass-energy, THEN this scheduler's "lag field" has the same shape
as gravitational time dilation: flat inside nothing, falling off as 1/r outside
a lump. We verify the 1/r fall-off numerically.

This is a construction, not a discovery: any local averaging process with
sources gives Poisson. The interesting question (see findings.md) is whether
there is any *reason* a real engine would schedule this way, and why load would
track mass-energy rather than, say, information complexity.

Outputs:
  output/lagfield_slice.png     tick-rate map through the middle of the world
  output/lagfield_profile.png   radial tick-rate deficit vs 1/r (Newtonian shape)
  output/lagfield_relax.mp4     the lag spreading out tick by tick (2-D slice)
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
N = 72                  # regions per side
ALPHA = 2e-4            # rate penalty per unit load per tick
R_BALL = 5              # radius (in regions) of the "planet"


def make_load(n=N, r_ball=R_BALL):
    z, y, x = np.indices((n, n, n)) - n // 2
    rr = np.sqrt(x**2 + y**2 + z**2)
    load = (rr <= r_ball).astype(float)      # uniform density ball: 1 unit of work per region
    return load, rr


def relax(load, iters, snapshot_every=None):
    r = np.ones_like(load)
    snaps = []
    for k in range(iters):
        nb = (np.roll(r, 1, 0) + np.roll(r, -1, 0) + np.roll(r, 1, 1) + np.roll(r, -1, 1)
              + np.roll(r, 1, 2) + np.roll(r, -1, 2)) / 6.0
        r = nb - ALPHA * load
        # empty space at the edge of the world runs at full speed
        r[0, :, :] = r[-1, :, :] = r[:, 0, :] = r[:, -1, :] = r[:, :, 0] = r[:, :, -1] = 1.0
        if snapshot_every and k % snapshot_every == 0:
            snaps.append(r[N // 2].copy())
    return r, snaps


def main():
    sv.apply_style()
    load, rr = make_load()
    print(f"  relaxing {N}³ = {N**3:,} regions …")
    r, snaps = relax(load, iters=9000, snapshot_every=60)
    deficit = 1 - r

    # --- slice
    fig, ax = plt.subplots(figsize=sv.WIDE)
    im = ax.imshow(r[N // 2], cmap="magma", origin="lower", extent=[-N / 2, N / 2, -N / 2, N / 2])
    ax.contour(np.linspace(-N / 2, N / 2, N), np.linspace(-N / 2, N / 2, N), r[N // 2], levels=12,
               colors="white", linewidths=0.6, alpha=0.5)
    circ = plt.Circle((0, 0), R_BALL, fill=False, color=sv.C["blue"], lw=2, ls="--")
    ax.add_patch(circ)
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax)
    cb.set_label("local tick rate (1 = full speed)")
    ax.set_title("A load-averaging scheduler: busy region (dashed) drags nearby clocks down")
    ax.set_xlabel("regions")
    sv.save(fig, OUT / "lagfield_slice.png")

    # --- radial profile vs 1/r
    mask = (rr > R_BALL + 1) & (rr < N / 2 - 12)
    rad = rr[mask].ravel()
    d = deficit[mask].ravel()
    # fit d ≈ A/r + B (B absorbs the finite-box boundary offset)
    Amat = np.c_[1 / rad, np.ones_like(rad)]
    (A, B), *_ = np.linalg.lstsq(Amat, d, rcond=None)
    resid = d - (A / rad + B)
    r2 = 1 - resid.var() / d.var()
    # compare against a power law fit to show the exponent
    p = np.polyfit(np.log(rad), np.log(d - B), 1)
    print(f"  outside the lump: deficit ≈ {A:.4g}/r + {B:.2g}   (R² = {r2:.5f}); "
          f"log-log slope of (deficit - offset) = {p[0]:.3f}  (Newton: -1)")
    # continuum Poisson prediction: ∇²r = 6·ALPHA·load  ->  deficit = 6·ALPHA·M / (4π r)
    M = load.sum()
    print(f"  analytic Poisson prediction A = 6·α·M/(4π) = {6 * ALPHA * M / (4 * np.pi):.4g}  (M = {M:.0f} loaded regions)")

    fig, ax = plt.subplots(figsize=sv.WIDE)
    alld = deficit.ravel()
    allr = rr.ravel()
    sel = allr < N / 2 - 1
    ax.scatter(allr[sel][::7], alld[sel][::7], s=2, color=sv.C["orange"], alpha=0.35, label="every region (sampled)")
    rs = np.linspace(R_BALL, N / 2 - 1, 300)
    ax.plot(rs, A / rs + B, color=sv.C["green"], lw=3, label=f"fit A/r + B  (R² = {r2:.4f})")
    ax.axvline(R_BALL, color=sv.C["blue"], ls="--")
    ax.text(R_BALL + 0.4, alld.max() * 0.92, "surface of\nthe busy lump", color=sv.C["blue"])
    ax.set_xlabel("distance from centre (regions)")
    ax.set_ylabel("tick-rate deficit  1 − r")
    ax.set_title("Outside the lump the lag falls off as 1/r — the shape of Newtonian potential")
    ax.legend()
    sv.save(fig, OUT / "lagfield_profile.png")

    # --- relaxation animation (for video)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.grid(False)
    vmin = r.min()
    im = ax.imshow(snaps[0], cmap="magma", origin="lower", vmin=vmin, vmax=1,
                   extent=[-N / 2, N / 2, -N / 2, N / 2])
    ax.add_patch(plt.Circle((0, 0), R_BALL, fill=False, color=sv.C["blue"], lw=2, ls="--"))
    fig.colorbar(im, ax=ax).set_label("local tick rate")
    ttl = ax.set_title("")

    def frame(i):
        im.set_data(snaps[i])
        ttl.set_text(f"scheduler tick {i*60:5d}: regions average their neighbours' clock rate − own load")
        return im, ttl

    anim = animation.FuncAnimation(fig, frame, frames=len(snaps))
    sv.save_anim(anim, OUT / "lagfield_relax.mp4", fps=30)


if __name__ == "__main__":
    main()
