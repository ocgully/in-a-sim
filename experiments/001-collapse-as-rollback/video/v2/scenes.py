"""Episode 001 scenes, rendered in headless Blender.

    Blender -b -P scenes.py -- <shot> [--preview]

Shots
  arena_game       wide: runner reaches cover, then drops (what a gamer experiences)
  arena_shooter    shooter's POV: sees the runner ~150 ms in the past, fires
  arena_runner     runner's over-the-shoulder view: safe behind cover… then eliminated
  arena_server     top-down orthographic "server" view with history-buffer ghosts
  arena_committed  wide: the committed timeline: the runner falls in the open, never reached cover
  lab_stripes      double slit, no record kept: stripes build up
  lab_observed     double slit with a which-path detector: two bands
  lab_delayed      close-up of the screen: later partner results sort old hits into stripes
  racks            keep-every-branch (servers doubling) vs commit-and-clean-up

Frames are written to build/frames/<shot>/f_####.png. Timing constants are the same
as sims/lag_compensation.py (6 m/s sprint, 50 ms shooter latency, 100 ms interpolation,
40 ms victim latency), exported to build/frames/<shot>/meta.json for the compositor.
"""
from __future__ import annotations

import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "shared", "engine"))
import bpy  # noqa: E402
import neon  # noqa: E402

P = neon.PALETTE
BUILD = os.path.join(HERE, "build")

# ---------------------------------------------------------------- netcode timeline
SPEED, X0 = 6.0, -4.0
SHOOTER = (-2.0, -8.0)
WALL_X0, WALL_Y = 0.0, -1.2
OWL_S, INTERP, OWL_V = 0.050, 0.100, 0.040
VIEW_LAG = OWL_S + INTERP
AIM_X = -0.4
T_SEEN = (AIM_X - X0) / SPEED
T_FIRE = T_SEEN + VIEW_LAG
T_RECV = T_FIRE + OWL_S
T_NOTIFY = T_RECV + OWL_V
FALL = 0.22                      # seconds of game time to hit the floor


def x_run(t, t_death):
    return X0 + SPEED * min(t, t_death)


def pose(t, t_death):
    """(location, rotation) of a runner that dies at t_death."""
    x = x_run(t, t_death)
    bob = 0.06 * abs(math.sin(t * 18)) if t < t_death else 0.0
    a = 0.0 if t < t_death else min(1.0, (t - t_death) / FALL) * math.radians(88)
    return (x, 0.0, bob), (0.0, a, 0.0)


def build_arena():
    neon.reset()
    neon.lights()
    neon.grid_floor()
    wall_mat = neon.mat_solid("wall", (0.08, 0.09, 0.12), rough=0.5, metal=0.1)
    edge = neon.mat_glow("wall_edge", P["green"], 4)
    neon.box("cover", (WALL_X0 + 3.0, WALL_Y, 1.25), (6.0, 0.6, 2.5), wall_mat)
    neon.box("cover_edge", (WALL_X0 + 3.0, WALL_Y - 0.31, 2.5), (6.0, 0.04, 0.06), edge)
    neon.box("cover_edge2", (WALL_X0 + 0.01, WALL_Y - 0.31, 1.25), (0.06, 0.04, 2.5), edge)
    # scenery blocks so the space reads as a map
    for i, (x, y, h) in enumerate([(8, 5, 4), (-8, -6, 2), (9, -6, 3), (3, 8, 5), (-6, 10, 2.5)]):
        neon.box(f"block{i}", (x, y, h / 2), (2.5, 2.5, h), wall_mat)
    shooter = neon.avatar("shooter", P["orange"])
    shooter.location = (*SHOOTER, 0)
    shooter.rotation_euler = (0, 0, math.atan2(-SHOOTER[1], AIM_X - SHOOTER[0]))
    gun = neon.box("gun", (SHOOTER[0] + 0.25, SHOOTER[1] + 0.35, 1.35), (0.12, 0.7, 0.12),
                   neon.mat_solid("gunm", (0.05, 0.05, 0.06), metal=0.8))
    gun.rotation_euler = (0, 0, math.atan2(-SHOOTER[1], AIM_X - SHOOTER[0]) - math.pi / 2)
    runner = neon.avatar("runner", P["cyan"])
    seen = neon.avatar("runner_seen", P["cyan"])          # what the shooter's screen draws
    ghosts = [neon.avatar(f"hist{k}", P["cyan"], ghost=True, alpha=0.35 - 0.035 * k) for k in range(1, 9)]
    flash = neon.sphere("muzzle", (SHOOTER[0] + 0.3, SHOOTER[1] + 0.8, 1.4), 0.25, neon.mat_glow("flash", P["yellow"], 40))
    muzzle_to = (AIM_X, 0.0, 1.2)
    d = (muzzle_to[0] - SHOOTER[0], muzzle_to[1] - SHOOTER[1])
    far = (SHOOTER[0] + d[0] * 1.6, SHOOTER[1] + d[1] * 1.6, 1.15)
    tracer = neon.cylinder_between("tracer", (SHOOTER[0] + 0.3, SHOOTER[1] + 0.8, 1.4), far, 0.03,
                                   neon.mat_glow("tracerm", P["yellow"], 25))
    return dict(runner=runner, seen=seen, ghosts=ghosts, flash=flash, tracer=tracer, shooter=shooter)


