"""Episode 002 scenes, rendered in headless Blender.

    Blender -b -P scenes.py -- <shot> [--preview]

Shots
  eve_battle     fleet battle round a station, everything in slow motion (MMO time dilation)
  tower_clocks   same avatar on a tower vs on the ground; the lower clock ticks slower
  tiles_ripple   floor of clock-tiles; a planet lands and the slowdown ripples outward
  march          a marching line crosses the tile field and swings toward the planet (why things fall)
  light_race     two light pulses race; the one through the gravity well arrives late (Shapiro delay)
  eclipse        1919: starlight grazing the Sun: the real path vs a "lag only" ghost path
  drop_test      supercomputer vs steel ball of equal mass, dropped together
  sync_space     tiles near the planet subdivide (more space) and the sync wave slows (slower tick)
"""
from __future__ import annotations

import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "shared", "engine"))
import bpy  # noqa: E402
import neon  # noqa: E402

P = neon.PALETTE
BUILD = os.path.join(HERE, "build")


def meta(shot, **kw):
    d = os.path.join(BUILD, "frames", shot)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "meta.json"), "w") as fh:
        json.dump(kw, fh, indent=1)


def sched():
    return json.load(open(os.path.join(BUILD, "tex", "schedule.json")))


def tile_floor(name, size=48):
    s = sched()
    bpy.ops.mesh.primitive_plane_add(size=size, location=(0, 0, 0))
    fl = bpy.context.object
    neon.assign(fl, neon.mat_image_sequence("floor_" + name, os.path.join(BUILD, "tex", name, "0001.png"),
                                            s[name]["frames"], strength=1.3))
    return fl, s[name]["frames"]


def planet(loc=(0, 0, 1.6), r=1.6):
    p = neon.sphere("planet", loc, r, neon._principled("planetm", (0.15, 0.05, 0.25), 0.4, 0.2,
                                                        emit=P["purple"], emit_strength=1.2), seg=48)
    ring = neon.sphere("planet_glow", loc, r * 1.12, neon.mat_ghost("pglowm", P["pink"], alpha=0.15, strength=3), seg=32)
    return p, ring


def clock(name, loc, color):
    """Floating clock face (ring + rotating hand). Returns the pivot empty to rotate."""
    bpy.ops.mesh.primitive_torus_add(major_radius=0.5, minor_radius=0.05, location=loc, rotation=(math.radians(90), 0, 0))
    neon.assign(bpy.context.object, neon.mat_glow(name + "_ring", color, 6))
    bpy.ops.object.empty_add(location=loc)
    piv = bpy.context.object
    piv.name = name + "_pivot"
    hand = neon.box(name + "_hand", (0, 0, 0), (0.06, 0.02, 0.42), neon.mat_glow(name + "_handm", P["white"], 8))
    hand.parent = piv
    hand.location = (0, -0.03, 0.2)
    return piv


