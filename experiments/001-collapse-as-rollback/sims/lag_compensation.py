"""Sim 1 — Lag compensation ("favour the shooter") as a toy model of retroactive truth.

A target sprints toward cover. A shooter with a laggy connection fires at the
*old* image of the target they see on their screen. The server receives the
shot late, REWINDS the world to the moment the shooter was looking at, tests
the hit against that historical snapshot, and commits the result. The victim
then learns they died — after they had already reached cover on their own
screen.

Nothing here is quantum. The point is structural: an authoritative server
resolving an event against a past snapshot, then broadcasting it as the one
truth, regardless of what any single observer experienced.

Outputs:
  output/lagcomp_spacetime.png   space-time diagram (time up, space across)
  output/lagcomp_behind_cover.png  % of kills that land "behind cover" vs ping
  output/lagcomp_three_views.mp4 slow-motion shooter / server / victim views
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "lib"))
import simviz as sv  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import animation  # noqa: E402

OUT = sv.out_dir(__file__)


@dataclass
class Netcode:
    speed: float = 6.0            # m/s; roughly a Source-engine sprint (~250 u/s)
    start_x: float = -1.0         # m; cover begins at x = 0
    shooter_owl: float = 0.050    # one-way latency server<->shooter (s)
    victim_owl: float = 0.040     # one-way latency server<->victim (s)
    interp: float = 0.100         # client interpolation buffer (s); Source default cl_interp 0.1
    aim_x: float = -0.10          # where the shooter sees the target when they fire (m)

    def x(self, t):
        """Authoritative (server) position of the target."""
        return self.start_x + self.speed * np.asarray(t)

    @property
    def view_lag(self) -> float:
        """How old the target image on the shooter's screen is."""
        return self.shooter_owl + self.interp

    def events(self) -> dict[str, float]:
        t_cover = -self.start_x / self.speed                     # target reaches cover (truth)
        t_seen = (self.aim_x - self.start_x) / self.speed        # state the shooter is looking at
        t_fire = t_seen + self.view_lag                          # trigger pulled
        t_recv = t_fire + self.shooter_owl                       # server gets the shot
        t_notify = t_recv + self.victim_owl                      # victim learns they are dead
        return dict(t_cover=t_cover, t_seen=t_seen, t_fire=t_fire, t_recv=t_recv, t_notify=t_notify)


def spacetime_diagram(nc: Netcode) -> None:
    ev = nc.events()
    t = np.linspace(0, 0.5, 400)
    fig, ax = plt.subplots(figsize=sv.WIDE)
    ax.axvspan(0, 3, color=sv.C["green"], alpha=0.12)
    ax.text(0.08, 0.475, "BEHIND COVER", color=sv.C["green"], fontsize=12, weight="bold")

    ax.plot(nc.x(t), t, color=sv.C["blue"], lw=3, label="Target — server truth / victim's own screen")
    ax.plot(nc.x(t - nc.view_lag), t, color=sv.C["orange"], lw=2.5, ls="--",
            label=f"Target as drawn on shooter's screen ({nc.view_lag*1000:.0f} ms old)")

    xs = nc.x(ev["t_seen"])
    ax.scatter([xs], [ev["t_fire"]], s=160, color=sv.C["orange"], zorder=5)
    ax.annotate("① trigger pulled\n(shooter sees target exposed)", (xs, ev["t_fire"]),
                xytext=(-2.4, ev["t_fire"] + 0.02), arrowprops=dict(arrowstyle="->", color=sv.C["orange"]),
                color=sv.C["orange"])

    ax.scatter([xs], [ev["t_recv"]], s=160, color=sv.C["pink"], zorder=5, marker="s")
    ax.annotate("", xy=(xs, ev["t_seen"]), xytext=(xs, ev["t_recv"]),
                arrowprops=dict(arrowstyle="-|>", color=sv.C["pink"], lw=2.5, ls=":"))
    ax.scatter([xs], [ev["t_seen"]], s=220, color=sv.C["pink"], marker="X", zorder=6)
    ax.annotate("② server receives shot,\nREWINDS world to the shooter's snapshot\n③ hit test vs the past → HIT (committed)",
                (xs, ev["t_seen"]), xytext=(0.2, 0.02),
                arrowprops=dict(arrowstyle="->", color=sv.C["pink"]), color=sv.C["pink"])

    xv = nc.x(ev["t_notify"])
    ax.scatter([xv], [ev["t_notify"]], s=220, color=sv.C["red"], marker="*", zorder=6)
    ax.annotate(f"④ victim told they are dead —\n{(ev['t_notify']-ev['t_cover'])*1000:.0f} ms after reaching cover,\n{xv:.2f} m behind the wall",
                (xv, ev["t_notify"]), xytext=(0.9, ev["t_notify"] - 0.13),
                arrowprops=dict(arrowstyle="->", color=sv.C["red"]), color=sv.C["red"])

    ax.axhline(ev["t_cover"], color=sv.C["green"], lw=1, ls=":")
    ax.set_xlim(-2.5, 3)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel("position (m) — cover starts at 0")
    ax.set_ylabel("server time (s)  ↑")
    ax.set_title("Lag compensation: the past is re-decided, then becomes the only truth")
    ax.legend(loc="upper left", fontsize=11)
    sv.save(fig, OUT / "lagcomp_spacetime.png")