def animate_arena(o, t0, t1, slowmo, t_death, show_seen=False, show_ghosts=False, t_shot=T_FIRE):
    f0, f1 = 1, neon.frame_of(t1, slowmo, t0)
    tf = lambda f: t0 + (f - 1) / (slowmo * neon.FPS)  # noqa: E731
    neon.key_path(o["runner"], lambda f: pose(tf(f), t_death)[0], f0, f1, rot_fn=lambda f: pose(tf(f), t_death)[1])
    # the shooter's screen: the runner as it was VIEW_LAG ago (never dies on this screen before the shot)
    neon.key_path(o["seen"], lambda f: pose(max(0, tf(f) - VIEW_LAG), 99)[0], f0, f1)
    neon.key_visible(o["seen"], lambda f: show_seen, f0, f1)
    neon.key_visible(o["runner"], lambda f: not show_seen, f0, f1)
    for k, g in enumerate(o["ghosts"], start=1):
        neon.key_path(g, lambda f, k=k: pose(max(0.0, tf(f) - 0.05 * k), t_death)[0], f0, f1)
        neon.key_visible(g, lambda f, k=k: show_ghosts and tf(f) - 0.05 * k > 0, f0, f1)
    neon.key_visible(o["flash"], lambda f: 0 <= tf(f) - t_shot < 0.03, f0, f1)
    neon.key_visible(o["tracer"], lambda f: 0 <= tf(f) - t_shot < 0.05, f0, f1)
    return f0, f1, tf


def meta(shot, **kw):
    d = os.path.join(BUILD, "frames", shot)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "meta.json"), "w") as fh:
        json.dump(kw, fh, indent=1)


# ---------------------------------------------------------------- arena shots
def shot_arena_game(preview):
    o = build_arena()
    t0, t1, s = 0.0, 1.35, 4.0
    f0, f1, tf = animate_arena(o, t0, t1, s, T_NOTIFY)
    cam, _ = neon.camera("cam", (-7.0, 5.0, 3.0), (0.2, -2.8, 0.9), lens=28)
    meta("arena_game", slowmo=s, t0=t0, f_fire=neon.frame_of(T_FIRE, s, t0),
         f_notify=neon.frame_of(T_NOTIFY, s, t0), f_cover=neon.frame_of(-X0 / SPEED + 0.037, s, t0))
    return cam, f0, f1


def shot_arena_committed(preview):
    o = build_arena()
    t0, t1, s = 0.0, 1.35, 4.0
    f0, f1, tf = animate_arena(o, t0, t1, s, T_SEEN, t_shot=T_SEEN - 0.03)
    cam, _ = neon.camera("cam", (-7.0, 5.0, 3.0), (0.2, -2.8, 0.9), lens=28)
    meta("arena_committed", slowmo=s, t0=t0, f_hit=neon.frame_of(T_SEEN, s, t0))
    return cam, f0, f1


