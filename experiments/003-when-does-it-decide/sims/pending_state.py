"""Sim D1 — When does an undecided photon get decided? Interaction count vs. timeout.

Two engine designs for "pending state" (an unresolved photon path):

  INTERACTION RULE (decoherence): the pending value survives until other things read / copy it.
      Each interaction i leaves a record with distinguishability d_i ∈ [0, 1]; the remaining
      coherence is ∏ (1 − d_i). Air or glass: many interactions with d ≈ 0 (coherent forward
      scattering, no record). A nebula absorbing and re-emitting: one interaction with d = 1.
  TIMEOUT RULE (a garbage-collection deadline): pending state is force-committed after T seconds
      of host time, whether or not anything touched it.

Observed anchors (see research/prior-art.md for sources; verify before publishing):
  * light from distant quasars still interferes between separate telescopes: 3C 273 (z = 0.158, ~2.0 Gyr;
    GRAVITY 2018) and a z = 2.325 quasar (~11 Gyr; GRAVITY+ 2024)
  * entanglement survives ≥ 10 s in a lab memory (Experiment 001 research)
A timeout shorter than the travel time would erase quasar interference, so an isolated photon's
timeout must exceed its travel time. The interaction rule predicts exactly what's seen.

Outputs:
  output/pending_scenarios.png   coherence remaining along each scenario, both rules
  output/timeout_bounds.png      lower bounds on any pending-state timeout, by experiment
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)
YEAR = 3.156e7


def coherence_interactions(events):
    """events: list of distinguishabilities d_i, in order. Returns running coherence."""
    c = np.cumprod([1.0] + [1 - d for d in events])
    return c


def scenarios(rng):
    return {
        "empty space (10⁹ years, no interactions)": [],
        "Earth's atmosphere (~10²⁰ tiny forward scatterings, d≈0)": list(np.full(200, 1e-22)),
        "thin dust (a few weak, partial records)": list(rng.uniform(0.02, 0.15, 12)),
        "nebula (absorbed + re-emitted: d = 1)": [0.0] * 5 + [1.0] + [0.0] * 5,
        "a detector pixel (a full record)": [1.0],
    }


def main():
    sv.apply_style()
    rng = np.random.default_rng(3)
    sc = scenarios(rng)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    cols = [sv.C["green"], sv.C["blue"], sv.C["yellow"], sv.C["orange"], sv.C["red"]]
    for (name, ev), col in zip(sc.items(), cols):
        c = coherence_interactions(ev)
        x = np.linspace(0, 1, len(c))
        ax.step(x, c, where="post", lw=3, color=col, label=f"{name}: {c[-1]:.2f} left")
        print(f"  interaction rule · {name:<58s} coherence left = {c[-1]:.3f}")
    ax.set_xlabel("progress along the photon's journey")
    ax.set_ylabel("how undecided the path still is (coherence)")
    ax.set_ylim(-0.05, 1.1)
    ax.set_title("Decided by what touches it, not by how long it has been waiting")
    ax.legend(loc="lower left", fontsize=10)
    sv.save(fig, OUT / "pending_scenarios.png")

    # lower bounds on a timeout rule
    bounds = [
        ("lab: entangled ion–photon kept in memory", 10.0),
        ("lab: delayed choice across 144 km (Canary Islands)", 450e-6),
        ("space: ground–satellite delayed-choice", 10e-3),
        ("cosmic: 3C 273 light interfering after ~2.0×10⁹ yr (GRAVITY 2018)", 2.0e9 * YEAR),
        ("cosmic: z = 2.3 quasar light interfering after ~1.1×10¹⁰ yr (GRAVITY+ 2024)", 1.1e10 * YEAR),
    ]
    fig, ax = plt.subplots(figsize=sv.WIDE)
    names = [b[0] for b in bounds]
    vals = [b[1] for b in bounds]
    ax.barh(names, vals, color=[sv.C["pink"], sv.C["purple"], sv.C["blue"], sv.C["green"], sv.C["yellow"]])
    ax.set_xscale("log")
    for i, v in enumerate(vals):
        ax.text(v * 1.5, i, f"≥ {v:.1e} s", va="center", fontsize=12)
    ax.set_xlabel("any pending-state timeout must be at least… (seconds, log scale)")
    ax.set_title("If the engine had a timeout on undecided state, it's longer than the universe's photons fly")
    ax.set_xlim(1e-5, 1e20)
    ax.grid(axis="y", visible=False)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    sv.save(fig, OUT / "timeout_bounds.png")
    for n, v in bounds:
        print(f"  timeout ≥ {v:.2e} s  ({n})")


if __name__ == "__main__":
    main()
