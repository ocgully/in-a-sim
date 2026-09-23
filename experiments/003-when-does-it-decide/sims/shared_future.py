"""Sim D2 — Entanglement as a pointer: a stored value vs. a shared future.

The author's intuition: entangled particles are like two references to the same object.
This sim writes that literally in code, two ways, and plays the Bell/CHSH game:

  StoredValue   both particles point at a value fixed when the pair was created
                (a pointer to data; this is a local hidden variable)
  SharedFuture  both particles point at an unresolved promise; the FIRST reader resolves it
                using ITS measurement angle; the second reader gets a correlated answer
                (lazy evaluation; this is Experiment 001's "authoritative server" design)

Only the shared future reaches the measured 2√2 ≈ 2.83. And neither reader can use it to send a
message: each side's own results stay 50/50 whatever the other side does.
"""
from __future__ import annotations

import math
import random


class StoredValue:
    """Pointer to data decided at creation: a hidden polarisation angle."""
    def __init__(self, rng):
        self.lam = rng.uniform(0, math.pi)

    def read(self, angle, rng):
        return 1 if math.cos(2 * (angle - self.lam)) >= 0 else -1


class SharedFuture:
    """Pointer to a promise: resolved on first read, with the first reader's angle."""
    def __init__(self, rng):
        self.first = None          # (angle, outcome) once resolved

    def read(self, angle, rng):
        if self.first is None:
            out = rng.choice((1, -1))
            self.first = (angle, out)
            return out
        a0, o0 = self.first
        same = rng.random() < math.cos(a0 - angle) ** 2
        return o0 if same else -o0


def chsh(kind, n=200_000, seed=1):
    rng = random.Random(seed)
    A = (0.0, math.pi / 4)
    B = (math.pi / 8, -math.pi / 8)
    tot = {(i, j): [0, 0] for i in range(2) for j in range(2)}
    bob_plus = {0: [0, 0], 1: [0, 0]}
    for _ in range(n):
        obj = kind(rng)                         # the pair shares ONE object (the pointer target)
        i, j = rng.randrange(2), rng.randrange(2)
        if rng.random() < 0.5:                  # who reads first is random, as it is at spacelike separation
            a = obj.read(A[i], rng); b = obj.read(B[j], rng)
        else:
            b = obj.read(B[j], rng); a = obj.read(A[i], rng)
        tot[(i, j)][0] += a * b
        tot[(i, j)][1] += 1
        bob_plus[i][0] += b == 1
        bob_plus[i][1] += 1
    E = {k: s / c for k, (s, c) in tot.items()}
    S = E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]
    marg = [bob_plus[k][0] / bob_plus[k][1] for k in (0, 1)]
    return S, marg


if __name__ == "__main__":
    for kind in (StoredValue, SharedFuture):
        S, m = chsh(kind)
        print(f"  {kind.__name__:<12s} CHSH S = {S:5.3f}   Bob P(+1) given Alice's setting a0/a1 = {m[0]:.3f} / {m[1]:.3f}")
    print("  classical limit 2 · measured ≈ 2.83 (2√2)")