def shot_arena_shooter(preview):
    o = build_arena()
    t0, t1, s = 0.25, 0.95, 6.0
    f0, f1, tf = animate_arena(o, t0, t1, s, T_NOTIFY, show_seen=True)
    o["shooter"].hide_render = True          # first-person: don't render your own body
    cam, tgt = neon.camera("cam", (SHOOTER[0] - 0.25, SHOOTER[1] - 0.4, 1.75), (0, 0, 1.2), lens=55)
    neon.key_path(tgt, lambda f: (pose(max(0, min(tf(f), T_FIRE) - VIEW_LAG), 99)[0][0] + 0.25, 0, 1.3), f0, f1)
    meta("arena_shooter", slowmo=s, t0=t0, f_fire=neon.frame_of(T_FIRE, s, t0))
    return cam, f0, f1


def shot_arena_runner(preview):
    o = build_arena()
    t0, t1, s = 0.3, 1.1, 6.0
    f0, f1, tf = animate_arena(o, t0, t1, s, T_NOTIFY)
    cam, tgt = neon.camera("cam", (0, 0, 0), (0, 0, 0), lens=30)
    neon.key_path(cam, lambda f: (x_run(tf(f), T_NOTIFY) - 3.8, 2.3, 2.6), f0, f1)
    neon.key_path(tgt, lambda f: (x_run(tf(f), T_NOTIFY) + 2.5, -0.6, 1.1), f0, f1)
    meta("arena_runner", slowmo=s, t0=t0, f_cover=neon.frame_of(-X0 / SPEED + 0.037, s, t0),
         f_notify=neon.frame_of(T_NOTIFY, s, t0))
    return cam, f0, f1


def shot_arena_server(preview):
    o = build_arena()
    t0, t1, s = 0.0, 1.05, 6.0
    f0, f1, tf = animate_arena(o, t0, t1, s, T_NOTIFY, show_ghosts=True)
    bpy.ops.object.camera_add(location=(-1.0, -3.2, 30))
    cam = bpy.context.object
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 20.0
    cam.rotation_euler = (0, 0, 0)
    meta("arena_server", slowmo=s, t0=t0, cx=-1.0, cy=-3.2, ortho=20.0,
         f_seen=neon.frame_of(T_SEEN, s, t0), f_fire=neon.frame_of(T_FIRE, s, t0),
         f_recv=neon.frame_of(T_RECV, s, t0), f_notify=neon.frame_of(T_NOTIFY, s, t0),
         hit_xy=[AIM_X, 0.0], shooter_xy=list(SHOOTER))
    return cam, f0, f1


# ---------------------------------------------------------------- lab shots
def build_lab(mode):
    neon.reset()
    neon.lights(energy=2.0)
    neon.grid_floor(color=(0.25, 0.1, 0.45), strength=0.8)
    sched = json.load(open(os.path.join(BUILD, "tex", "schedule.json")))
    metal = neon.mat_solid("barrier", (0.1, 0.1, 0.13), rough=0.4, metal=0.6)
    # barrier with two slits at y = ±0.5 (width 0.25)
    for name, y0, y1 in [("b_left", -4, -0.625), ("b_mid", -0.375, 0.375), ("b_right", 0.625, 4)]:
        neon.box(name, (0, (y0 + y1) / 2, 1.25), (0.2, y1 - y0, 2.5), metal)
    edge = neon.mat_glow("slitglow", P["purple"], 6)
    for y in (-0.5, 0.5):
        neon.box(f"slit{y}", (-0.11, y, 2.52), (0.02, 0.25, 0.04), edge)
    # gun
    neon.box("gun_body", (-9.3, 0, 1.25), (1.4, 0.6, 0.6), metal)
    neon.box("gun_ring", (-8.55, 0, 1.25), (0.1, 0.7, 0.7), neon.mat_glow("gunring", P["cyan"], 6))
    # screen: plane facing -X showing the texture sequence
    key = "delayed" if mode == "delayed" else mode
    first = os.path.join(BUILD, "tex", key, "0001.png")
    bpy.ops.mesh.primitive_plane_add(size=1, location=(9, 0, 1.25), rotation=(math.radians(90), 0, math.radians(90)))
    scr = bpy.context.object
    scr.scale = (8, 2.5, 1)
    neon.assign(scr, neon.mat_image_sequence("screen", first, sched[key]["frames"], strength=1.6))
    neon.box("screen_frame", (9.08, 0, 1.25), (0.1, 8.3, 2.8), metal)
    if mode == "observed":
        neon.box("det_body", (0.5, 0, 2.95), (0.5, 1.6, 0.35), metal)
        lens = neon.sphere("det_lens", (0.2, 0, 2.9), 0.14, neon.mat_glow("detlens", P["red"], 18))
    return sched