def behind_cover_sweep() -> None:
    """Monte Carlo: target crosses an open gap; shooter kills at a uniformly random
    moment of what *they see*. What fraction of deaths does the victim experience
    as 'I was already safe'?"""
    rng = np.random.default_rng(7)
    gap_times = [0.25, 0.5, 1.0]  # seconds the target is exposed while crossing
    pings = np.linspace(0, 0.300, 61)  # shooter RTT
    fig, ax = plt.subplots(figsize=sv.WIDE)
    for gap, col in zip(gap_times, [sv.C["red"], sv.C["orange"], sv.C["yellow"]]):
        frac = []
        for rtt in pings:
            nc = Netcode(shooter_owl=rtt / 2)
            t_seen = rng.uniform(0, gap, 20000)
            t_notify = t_seen + nc.view_lag + nc.shooter_owl + nc.victim_owl
            frac.append(np.mean(t_notify > gap) * 100)
        ax.plot(pings * 1000, frac, lw=3, color=col, label=f"exposed for {gap*1000:.0f} ms")
        at = {ms: frac[int(np.argmin(np.abs(pings * 1000 - ms)))] for ms in (30, 60, 100, 150)}
        print(f"  exposed {gap*1000:4.0f} ms: behind-cover deaths at RTT 30/60/100/150 ms = "
              + " / ".join(f"{v:.0f}%" for v in at.values()))
    ax.set_xlabel("shooter ping / RTT (ms)")
    ax.set_ylabel("% of kills the victim experiences\nas happening behind cover")
    ax.set_title("With rewind, 'already safe' deaths are not a bug — they are the design")
    ax.set_ylim(0, 100)
    ax.legend()
    sv.save(fig, OUT / "lagcomp_behind_cover.png")


def three_views_animation(nc: Netcode, slowmo: float = 12.0, fps: int = 30) -> None:
    ev = nc.events()
    T = 0.55
    n_frames = int(T * slowmo * fps)
    ts = np.linspace(0, T, n_frames)

    fig, axes = plt.subplots(3, 1, figsize=sv.WIDE, sharex=True)
    titles = ["SHOOTER'S SCREEN  (sees the past)", "SERVER  (authoritative truth + history buffer)",
              "VICTIM'S SCREEN  (sees self in the present)"]
    dots, ghosts, texts = [], [], []
    for ax, title in zip(axes, titles):
        ax.set_xlim(-1.2, 2.5)
        ax.set_ylim(-1, 1)
        ax.set_yticks([])
        ax.grid(False)
        ax.axvspan(0, 2.5, color=sv.C["green"], alpha=0.15)
        ax.text(1.9, 0.55, "COVER", color=sv.C["green"], weight="bold")
        ax.set_title(title, fontsize=13, loc="left")
        dots.append(ax.scatter([], [], s=500, color=sv.C["blue"], zorder=5))
        ghosts.append(ax.scatter([], [], s=500, facecolors="none", edgecolors=sv.C["pink"], lw=3, zorder=4))
        texts.append(ax.text(-1.15, -0.8, "", fontsize=13, weight="bold"))
    axes[-1].set_xlabel("position (m)")
    clock = fig.text(0.5, 0.955, "", ha="center", fontsize=15, color=sv.C["yellow"], weight="bold")
    xs = nc.x(ev["t_seen"])

    def frame(i):
        t = ts[i]
        clock.set_text(f"server time {t*1000:6.0f} ms   ·   {slowmo:.0f}× slow motion")
        # shooter sees the past
        dots[0].set_offsets([[nc.x(t - nc.view_lag), 0]])
        if t >= ev["t_fire"]:
            texts[0].set_text("① BANG — crosshair was on target")
            texts[0].set_color(sv.C["orange"])
        # server
        dots[1].set_offsets([[nc.x(t), 0]])
        if t >= ev["t_recv"]:
            ghosts[1].set_offsets([[xs, 0]])
            texts[1].set_text(f"② shot arrives → rewind {(ev['t_recv']-ev['t_seen'])*1000:.0f} ms → ③ HIT vs past snapshot → committed")
            texts[1].set_color(sv.C["pink"])
        else:
            ghosts[1].set_offsets(np.empty((0, 2)))
        # victim sees themself in the present
        alive = t < ev["t_notify"]
        dots[2].set_offsets([[nc.x(t) if alive else nc.x(ev["t_notify"]), 0]])
        dots[2].set_color(sv.C["blue"] if alive else sv.C["red"])
        if t >= ev["t_cover"] and alive:
            texts[2].set_text("safe behind cover …")
            texts[2].set_color(sv.C["green"])
        if not alive:
            texts[2].set_text("④ ELIMINATED — history was decided without you")
            texts[2].set_color(sv.C["red"])
        return dots + ghosts + texts + [clock]

    anim = animation.FuncAnimation(fig, frame, frames=n_frames, blit=False)
    sv.save_anim(anim, OUT / "lagcomp_three_views.mp4", fps=fps)


if __name__ == "__main__":
    sv.apply_style()
    nc = Netcode()
    ev = nc.events()
    print("Lag compensation timeline (s):", {k: round(v, 3) for k, v in ev.items()})
    print(f"  victim notified {(ev['t_notify']-ev['t_cover'])*1000:.0f} ms after reaching cover, "
          f"{nc.x(ev['t_notify']):.2f} m behind it")
    spacetime_diagram(nc)
    behind_cover_sweep()
    three_views_animation(nc)