# ------------------------------------------------------------------ shots
def shot_eve_battle(preview):
    neon.reset()
    random.seed(2011)
    n = 240
    # starfield
    star = neon.mat_glow("star", P["white"], 12)
    for i in range(260):
        th, ph = random.uniform(0, 2 * math.pi), random.uniform(-1, 1)
        r = 90
        neon.sphere(f"s{i}", (r * math.cos(th) * math.sqrt(1 - ph**2), r * math.sin(th) * math.sqrt(1 - ph**2), r * ph),
                    random.uniform(0.08, 0.25), star, seg=6)
    # station
    metal = neon.mat_solid("stat", (0.12, 0.13, 0.16), rough=0.3, metal=0.8)
    bpy.ops.mesh.primitive_torus_add(major_radius=3.2, minor_radius=0.45, location=(0, 0, 0))
    neon.assign(bpy.context.object, metal)
    bpy.ops.mesh.primitive_torus_add(major_radius=3.2, minor_radius=0.08, location=(0, 0, 0.5))
    neon.assign(bpy.context.object, neon.mat_glow("statglow", P["yellow"], 6))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.9, depth=4, location=(0, 0, 0))
    neon.assign(bpy.context.object, metal)
    # ships on slow orbits
    teams = [neon.mat_glow("teamA", P["orange"], 8), neon.mat_glow("teamB", P["cyan"], 8)]
    ships = []
    for i in range(130):
        team = i % 2
        bpy.ops.mesh.primitive_cone_add(radius1=0.18, depth=0.7, vertices=8)
        sh = neon.assign(bpy.context.object, teams[team])
        R = random.uniform(6, 16)
        inc = random.uniform(-0.5, 0.5)
        w = random.uniform(0.05, 0.12) * (1 if team else -1)
        ph0 = random.uniform(0, 2 * math.pi)
        def pos(f, R=R, inc=inc, w=w, ph0=ph0):
            a = ph0 + w * f / 30 * 2 * math.pi * 0.15   # already "10% speed"
            return (R * math.cos(a), R * math.sin(a) * math.cos(inc), R * math.sin(a) * math.sin(inc))
        def rot(f, R=R, inc=inc, w=w, ph0=ph0):
            a = ph0 + w * f / 30 * 2 * math.pi * 0.15
            return (math.pi / 2, 0, a + (math.pi if w < 0 else 0))
        neon.key_path(sh, pos, 1, n, rot_fn=rot)
        ships.append((sh, pos))
    # lasers between random ship pairs, flickering
    lz = [neon.mat_glow("lzA", P["orange"], 30), neon.mat_glow("lzB", P["cyan"], 30)]
    for k in range(16):
        a, b = random.sample(range(len(ships)), 2)
        f0 = random.randint(1, n - 40)
        pa, pb = ships[a][1](f0), ships[b][1](f0)
        beam = neon.cylinder_between(f"laser{k}", pa, pb, 0.03, lz[k % 2])
        neon.key_visible(beam, lambda f, f0=f0: f0 <= f < f0 + 18, 1, n)
    cam, tgt = neon.camera("cam", (20, -22, 9), (0, 0, 0), lens=30)
    neon.key_path(cam, lambda f: (26 * math.cos(-0.85 + 0.35 * f / n), 26 * math.sin(-0.85 + 0.35 * f / n), 9 - 2 * f / n), 1, n)
    meta("eve_battle", frames=n)
    return cam, 1, n


def shot_tower_clocks(preview):
    neon.reset()
    neon.lights(energy=2.0)
    neon.grid_floor()
    n = 210
    wall = neon.mat_solid("tower", (0.08, 0.09, 0.12), rough=0.5, metal=0.2)
    neon.box("tower", (4, 0, 4), (2.4, 2.4, 8), wall)
    neon.box("tower_edge", (4, -1.21, 8), (2.4, 0.04, 0.08), neon.mat_glow("te", P["green"], 5))
    top = neon.avatar("top", P["cyan"])
    top.location = (4, 0, 8)
    top.rotation_euler = (0, 0, -math.pi / 2)
    low = neon.avatar("low", P["cyan"])
    low.location = (-3, 0, 0)
    low.rotation_euler = (0, 0, -math.pi / 2)
    c_top = clock("ctop", (4, 0, 10.9), P["cyan"])
    c_low = clock("clow", (-3, 0, 2.9), P["purple"])
    for piv, rate in ((c_top, 1.0), (c_low, 0.62)):
        neon.key_path(piv, lambda f, piv=piv: tuple(piv.location), 1, n,
                      rot_fn=lambda f, rate=rate: (0, rate * f / 30 * 2 * math.pi * 0.5, 0))
    cam, _ = neon.camera("cam", (0.5, -24, 6.5), (0.5, 0, 5.6), lens=30)
    meta("tower_clocks", frames=n)
    return cam, 1, n