def particles(sched, mode, n_frames):
    s = sched[mode]
    every, flight, n = s["launch_every"], s["flight"], s["n_slow"]
    half = flight // 2
    glow = neon.mat_glow("pglow", P["white"], 30)
    faint = neon.mat_glow("pfaint", P["cyan"], 8)
    for k in range(n):
        launch = 1 + k * every
        p = neon.sphere(f"p{k}", (-8.5, 0, 1.25), 0.09, glow, seg=12)
        y_end, z_end = s["y"][k], s["z"][k]
        def main_pos(f, launch=launch, y_end=y_end, z_end=z_end):
            u = (f - launch) / half
            if u <= 1:
                return (-8.5 + 8.5 * u, 0, 1.25)
            if mode == "observed":
                slit = 0.5 if y_end > 0 else -0.5
                v = min(1.0, u - 1)
                return (9 * v, slit + (y_end - slit) * v, 1.25 + (z_end - 1.25) * v)
            return (0, 0, 1.25)
        neon.key_path(p, main_pos, launch, min(n_frames, launch + flight))
        stop = flight if mode == "observed" else half
        neon.key_visible(p, lambda f, launch=launch, stop=stop: launch <= f < launch + stop, 1, n_frames)
        if mode == "stripes":      # no record kept: the particle continues through BOTH slits, faintly
            for side in (-0.5, 0.5):
                q = neon.sphere(f"q{k}{side}", (0, side, 1.25), 0.07, faint, seg=10)
                neon.key_path(q, lambda f, launch=launch, side=side, y_end=y_end, z_end=z_end:
                              (9 * min(1, (f - launch - half) / half), side + (y_end - side) * min(1, (f - launch - half) / half),
                               1.25 + (z_end - 1.25) * min(1, (f - launch - half) / half)),
                              launch + half, min(n_frames, launch + flight))
                neon.key_visible(q, lambda f, launch=launch: launch + half <= f < launch + flight, 1, n_frames)
    return n


def shot_lab(mode, preview):
    sched = build_lab(mode)
    n_frames = sched[mode]["frames"]
    particles(sched, mode, n_frames)
    if mode == "observed":
        lens = bpy.data.objects["det_lens"]
        s = sched[mode]
        half = s["flight"] // 2
        hits = {1 + k * s["launch_every"] + half + j for k in range(s["n_slow"]) for j in range(3)}
        neon.key_visible(lens, lambda f: f in hits or f > 1 + s["n_slow"] * s["launch_every"] + half, 1, n_frames)
    cam, tgt = neon.camera("cam", (-5.0, -13.0, 5.5), (-3.0, 0, 1.1), lens=26)
    neon.key_path(cam, lambda f: (-5.0 + 7.0 * f / n_frames, -13.0 + 4.0 * f / n_frames, 5.5 - 1.5 * f / n_frames), 1, n_frames)
    neon.key_path(tgt, lambda f: (-3.0 + 9.0 * min(1, 1.6 * f / n_frames) ** 1.3, 0, 1.1), 1, n_frames)
    meta(f"lab_{mode}", frames=n_frames)
    return cam, 1, n_frames


def shot_lab_delayed(preview):
    sched = build_lab("delayed")
    n = sched["delayed"]["frames"]
    cam, _ = neon.camera("cam", (4.0, -2.2, 1.5), (9, 0, 1.25), lens=30)
    meta("lab_delayed", frames=n, phases=sched["delayed"]["phases"])
    return cam, 1, n


