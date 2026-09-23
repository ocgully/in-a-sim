"""Sim 4 — What does each interpretation cost to host?

We run the same little quantum "world" (n entangled qubits, scrambled every
round, one qubit observed per round) on three engine designs:

  MANY-WORLDS  : never discard anything. An observation is just the qubit
                 entangling with a fresh "pointer/environment" qubit. Every
                 branch stays in memory.
  COLLAPSE     : on observation, sample an outcome (Born rule), project, and
                 garbage-collect the branch that did not happen.
  DETERMINISTIC: COLLAPSE, but the dice are a seeded PRNG. Same seed -> same
                 history, bit for bit (a replay file / lockstep RTS model).

We then check that an inhabitant keeping a lab notebook of outcomes cannot tell
the three engines apart statistically — only the host's memory bill differs.

Caveat baked into the write-up: this is the cost for a naive state-vector host.
A smarter host (tensor networks, stabiliser tricks, lazy evaluation) changes the
constants, and Many-Worlds proponents would say the branches exist either way.

Outputs:
  output/branching_memory.png   amplitudes stored vs. number of observations
  output/branching_records.png  outcome-record statistics: MWI weights vs collapse runs
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = sv.out_dir(__file__)


def random_u2(rng):
    z = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def apply_1q(psi, u, axis):
    return np.moveaxis(np.tensordot(u, psi, axes=([1], [axis])), 0, axis)


def apply_cz(psi, a, b):
    idx = [slice(None)] * psi.ndim
    idx[a], idx[b] = 1, 1
    psi = psi.copy()
    psi[tuple(idx)] *= -1
    return psi


def scramble(psi, n_sys, gates):
    for q in range(n_sys):
        psi = apply_1q(psi, gates[q], q)
    for q in range(n_sys - 1):
        psi = apply_cz(psi, q, q + 1)
    return psi


def mwi_observe(psi, q):
    """Entangle system qubit q with a new pointer qubit (appended as last axis)."""
    shape = [1] * psi.ndim
    shape[q] = 2
    m0 = np.array([1, 0]).reshape(shape)
    m1 = np.array([0, 1]).reshape(shape)
    return np.stack([psi * m0, psi * m1], axis=-1)


def collapse_observe(psi, q, rng):
    p1 = np.sum(np.abs(np.take(psi, 1, axis=q)) ** 2)
    outcome = int(rng.random() < p1)
    mask_shape = [1] * psi.ndim
    mask_shape[q] = 2
    mask = np.zeros(2)
    mask[outcome] = 1
    psi = psi * mask.reshape(mask_shape)
    return psi / np.linalg.norm(psi), outcome


def world(n_sys, rounds, seed_gates):
    rng = np.random.default_rng(seed_gates)
    gates = [[random_u2(rng) for _ in range(n_sys)] for _ in range(rounds)]
    psi = np.zeros([2] * n_sys, complex)
    psi[(0,) * n_sys] = 1
    return psi, gates


def run_mwi(n_sys, rounds, seed_gates=0):
    psi, gates = world(n_sys, rounds, seed_gates)
    sizes, times = [psi.size], [0.0]
    t0 = time.perf_counter()
    for r in range(rounds):
        # scramble acts only on the system axes (pointer axes ride along)
        for q in range(n_sys):
            psi = apply_1q(psi, gates[r][q], q)
        for q in range(n_sys - 1):
            psi = apply_cz(psi, q, q + 1)
        psi = mwi_observe(psi, r % n_sys)
        sizes.append(psi.size)
        times.append(time.perf_counter() - t0)
    return psi, sizes, times


def run_collapse(n_sys, rounds, rng, seed_gates=0):
    psi, gates = world(n_sys, rounds, seed_gates)
    record, sizes = [], [psi.size]
    for r in range(rounds):
        psi = scramble(psi, n_sys, gates[r])
        psi, o = collapse_observe(psi, r % n_sys, rng)
        record.append(o)
        sizes.append(psi.size)
    return tuple(record), sizes


def memory_figure():
    n_sys, rounds = 8, 14
    _, sizes_mwi, t_mwi = run_mwi(n_sys, rounds)
    _, sizes_col = run_collapse(n_sys, rounds, np.random.default_rng(0))
    k = np.arange(rounds + 1)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.semilogy(k, sizes_mwi, "o-", color=sv.C["green"], lw=3, label="Many-Worlds host: keep every branch")
    ax.semilogy(k, sizes_col, "s-", color=sv.C["pink"], lw=3, label="Collapse host: garbage-collect unobserved branch")
    kk = np.arange(rounds, 60)
    ax.semilogy(kk, sizes_mwi[-1] * 2.0 ** (kk - rounds), ":", color=sv.C["green"], lw=2)
    ax.axhline(8 * 2**30 / 16, color=sv.C["yellow"], ls="--", lw=1.5)
    ax.text(1, 8 * 2**30 / 16 * 1.6, "8 GB of RAM (complex128)", color=sv.C["yellow"])
    ax.axhline(2**30 * 1e6 * 8 / 16, color=sv.C["red"], ls="--", lw=1.5)
    ax.text(1, 2**30 * 1e6 * 8 / 16 * 1.6, "8 petabytes", color=sv.C["red"])
    ax.set_xlabel("number of observations (measurements)")
    ax.set_ylabel("complex amplitudes the host must store")
    ax.set_title(f"Same {n_sys}-qubit world, same lab notebooks — very different server bills")
    ax.legend(loc="upper left")
    ax.set_xlim(0, 59)
    sv.save(fig, OUT / "branching_memory.png")
    print(f"  MWI after {rounds} observations: {sizes_mwi[-1]:,} amplitudes ({t_mwi[-1]*1000:.0f} ms); "
          f"collapse: {sizes_col[-1]:,}")
    print(f"  each extra observation doubles MWI memory; 2^266 ≈ 10^80 (atoms in the observable universe)")


def records_figure():
    """Inhabitants' view: distribution of outcome records must match across engines."""
    n_sys, rounds = 3, 5
    psi, _, _ = run_mwi(n_sys, rounds, seed_gates=42)
    # MWI branch weight of each record = norm² over system axes for fixed pointer values
    weights = np.sum(np.abs(psi) ** 2, axis=tuple(range(n_sys))).ravel()
    recs = list(itertools.product([0, 1], repeat=rounds))
    trials = 40_000
    rng_true = np.random.default_rng(2026)       # stand-in for "true" randomness; seeded so the numbers reproduce
    counts = {r: 0 for r in recs}
    for _ in range(trials):
        rec, _ = run_collapse(n_sys, rounds, rng_true, seed_gates=42)
        counts[rec] += 1
    freq = np.array([counts[r] / trials for r in recs])
    # deterministic: same seed twice -> identical histories
    h1 = run_collapse(n_sys, rounds, np.random.default_rng(7), 42)[0]
    h2 = run_collapse(n_sys, rounds, np.random.default_rng(7), 42)[0]
    tvd = 0.5 * np.abs(freq - weights).sum()
    print(f"  records: total-variation distance MWI weights vs collapse frequencies = {tvd:.4f} "
          f"(sampling noise ~{np.sqrt(len(recs)/trials)/2:.3f})")
    print(f"  deterministic replay: seed 7 twice -> {h1} vs {h2} identical={h1 == h2}")

    fig, ax = plt.subplots(figsize=sv.WIDE)
    xi = np.arange(len(recs))
    ax.bar(xi - 0.2, weights, 0.4, color=sv.C["green"], label="Many-Worlds: branch weight (computed exactly)")
    ax.bar(xi + 0.2, freq, 0.4, color=sv.C["pink"], label=f"Collapse: frequency over {trials:,} runs")
    ax.set_xticks(xi[::2])
    ax.set_xticklabels(["".join(map(str, r)) for r in recs][::2], rotation=90, fontsize=9)
    ax.set_xlabel("lab-notebook record of 5 observations")
    ax.set_ylabel("probability")
    ax.set_title(f"From inside, the engines agree (TVD = {tvd:.3f}) — only the host sees the difference")
    ax.legend()
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    sv.save(fig, OUT / "branching_records.png")


if __name__ == "__main__":
    sv.apply_style()
    memory_figure()
    records_figure()
