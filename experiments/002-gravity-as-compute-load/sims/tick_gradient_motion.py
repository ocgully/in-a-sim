"""Sim G2 — If clocks tick slower "down there", do things fall? Does light bend?

PART A — MATTER. Quantum mechanically, a particle of mass m carries an internal
clock: its phase turns at the Compton rate ω = mc²/ħ. We tell the engine one
thing only: *every point advances that internal clock at its local tick rate*
r(x) = 1 + g·x/c²  (slower lower down). We never write a force or a potential.
Result: the wave packet falls with acceleration g. (Mathematically, the local
clock rate acts exactly like a potential m c² (r − 1) = m g x — this is the
standard weak-field result that Newtonian gravity lives in the time–time part
of the metric.)

PART B — LIGHT. A tick-rate deficit also slows light, so rays refract toward
slow regions (gravitational lensing as refraction). But a pure "time lag" model
bends light by only HALF the measured amount — Einstein's 1911 (time-only) value
vs his 1915 GR value. Real light bending requires space itself to be stretched
too (PPN γ = 1, measured to ~10⁻⁵ by Cassini). So "lag" alone is not enough.

Outputs:
  output/tick_fall.png          packet centre vs. −½gt² ; snapshots
  output/tick_fall.mp4          packet falling through a clock-rate gradient
  output/light_bending.png      rays: time-only lag vs time+space (GR); solar numbers
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

# ----------------------------------------------------------------- PART A
HBAR = M = 1.0
C2 = 1.0e4          # c² in sim units: big so the clock-rate gradient is tiny, like reality
G = 2.0             # "g" in sim units


def fall(t_end=4.0, dt=2e-3, L=120.0, n=4096, x0=10.0, sigma=2.0):
    x = np.linspace(-L / 2, L / 2, n, endpoint=False)
    k = 2 * np.pi * np.fft.fftfreq(n, d=x[1] - x[0])
    rate = 1 + G * x / C2                        # local tick rate: slower at lower x
    psi = np.exp(-((x - x0) ** 2) / (4 * sigma**2)).astype(complex)
    psi /= np.linalg.norm(psi)
    # split-step: internal clock phase at LOCAL rate, then free propagation
    clock_half = np.exp(-1j * (M * C2 / HBAR) * rate * dt / 2)
    kinetic = np.exp(-1j * HBAR * k**2 / (2 * M) * dt)
    steps = int(t_end / dt)
    ts, xs, snaps = [], [], []
    for s in range(steps + 1):
        if s % 20 == 0:
            p = np.abs(psi) ** 2
            ts.append(s * dt)
            xs.append(np.sum(x * p) / p.sum())
            snaps.append(p.copy())
        psi = clock_half * psi
        psi = np.fft.ifft(kinetic * np.fft.fft(psi))
        psi = clock_half * psi
    return x, np.array(ts), np.array(xs), snaps, rate


def part_a():
    x, ts, xs, snaps, rate = fall()
    x0 = xs[0]
    classical = x0 - 0.5 * G * ts**2
    err = np.max(np.abs(xs - classical))
    print(f"  A: packet fell {x0 - xs[-1]:.2f} units in t={ts[-1]:.1f}; ½gt² = {0.5*G*ts[-1]**2:.2f}; "
          f"max deviation from free-fall parabola = {err:.2e}")
    print(f"     tick-rate difference top-to-bottom of the fall region: {G*(x0-xs[-1])/C2:.1e} "
          f"(Earth: g/c² ≈ 1.1e-16 per metre)")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=sv.WIDE, gridspec_kw=dict(width_ratios=[1.1, 1]))
    ax1.plot(ts, classical, color=sv.C["green"], lw=6, alpha=0.5, label="Newton: x₀ − ½gt²")
    ax1.plot(ts, xs, color=sv.C["orange"], lw=2.5, label="engine: only local clock rates set")
    ax1.set_xlabel("time")
    ax1.set_ylabel("height of packet centre")
    ax1.set_title("It falls — with no force in the code")
    ax1.legend()
    for i, col in zip([0, len(snaps) // 3, 2 * len(snaps) // 3, -1],
                      [sv.C["blue"], sv.C["purple"], sv.C["pink"], sv.C["orange"]]):
        ax2.plot(snaps[i], x, color=col, lw=2, label=f"t = {ts[i]:.1f}")
    ax2.set_ylim(-12, 16)
    ax2.set_xlabel("probability density")
    ax2.set_ylabel("height  (clocks slower ↓)")
    ax2.set_title("Wave packet snapshots")
    ax2.legend(loc="lower right")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    sv.save(fig, OUT / "tick_fall.png")

    # animation
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.grid(False)
    ext = [0, 1, x.min(), x.max()]
    ax.imshow(rate[:, None], extent=ext, aspect="auto", origin="lower", cmap="magma", alpha=0.55)
    line, = ax.plot([], [], color=sv.C["blue"], lw=3)
    ax.set_xlim(0, 1)
    ax.set_ylim(-12, 16)
    ax.set_ylabel("height — background: local tick rate (darker = slower)")
    ax.set_xticks([])
    ttl = ax.set_title("")
    pmax = max(s.max() for s in snaps)

    def frame(i):
        line.set_data(0.05 + 0.85 * snaps[i] / pmax, x)
        ttl.set_text(f"t = {ts[i]:.2f}   only rule: each point ticks its clock at the local rate")
        return line, ttl

    anim = animation.FuncAnimation(fig, frame, frames=len(snaps))
    sv.save_anim(anim, OUT / "tick_fall.mp4", fps=30)


# ----------------------------------------------------------------- PART B
def trace_ray(b, kfac, rs, x_start=-60.0, x_end=60.0, ds=0.01):
    """Eikonal ray through n(r) = 1 + kfac·rs/(2r)  (rs = Schwarzschild radius units).
    kfac = 1: only clocks slowed (time-only).  kfac = 2: clocks + space stretched (GR, weak field)."""
    pos = np.array([x_start, b], float)
    d = np.array([1.0, 0.0])
    path = [pos.copy()]
    while pos[0] < x_end:
        r = np.hypot(*pos)
        n = 1 + kfac * rs / (2 * r)
        grad = -kfac * rs / (2 * r**3) * pos
        d = d + ds * (grad - np.dot(grad, d) * d) / n
        d /= np.linalg.norm(d)
        pos = pos + ds * d
        path.append(pos.copy())
    path = np.array(path)
    return path, np.arctan2(-d[1], d[0])


def part_b():
    rs_demo = 1.2
    fig, (ax, bx) = plt.subplots(1, 2, figsize=sv.WIDE, gridspec_kw=dict(width_ratios=[1.6, 1]))
    ax.scatter([0], [0], s=1400, color=sv.C["yellow"], alpha=0.85, zorder=3)
    for b in [4, 7, 11]:
        for kfac, col, ls, lab in [(1, sv.C["blue"], "--", "clocks slowed only"),
                                   (2, sv.C["pink"], "-", "clocks + space stretched (GR)")]:
            path, _ = trace_ray(b, kfac, rs_demo)
            ax.plot(path[:, 0], path[:, 1], color=col, ls=ls, lw=2, label=lab if b == 4 else None)
        ax.axhline(b, color=sv.MUTED, lw=0.6, ls=":")
    ax.set_xlim(-60, 60)
    ax.set_ylim(-6, 14)
    ax.set_aspect("auto")
    ax.set_title("Light passing a heavy region (exaggerated)")
    ax.legend(loc="lower left", fontsize=11)
    ax.grid(False)

    # Sun grazing ray, exact weak-field numbers: α = 2(1+γ)GM/(bc²)
    GM_sun, c, R_sun = 1.32712440018e20, 299792458.0, 6.957e8
    base = 2 * GM_sun / (R_sun * c**2)
    to_arcsec = 180 / np.pi * 3600
    time_only, gr = base * to_arcsec, 2 * base * to_arcsec
    print(f"  B: Sun-grazing deflection — clocks-only lag: {time_only:.3f}″   GR (clocks+space): {gr:.3f}″")
    labels = ["lag only", "GR", "measured"]
    vals = [time_only, gr, gr]
    bx.bar(labels, vals, color=[sv.C["blue"], sv.C["pink"], sv.C["green"]])
    for i, v in enumerate(vals):
        bx.text(i, v + 0.04, f"{v:.2f}″", ha="center", fontsize=13)
    bx.set_ylabel("starlight deflection at the Sun's edge (arcsec)")
    bx.set_title("Lag alone gets half")
    bx.text(1, 2.05, "measured: PPN γ = 1 to ~10⁻⁵ (Cassini)", ha="center", fontsize=10, color=sv.MUTED)
    bx.set_ylim(0, 2.2)
    bx.grid(axis="x", visible=False)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    sv.save(fig, OUT / "light_bending.png")


if __name__ == "__main__":
    sv.apply_style()
    part_a()
    part_b()
