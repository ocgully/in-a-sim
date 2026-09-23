"""Sim T1 — "Same-tick decisions": would a tick-based engine leave a fingerprint in event timestamps?

Author's idea: if the universe updates in ticks, many quantum "decisions" (detections, decays) would be
made in the SAME tick. That's a batching optimisation, and it could leave a signature:
  1. timestamps of independent events pile up at tick boundaries (a comb when folded modulo the tick)
  2. two INDEPENDENT detectors show excess exact coincidences (same tick) beyond chance

Any real detector smears timestamps with jitter σ. This sim asks how detectable the comb is as a
function of tick length τ relative to σ, and how many events you'd need.

Outputs:
  output/tick_comb.png          folded timestamps: continuous time vs tick engine (τ = 3σ and τ = σ/3)
  output/tick_detectability.png  significance of the comb vs τ/σ for 10⁶ events
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)


def events(n, rate, tick, sigma, rng, engine=True):
    t = np.cumsum(rng.exponential(1 / rate, n))
    if engine:
        t = np.ceil(t / tick) * tick            # the decision is committed at the next tick boundary
    return t + rng.normal(0, sigma, n)          # detector jitter


def comb_strength(t, tick):
    """Rayleigh test for periodicity at the tick: Z = n·|mean(e^{2πi t/τ})|²."""
    ph = 2 * np.pi * (t % tick) / tick
    return len(t) * np.abs(np.mean(np.exp(1j * ph))) ** 2


def main():
    sv.apply_style()
    rng = np.random.default_rng(42)
    sigma, n = 1.0, 1_000_000
    fig, axes = plt.subplots(1, 3, figsize=sv.WIDE, sharey=True)
    for ax, (label, tick, eng) in zip(axes, [("continuous time", 3.0, False),
                                              ("tick engine, tick = 3× jitter", 3.0, True),
                                              ("tick engine, tick = ⅓× jitter", 1 / 3, True)]):
        t = events(200_000, 0.05, tick, sigma, rng, eng)
        ax.hist((t % tick) / tick, bins=60, color=sv.C["blue"] if not eng else sv.C["pink"])
        ax.set_title(label, fontsize=12)
        ax.set_xlabel("timestamp position within a tick")
        ax.set_yticks([])
    fig.suptitle("Fold the timestamps on the tick length: a comb appears only if ticks are longer than the jitter",
                 fontsize=14, weight="bold")
    fig.tight_layout(rect=(0, 0.03, 1, 0.92))
    sv.save(fig, OUT / "tick_comb.png")

    ratios = np.logspace(-1, 0.7, 25)
    Z = []
    for r in ratios:
        t = events(n, 0.05, r * sigma, sigma, rng, True)
        Z.append(comb_strength(t, r * sigma))
    Z = np.array(Z)
    # analytic expectation: Z ≈ n · exp(-(2πσ/τ)²)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.semilogy(ratios, Z, "o-", color=sv.C["pink"], lw=3, label="tick engine (simulated, 10⁶ events)")
    ax.semilogy(ratios, n * np.exp(-(2 * np.pi / ratios) ** 2) + 1, "--", color=sv.C["yellow"], label="theory n·e^{-(2πσ/τ)²}")
    ax.axhline(25, color=sv.C["green"], ls=":", lw=2)
    ax.text(0.11, 30, "≈5σ detection threshold", color=sv.C["green"])
    ax.set_xscale("log")
    ax.set_xlabel("tick length ÷ detector timing jitter")
    ax.set_ylabel("comb strength (Rayleigh Z)")
    ax.set_title("Same-tick decisions are only visible if a tick is longer than about your timing jitter")
    ax.legend()
    sv.save(fig, OUT / "tick_detectability.png")
    thr = ratios[np.argmax(Z > 25)]
    print(f"  with 10⁶ events, the tick comb becomes a ≥5σ signal once tick ≳ {thr:.2f} × timing jitter")
    print("  best photon-timing jitter is ~ps scale → a direct timestamp test probes ticks ≳ 10⁻¹² s;"
          " indirect bounds on a fundamental time step are far tighter (see research, verify)")


if __name__ == "__main__":
    main()
