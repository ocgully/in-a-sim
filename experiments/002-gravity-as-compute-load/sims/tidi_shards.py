"""Sim G3 — Real-world precedent: MMO "Time Dilation" (EVE Online style TiDi).

EVE Online runs each star system on a server node. When a battle overloads a
node, the game deliberately slows that system's clock (down to a 10% floor) so
the simulation stays correct instead of dropping actions. Pilots inside the
battle experience fewer game-seconds per real second than pilots elsewhere.

This toy reproduces the mechanism: fixed compute budget per node, interaction
cost that grows ~N² with the number of ships (every ship can target every
other), dilation = min(1, budget / load), floored at 0.10.

It is the closest *engineered* precedent for "more stuff in a region => time
runs slower there". It also shows where the analogy breaks: dilation is a
step function per shard (not a smooth 1/r field), and it tracks ACTIVITY
(interactions), not mass — a big idle rock costs nothing.

Outputs:
  output/tidi_curve.png    dilation factor vs ships in system
  output/tidi_clocks.png   game-time elapsed in 4 systems during a battle (clock drift)
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)
BUDGET = 400.0 ** 2          # interaction pairs per tick a node can afford at full speed
FLOOR = 0.10                 # EVE's minimum time dilation


def dilation(ships):
    load = np.maximum(np.asarray(ships, float), 1) ** 2
    return np.clip(BUDGET / load, FLOOR, 1.0)


def main():
    sv.apply_style()
    n = np.arange(1, 4001)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.plot(n, dilation(n), color=sv.C["orange"], lw=3)
    ax.axhline(FLOOR, color=sv.C["red"], ls="--")
    ax.text(3000, FLOOR + 0.03, "10% floor", color=sv.C["red"])
    ax.set_xlabel("ships in the star system")
    ax.set_ylabel("game seconds per real second")
    ax.set_title("MMO time dilation: more stuff in a region → that region's clock runs slow")
    sv.save(fig, OUT / "tidi_curve.png")

    # a 90-minute battle: fleets pour into "Battle" system, others stay quiet
    t = np.linspace(0, 90, 901)                        # real minutes
    systems = {
        "Home (20 ships)": np.full_like(t, 20),
        "Neighbour (300 ships)": np.full_like(t, 300),
        "Staging (500 ships)": 300 + 200 * np.clip(t / 20, 0, 1),
        "Battle (up to 3,000 ships)": 50 + 2950 * np.clip((t - 10) / 30, 0, 1) * (t < 75) + 400 * (t >= 75),
    }
    fig, ax = plt.subplots(figsize=sv.WIDE)
    cols = [sv.C["green"], sv.C["blue"], sv.C["purple"], sv.C["red"]]
    dt = t[1] - t[0]
    for (name, ships), col in zip(systems.items(), cols):
        game = np.concatenate([[0], np.cumsum(dilation(ships)[:-1]) * dt])
        ax.plot(t, game, color=col, lw=3, label=f"{name}: {game[-1]:.0f} game-min")
    ax.plot(t, t, color=sv.MUTED, ls=":", lw=1)
    ax.set_xlabel("real (host) minutes")
    ax.set_ylabel("game minutes experienced inside the system")
    ax.set_title("Pilots who fought in the battle come home 'younger' — a twin paradox from load")
    ax.legend(loc="upper left")
    sv.save(fig, OUT / "tidi_clocks.png")
    for name, ships in systems.items():
        print(f"  {name:<28s} experienced {np.sum(dilation(ships)[:-1])*dt:5.1f} game-min of 90 real min")


if __name__ == "__main__":
    main()