def shot_tiles_ripple(preview):
    neon.reset()
    neon.lights(energy=1.0)
    _, n = tile_floor("ripple")
    p, g = planet()
    for o in (p, g):
        neon.key_path(o, lambda f: (0, 0, 1.6 + max(0, 30 - f) * 0.5), 1, n)
    cam, _ = neon.camera("cam", (0, -30, 22), (0, 0, 0), lens=30)
    neon.key_path(cam, lambda f: (30 * math.sin(0.25 * f / n), -30 * math.cos(0.25 * f / n), 22 - 3 * f / n), 1, n)
    meta("tiles_ripple", frames=n, land=30)
    return cam, 1, n


def rate_at(x, y, s):
    d = math.hypot(x, y)
    fdef = s["field"]
    return 1 - fdef["depth"] * fdef["soft"] / math.sqrt(d * d + fdef["soft"] ** 2)


def shot_march(preview):
    neon.reset()
    neon.lights(energy=1.0)
    _, n = tile_floor("steady")
    planet()
    s = sched()
    k, gap, v0, gain = 7, 1.15, 3.2, 3.0
    width = (k - 1) * gap
    # tank-tread model: centre moves at local rate, heading turns toward the slower side
    cx, cy, th = -21.0, -7.5, 0.0
    states = []
    for f in range(1, n + 1):
        states.append((cx, cy, th))
        nx, ny = -math.sin(th), math.cos(th)
        rl = rate_at(cx + nx * width / 2, cy + ny * width / 2, s)
        rr = rate_at(cx - nx * width / 2, cy - ny * width / 2, s)
        rc = rate_at(cx, cy, s)
        dt = 1 / 30
        th += gain * v0 * (rr - rl) / width * dt
        cx += v0 * rc * math.cos(th) * dt
        cy += v0 * rc * math.sin(th) * dt
    bodies = [neon.avatar(f"m{i}", P["cyan"] if i != k // 2 else P["yellow"]) for i in range(k)]
    for i, b in enumerate(bodies):
        off = (i - (k - 1) / 2) * gap
        def pos(f, off=off):
            x, y, t = states[f - 1]
            return (x - math.sin(t) * off, y + math.cos(t) * off, 0.05 * abs(math.sin(f * 0.5 + off)))
        neon.key_path(b, pos, 1, n, rot_fn=lambda f: (0, 0, states[f - 1][2]))
    # breadcrumb trail of the centre
    crumb = neon.mat_glow("crumb", P["yellow"], 10)
    for j in range(0, n, 10):
        x, y, _ = states[j]
        c = neon.sphere(f"crumb{j}", (x, y, 0.06), 0.09, crumb, seg=8)
        neon.key_visible(c, lambda f, j=j: f > j + 1, 1, n)
    cam, tgt = neon.camera("cam", (-8, -30, 20), (-4, -2, 0), lens=30)
    meta("march", frames=n, turn_deg=math.degrees(states[-1][2]))
    return cam, 1, n


def well_z(x, y, W=6.0, S=3.4):
    return -W / (1 + (x * x + y * y) / (S * S))


def shot_light_race(preview):
    neon.reset()
    neon.lights(energy=1.0)
    n = 300
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=110, y_subdivisions=110, size=44, location=(0, 0, 0))
    g = bpy.context.object
    for v in g.data.vertices:
        v.co.z = well_z(v.co.x, v.co.y)
    mod = g.modifiers.new("wire", "WIREFRAME")
    mod.thickness = 0.035
    neon.assign(g, neon.mat_glow("wellgrid", (0.1, 0.4, 0.9), 1.6))
    planet(loc=(0, 0, -4.4), r=1.3)
    # race: A through the well (y=0), B far from it (y=15)
    W = 6.0
    v0 = 36 / 170                                     # B crosses 36 m in ~170 frames
    lanes = {"A": 0.0, "B": 15.0}
    track = {}
    for name, y in lanes.items():
        x, pts = -18.0, []
        for f in range(1, n + 1):
            pts.append((x, y, well_z(x, y) + 0.35))
            if x < 18:
                depth = abs(well_z(x, y)) / W
                slope = (well_z(x + 0.01, y) - well_z(x - 0.01, y)) / 0.02
                local = v0 / (1 + 0.5 * depth)        # slower ticks (time half)
                x += local / math.sqrt(1 + slope * slope)   # longer path over the dip (space half)
        track[name] = pts
    arrive = {k: next(i + 1 for i, p in enumerate(v) if p[0] >= 18) for k, v in track.items()}
    for name, col in (("A", P["yellow"]), ("B", P["white"])):
        head = neon.sphere("pulse" + name, track[name][0], 0.28, neon.mat_glow("pm" + name, col, 40), seg=16)
        neon.key_path(head, lambda f, name=name: track[name][f - 1], 1, n)
        for t in range(1, 14):
            tr = neon.sphere(f"trail{name}{t}", track[name][0], 0.2 * (1 - t / 16),
                             neon.mat_glow(f"tm{name}{t}", col, 14 * (1 - t / 15)), seg=8)
            neon.key_path(tr, lambda f, name=name, t=t: track[name][max(0, f - 1 - 2 * t)], 1, n)
        # start/finish gates
        for gx, gcol in ((-18, P["cyan"]), (18, P["green"])):
            y = lanes[name]
            neon.box(f"gate{name}{gx}", (gx, y, well_z(gx, y) + 1.2), (0.12, 2.2, 2.4), neon.mat_ghost(f"gm{name}{gx}", gcol, alpha=0.25, strength=3))
    cam, tgt = neon.camera("cam", (-4, -26, 9), (0, 6, -2.5), lens=26)
    neon.key_path(cam, lambda f: (-4 + 6 * f / n, -26 + 2 * f / n, 9 - 1.5 * f / n), 1, n)
    meta("light_race", frames=n, arrive_A=arrive["A"], arrive_B=arrive["B"])
    return cam, 1, n


def shot_eclipse(preview):
    neon.reset()
    random.seed(1919)
    n = 240
    star = neon.mat_glow("star", P["white"], 10)
    for i in range(160):
        neon.sphere(f"s{i}", (random.uniform(-60, 60), random.uniform(20, 60), random.uniform(-30, 30)),
                    random.uniform(0.06, 0.18), star, seg=6)
    neon.sphere("sun", (0, 0, 0), 2.0, neon.mat_glow("sunm", (1.0, 0.75, 0.3), 9), seg=48)
    neon.sphere("corona", (0, 0, 0), 2.6, neon.mat_ghost("corm", P["yellow"], alpha=0.12, strength=3), seg=32)
    neon.sphere("earth", (16, 0, 0), 0.55, neon._principled("earthm", (0.05, 0.2, 0.6), 0.5, 0, emit=P["cyan"], emit_strength=1.5), seg=32)
    neon.sphere("far_star", (-26, 0, 2.4), 0.35, neon.mat_glow("fstar", P["white"], 30), seg=16)
    b = 2.4
    a_real = 2 * b / (16 + math.sqrt(256 + b * b))
    y_real = lambda x: b - (a_real / 2) * (x + math.sqrt(x * x + b * b))      # noqa: E731
    y_half = lambda x: b - (a_real / 4) * (x + math.sqrt(x * x + b * b))      # noqa: E731
    xs = [-26 + 42 * i / 90 for i in range(91)]
    real_m, ghost_m = neon.mat_glow("beam", P["yellow"], 20), neon.mat_ghost("ghost", P["cyan"], alpha=0.5, strength=5)
    for i, x in enumerate(xs):
        f_on = 20 + int(i * 1.6)
        d1 = neon.sphere(f"r{i}", (x, 0, y_real(x)), 0.09, real_m, seg=8)
        neon.key_visible(d1, lambda f, f_on=f_on: f >= f_on, 1, n)
        if i % 2 == 0:
            d2 = neon.sphere(f"g{i}", (x, -0.02, y_half(x)), 0.07, ghost_m, seg=8)
            neon.key_visible(d2, lambda f, f_on=f_on: f >= f_on + 30, 1, n)
    cam, _ = neon.camera("cam", (-5, -36, 1.5), (-5, 0, 0.8), lens=26)
    meta("eclipse", frames=n, ghost_miss=y_half(16), real_hit=y_real(16))
    return cam, 1, n


def shot_drop_test(preview):
    neon.reset()
    neon.lights(energy=2.0)
    neon.grid_floor()
    n = 150
    g, h0, f_rel = 6.0, 7.0, 40
    z = lambda f: h0 - 0.5 * g * max(0, (f - f_rel) / 30) ** 2               # noqa: E731
    body = neon.mat_solid("rackm", (0.06, 0.06, 0.08), rough=0.3, metal=0.7)
    rack = neon.box("rack", (-2.2, 0, 0), (1.0, 1.0, 2.2), body)
    leds = [neon.box(f"led{i}", (-2.2, -0.51, 0), (0.8, 0.02, 0.06), neon.mat_glow(f"ledm{i}", random.choice([P["green"], P["cyan"], P["pink"]]), 12)) for i in range(9)]
    ball = neon.sphere("ball", (2.2, 0, 0), 0.9, neon._principled("steel", (0.75, 0.78, 0.82), 0.25, 0.9, emit=(0.5, 0.6, 0.8), emit_strength=0.35), seg=48)
    land = next(f for f in range(1, n + 1) if z(f) <= 0) if any(z(f) <= 0 for f in range(1, n + 1)) else n
    zc = lambda f: max(0.0, z(f))                                               # noqa: E731
    neon.key_path(rack, lambda f: (-2.2, 0, zc(f) + 1.1), 1, n)
    for i, l in enumerate(leds):
        neon.key_path(l, lambda f, i=i: (-2.2, -0.51, zc(f) + 0.25 + i * 0.22), 1, n)
    neon.key_path(ball, lambda f: (2.2, 0, zc(f) + 0.9), 1, n)
    for x in (-2.2, 2.2):
        bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.05, location=(x, 0, 0.05))
        ring = neon.assign(bpy.context.object, neon.mat_glow(f"impact{x}", P["yellow"], 20))
        neon.key_visible(ring, lambda f: land <= f < land + 12, 1, n)
        neon.key_path(ring, lambda f: (ring.location.x, 0, 0.05), 1, n, scale_fn=lambda f: 1 + 0.25 * max(0, f - land))
    cam, _ = neon.camera("cam", (0, -15, 4.8), (0, 0, 4.0), lens=26)
    meta("drop_test", frames=n, release=f_rel, land=land)
    return cam, 1, n


def shot_sync_space(preview):
    neon.reset()
    neon.lights(energy=1.0)
    _, n = tile_floor("sync")
    planet()
    cam, _ = neon.camera("cam", (0, -20, 26), (0, 0, 0), lens=30)
    neon.key_path(cam, lambda f: (0, -20 + 6 * f / n, 26 - 6 * f / n), 1, n)
    meta("sync_space", frames=n)
    return cam, 1, n


SHOTS = {
    "eve_battle": shot_eve_battle, "tower_clocks": shot_tower_clocks, "tiles_ripple": shot_tiles_ripple,
    "march": shot_march, "light_race": shot_light_race, "eclipse": shot_eclipse,
    "drop_test": shot_drop_test, "sync_space": shot_sync_space,
}

if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    name = argv[0]
    preview = "--preview" in argv
    cam, f0, f1 = SHOTS[name](preview)
    if preview:
        mid = (f0 + f1) // 2
        for f in (f0, mid, f1):
            neon.render(cam, os.path.join(BUILD, "preview", name, str(f)), f, f)
    else:
        neon.render(cam, os.path.join(BUILD, "frames", name), f0, f1)
