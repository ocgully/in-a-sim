"""Sim G4 — The exchange rate between "extra lag" and "extra space".

Author's hypothesis: energy doesn't only slow a region's clock (lag), it also ADDS SPACE
(more cells / more room). How much of each?

Weak-field bookkeeping, per unit of Newtonian potential Φ/c² (Φ < 0 near mass):
    local tick rate      ≈ 1 + a·Φ/c²     (a = "lag" coefficient)
    local ruler / cells  ≈ 1 − b·Φ/c²     (b = "extra space" coefficient)
A light signal moves one cell per tick locally, so seen from outside its speed is
    v ≈ c · (1 + (a + b)·Φ/c²)   →   effective refractive index n ≈ 1 − (a + b)Φ/c²

Two independent measurements pin a and b:
  * FREE FALL of slow matter only feels the clock gradient → a = 1 exactly (Sim G2A).
  * LIGHT sees both → bending and radar echo delay scale with (a + b) = 1 + γ, where γ
    (the PPN parameter) = b / a. Cassini: γ = 1 + (2.1 ± 2.3)×10⁻⁵.

So nature's exchange rate is b/a = 1: every bit of lag comes with exactly the same
fraction of extra space. This sim computes what different "engine designs" (different
b) would predict for starlight bending at the Sun and for the radar echo delay
(Shapiro delay) of a signal grazing the Sun on its way to Mars and back, then
compares them with the measurement.

Outputs:
  output/exchange_rate.png   predictions vs b, with the measured value
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)
GM, C = 1.32712440018e20, 299792458.0
R_SUN, R_EARTH_ORBIT, R_MARS_ORBIT = 6.957e8, 1.496e11, 2.279e11
ARCSEC = 180 / np.pi * 3600


def bending(a, b, impact=R_SUN):
    return (a + b) * 2 * GM / (impact * C**2) * ARCSEC


def shapiro_round_trip(a, b, impact=R_SUN):
    """Excess round-trip time for a radar pulse Earth → (grazing Sun) → Mars → back."""
    return 2 * (a + b) * GM / C**3 * np.log(4 * R_EARTH_ORBIT * R_MARS_ORBIT / impact**2)


def main():
    sv.apply_style()
    designs = [
        ("lag only (no extra space)", 1.0, 0.0),
        ("extra space only (no lag)", 0.0, 1.0),
        ("lag + space, 1 : 1", 1.0, 1.0),
        ("space grows as volume (b = 3)", 1.0, 3.0),
    ]
    print(f"  {'engine design':<34s} {'a':>4s} {'b':>4s}   bending″   echo delay (µs)   falls correctly?")
    for name, a, b in designs:
        print(f"  {name:<34s} {a:4.1f} {b:4.1f}   {bending(a, b):7.3f}   {shapiro_round_trip(a, b)*1e6:10.1f}"
              f"         {'yes' if a == 1 else 'NO (objects would not fall at g)'}")
    print(f"  measured: bending 1.75″ (VLBI, γ≈1), Cassini γ−1 = (2.1±2.3)e-5 → b/a = 1.00000 ± 0.00002")

    bs = np.linspace(0, 3, 301)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=sv.WIDE)
    ax1.plot(bs, bending(1, bs), color=sv.C["blue"], lw=3)
    ax1.axhline(bending(1, 1), color=sv.C["green"], ls="--")
    ax1.axvline(1, color=sv.C["green"], ls="--")
    ax1.scatter([0, 1, 3], [bending(1, 0), bending(1, 1), bending(1, 3)], color=[sv.C["orange"], sv.C["green"], sv.C["red"]], s=80, zorder=5)
    ax1.set_xlabel("extra-space coefficient b  (lag fixed at a = 1 by free fall)")
    ax1.set_ylabel("starlight bending at the Sun's edge (″)")
    ax1.set_title("Bending: nature says b = a")
    ax2.plot(bs, shapiro_round_trip(1, bs) * 1e6, color=sv.C["pink"], lw=3)
    ax2.axhline(shapiro_round_trip(1, 1) * 1e6, color=sv.C["green"], ls="--")
    ax2.axvline(1, color=sv.C["green"], ls="--")
    ax2.set_xlabel("extra-space coefficient b")
    ax2.set_ylabel("Earth→Sun-graze→Mars radar echo delay (µs)")
    ax2.set_title("Echo delay: same answer")
    fig.suptitle("Every bit of lag comes with exactly as much extra space (γ = 1 to 2×10⁻⁵)", fontsize=16, weight="bold")
    fig.tight_layout(rect=(0, 0.03, 1, 0.93))
    sv.save(fig, OUT / "exchange_rate.png")


if __name__ == "__main__":
    main()