# ---------------------------------------------------------------- racks
def shot_racks(preview):
    neon.reset()
    neon.lights(energy=2.0)
    neon.grid_floor(color=(0.05, 0.3, 0.2), strength=0.7)
    body = neon.mat_solid("rack", (0.06, 0.06, 0.08), rough=0.3, metal=0.7)
    led_g = neon.mat_glow("ledg", P["green"], 6)
    led_p = neon.mat_glow("ledp", P["pink"], 6)
    led_r = neon.mat_glow("ledr", P["red"], 20)
    step, steps = 24, 10                                # doubling every 24 frames: 1 → 512
    n_frames = step * steps + 60
    # template rack
    base = neon.box("rack_t", (0, 0, 1.1), (0.8, 0.8, 2.2), body)
    led = neon.box("led_t", (0.41, 0, 1.1), (0.02, 0.5, 1.6), led_g)
    def rack_at(name, loc, led_mat):
        b = base.copy(); b.name = name; b.location = (loc[0], loc[1], 1.1)
        bpy.context.collection.objects.link(b)
        l = led.copy(); l.data = led.data.copy(); l.name = name + "_led"; l.location = (loc[0] + 0.41, loc[1], 1.1)
        l.data.materials.clear(); l.data.materials.append(led_mat)
        bpy.context.collection.objects.link(l)
        return b, l
    base.hide_render = led.hide_render = True
    # LEFT: keep every branch, grid growing away from the camera (-x, +y)
    for i in range(512):
        gx, gy = i % 32, i // 32
        b, l = rack_at(f"L{i}", (-2.0 - gx * 1.1, -3 + gy * 1.1), led_g)
        appear = 1 + step * max(0, math.ceil(math.log2(i + 1)))
        for o in (b, l):
            neon.key_visible(o, lambda f, appear=appear: f >= appear, 1, n_frames)
    # RIGHT: commit + clean up: one rack; each step a branch spawns then is deleted
    keep_b, keep_l = rack_at("R0", (3.0, -2.0), led_p)
    for s_ in range(1, steps):
        b, l = rack_at(f"Rb{s_}", (4.2, -2.0), led_p)
        t_on, t_off = 1 + step * s_, 1 + step * s_ + 14
        for o in (b, l):
            neon.key_visible(o, lambda f, a=t_on, z=t_off: a <= f < z, 1, n_frames)
        x_ = neon.box(f"Rx{s_}", (4.2, -2.0, 1.1), (0.9, 0.9, 2.3), led_r)
        neon.key_visible(x_, lambda f, a=t_off: a <= f < a + 3, 1, n_frames)
    cam, tgt = neon.camera("cam", (6, -12, 5), (-2, 0, 1), lens=28)
    neon.key_path(cam, lambda f: (6 + 4 * f / n_frames, -12 - 14 * (f / n_frames) ** 1.5, 5 + 16 * (f / n_frames) ** 1.5), 1, n_frames)
    neon.key_path(tgt, lambda f: (-2 - 7 * (f / n_frames) ** 1.5, 3 * (f / n_frames), 1), 1, n_frames)
    meta("racks", frames=n_frames, step=step, steps=steps)
    return cam, 1, n_frames


SHOTS = {
    "arena_game": shot_arena_game,
    "arena_committed": shot_arena_committed,
    "arena_shooter": shot_arena_shooter,
    "arena_runner": shot_arena_runner,
    "arena_server": shot_arena_server,
    "lab_stripes": lambda p: shot_lab("stripes", p),
    "lab_observed": lambda p: shot_lab("observed", p),
    "lab_delayed": shot_lab_delayed,
    "racks": shot_racks,
}

if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    name = argv[0]
    preview = "--preview" in argv
    cam, f0, f1 = SHOTS[name](preview)
    if preview:                      # render 3 stills only
        mid = (f0 + f1) // 2
        for f in (f0, mid, f1):
            neon.render(cam, os.path.join(BUILD, "preview", name, str(f)), f, f)
    else:
        neon.render(cam, os.path.join(BUILD, "frames", name), f0, f1)
