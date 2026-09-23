"""Sim 3 — Bell / CHSH: which server architecture can reproduce reality's scoreboard?

Two players (Alice, Bob) are far apart. Each gets a random setting and must
output ±1. CHSH score S = E(a0,b0) + E(a0,b1) + E(a1,b0) − E(a1,b1).

Loophole-free experiments (Hensen 2015, Giustina 2015, Shalm 2015) measure
S ≈ 2√2 ≈ 2.83 on entangled particles. We implement several game-engine
architectures and see which can hit that number, and at what architectural cost:

  A. CLIENT-SIDE PREDICTION (local hidden variables): each particle leaves the
     source carrying a pre-computed answer table. No talking later.
  B. AUTHORITATIVE SERVER (collapse/rollback-like): outcomes are resolved at
     measurement time by a server that sees BOTH settings.
  C. GREEDY SERVER (Popescu–Rohrlich box): same architecture as B, but maximises S.
  D. PRE-SCRIPTED REPLAY (superdeterminism / deterministic sim): one global seed
     pre-computes the particles AND the "random" settings the players will pick.
  E. KEEP EVERY BRANCH (Many-Worlds bookkeeping): no sampling; store every outcome
     branch with its weight and score from the weights.
  F. LEAKY SERVER: like B but Bob's marginal depends on Alice's setting (signalling).

Photon polarisation convention: E(α, β) = cos 2(α − β).
Settings: a0 = 0°, a1 = 45°, b0 = 22.5°, b1 = −22.5°.

Outputs:
  output/bell_scoreboard.png     S for each architecture vs. the 2 / 2√2 / 4 bounds
  output/bell_correlation.png    E(Δθ): local model (straight lines) vs quantum (cosine)
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)
A_ANG = np.deg2rad([0.0, 45.0])
B_ANG = np.deg2rad([22.5, -22.5])
N = 400_000


def chsh(a_set, b_set, A, B):
    E = np.zeros((2, 2))
    for i, j in itertools.product(range(2), range(2)):
        m = (a_set == i) & (b_set == j)
        E[i, j] = np.mean(A[m] * B[m])
    return E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1], E


def marginals(a_set, b_set, B):
    """P(Bob = +1 | Alice's setting) — must not depend on Alice's setting (no signalling)."""
    return [np.mean(B[a_set == i] == 1) for i in range(2)]


def settings(rng):
    return rng.integers(0, 2, N), rng.integers(0, 2, N)


def arch_A_local(rng):
    a, b = settings(rng)
    lam = rng.uniform(0, np.pi, N)                   # hidden polarisation carried by both
    A = np.sign(np.cos(2 * (A_ANG[a] - lam)))
    B = np.sign(np.cos(2 * (B_ANG[b] - lam)))
    return a, b, A, B


def best_deterministic_local():
    """Exhaustive: every possible pre-computed answer table. Max |S| over all 16."""
    best = 0
    for A0, A1, B0, B1 in itertools.product([-1, 1], repeat=4):
        best = max(best, abs(A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1))
    return best


def arch_B_server(rng):
    a, b = settings(rng)
    A = rng.choice([-1, 1], N)                       # server: Alice's result is a fair coin
    same = rng.random(N) < np.cos(A_ANG[a] - B_ANG[b]) ** 2   # needs BOTH settings -> nonlocal
    B = np.where(same, A, -A)
    return a, b, A, B


def arch_C_pr_box(rng):
    a, b = settings(rng)
    A = rng.choice([-1, 1], N)
    B = np.where(a * b == 1, -A, A)                  # perfect CHSH strategy
    return a, b, A, B


def arch_D_superdeterministic(rng):
    # One seed decides everything, *including* what the players will "choose".
    a, b = settings(rng)                             # the script already knows these
    # The source reads the script and pre-loads each particle with the answer for the
    # setting it WILL meet. Each particle is then purely local at detection time.
    A = rng.choice([-1, 1], N)
    same = rng.random(N) < np.cos(A_ANG[a] - B_ANG[b]) ** 2
    B = np.where(same, A, -A)
    return a, b, A, B


def arch_E_many_worlds():
    """No sampling: build |Φ+> and score from exact branch weights."""
    phi = np.array([1, 0, 0, 1]) / np.sqrt(2)        # |HH> + |VV>
    def basis(t):
        return np.array([np.cos(t), np.sin(t)]), np.array([-np.sin(t), np.cos(t)])
    E = np.zeros((2, 2))
    branches = 0
    for i, j in itertools.product(range(2), range(2)):
        pa, ma = basis(A_ANG[i])
        pb, mb = basis(B_ANG[j])
        for sa, va in ((1, pa), (-1, ma)):
            for sb, vb in ((1, pb), (-1, mb)):
                w = abs(np.kron(va, vb) @ phi) ** 2   # branch weight
                E[i, j] += sa * sb * w
                branches += 1
    return E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1], branches


def arch_F_leaky(rng):
    a, b, A, B = arch_B_server(rng)
    flip = (a == 1) & (rng.random(N) < 0.3)           # Alice's setting biases Bob's marginal
    B = np.where(flip, 1, B)
    return a, b, A, B


def main():
    sv.apply_style()
    rng = np.random.default_rng(1964)                # Bell's paper year
    rows = []
    for name, fn, arch in [
        ("A  client-side prediction\n(local hidden variables)", arch_A_local, "local"),
        ("B  authoritative server\n(resolve at measurement)", arch_B_server, "nonlocal"),
        ("C  greedy server\n(PR box)", arch_C_pr_box, "nonlocal"),
        ("D  pre-scripted replay\n(superdeterminism)", arch_D_superdeterministic, "local + no free choice"),
        ("F  leaky server\n(signalling)", arch_F_leaky, "nonlocal"),
    ]:
        a, b, A, B = fn(rng)
        S, _ = chsh(a, b, A, B)
        mb = marginals(a, b, B)
        rows.append((name, S, mb, arch))
    S_mwi, n_br = arch_E_many_worlds()
    rows.insert(4, ("E  keep every branch\n(Many-Worlds)", S_mwi, [0.5, 0.5], f"exact, {n_br} branches"))

    print(f"  best possible deterministic local table: |S| = {best_deterministic_local()}")
    print(f"  {'architecture':<45s} {'S':>6s}   P(Bob=+1 | Alice a0/a1)   notes")
    for name, S, mb, arch in rows:
        print(f"  {name.replace(chr(10), ' '):<45s} {S:6.3f}   {mb[0]:.3f} / {mb[1]:.3f}            {arch}")

    fig, ax = plt.subplots(figsize=sv.WIDE)
    names = [r[0] for r in rows]
    vals = [r[1] for r in rows]
    cols = [sv.C["blue"], sv.C["pink"], sv.C["red"], sv.C["purple"], sv.C["green"], sv.C["yellow"]]
    bars = ax.barh(names[::-1], vals[::-1], color=cols[::-1])
    for bar, v in zip(bars, vals[::-1]):
        ax.text(v + 0.05, bar.get_y() + bar.get_height() / 2, f"{v:.2f}", va="center", fontsize=13)
    for x, lbl, c in [(2, "classical limit 2", sv.MUTED), (2 * np.sqrt(2), "nature / Tsirelson 2√2", sv.C["green"]),
                      (4, "algebraic max 4", sv.C["red"])]:
        ax.axvline(x, color=c, ls="--", lw=2, label=lbl)
    ax.legend(loc="lower right", fontsize=11, facecolor=sv.BG, framealpha=0.9, frameon=True)
    ax.set_axisbelow(True)
    leak = rows[-1][2]
    ax.text(0.1, 0, f"breaks no-signalling: Bob's P(+1) shifts {leak[0]:.2f} → {leak[1]:.2f}\nwith Alice's setting = FTL messaging (never observed)",
            va="center", fontsize=10, color=sv.BG, weight="bold")
    ax.set_xlim(0, 4.6)
    ax.set_xlabel("CHSH score S  (experiments measure ≈ 2.83)")
    ax.set_title("Which engine architecture reproduces the Bell-test scoreboard?")
    ax.grid(axis="y", visible=False)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    sv.save(fig, OUT / "bell_scoreboard.png")

    # correlation curve
    d = np.linspace(0, np.pi / 2, 200)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.plot(np.rad2deg(d), np.cos(2 * d), color=sv.C["green"], lw=3, label="quantum prediction / experiment: cos 2Δθ")
    ax.plot(np.rad2deg(d), 1 - 4 * d / np.pi, color=sv.C["blue"], lw=3, ls="--",
            label="best 'pre-computed answer' model (A): straight line")
    ax.fill_between(np.rad2deg(d), np.cos(2 * d), 1 - 4 * d / np.pi, color=sv.C["yellow"], alpha=0.2)
    ax.text(18, 0.35, "the gap a local engine\ncannot close", color=sv.C["yellow"], fontsize=13)
    ax.set_xlabel("angle between detectors Δθ (degrees)")
    ax.set_ylabel("correlation E")
    ax.set_title("Entangled correlations bend in a way pre-loaded answers can't")
    ax.legend(loc="lower left")
    sv.save(fig, OUT / "bell_correlation.png")


if __name__ == "__main__":
    main()
