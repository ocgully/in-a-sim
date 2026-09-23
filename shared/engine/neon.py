"""Neon-arcade scene kit for headless Blender (tested on Blender 3.4, EEVEE).

Imported from inside Blender scripts:
    sys.path.insert(0, "<repo>/shared/engine"); import neon

Gives every episode the same look: dark void, glowing grid floor, emissive
"hologram" avatars, bloom. Everything is procedural (no downloaded assets),
so any scene can be re-rendered exactly from the repo.
"""
from __future__ import annotations

import math
import os

import bpy
from mathutils import Vector

FPS = 30
PALETTE = {
    "cyan": (0.20, 0.75, 1.00),
    "orange": (1.00, 0.45, 0.10),
    "pink": (1.00, 0.25, 0.65),
    "green": (0.25, 1.00, 0.45),
    "red": (1.00, 0.12, 0.10),
    "yellow": (1.00, 0.80, 0.20),
    "purple": (0.60, 0.35, 1.00),
    "white": (0.90, 0.95, 1.00),
    "grid": (0.05, 0.35, 0.60),
}


# ------------------------------------------------------------------ scene
def reset(res=(1280, 720), samples=16):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.fps = FPS
    sc.render.image_settings.file_format = "PNG"
    ev = sc.eevee
    ev.taa_render_samples = samples
    ev.use_bloom = True
    ev.bloom_intensity = 0.08
    ev.bloom_threshold = 0.8
    ev.use_gtao = True
    ev.use_ssr = True
    sc.view_settings.view_transform = "Filmic"
    sc.view_settings.look = "High Contrast"
    world = bpy.data.worlds.new("void")
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.004, 0.006, 0.012, 1)
    bg.inputs[1].default_value = 1.0
    sc.world = world
    return sc


def _principled(name, color, rough=0.4, metal=0.0, emit=None, emit_strength=0.0, alpha=1.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit is not None:
        b.inputs["Emission"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = emit_strength
    if alpha < 1.0:
        b.inputs["Alpha"].default_value = alpha
        m.blend_method = "BLEND"
        m.shadow_method = "NONE"
        m.show_transparent_back = False
    return m


def mat_solid(name, color, rough=0.35, metal=0.2):
    return _principled(name, color, rough, metal)


def mat_glow(name, color, strength=6.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs[0].default_value = (*color, 1)
    e.inputs[1].default_value = strength
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(e.outputs[0], o.inputs[0])
    return m


def mat_ghost(name, color, alpha=0.3, strength=1.5):
    return _principled(name, (0.02, 0.02, 0.03), 0.5, 0.0, emit=color, emit_strength=strength, alpha=alpha)


def mat_image_sequence(name, first_frame_path, n_frames, strength=2.0):
    """Emissive material showing an animated PNG sequence (e.g. a detector screen)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    tex = nt.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(first_frame_path)
    img.source = "SEQUENCE"
    tex.image = img
    tex.image_user.frame_duration = n_frames
    tex.image_user.frame_start = 1
    tex.image_user.frame_offset = 0
    tex.image_user.use_auto_refresh = True
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs[1].default_value = strength
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(tex.outputs[0], e.inputs[0])
    nt.links.new(e.outputs[0], o.inputs[0])
    return m


def assign(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)
    return obj


# ------------------------------------------------------------------ geometry
def grid_floor(size=80, cells=80, color=PALETTE["grid"], strength=1.2):
    bpy.ops.mesh.primitive_plane_add(size=size, location=(0, 0, -0.01))
    base = bpy.context.object
    assign(base, mat_solid("floor", (0.01, 0.012, 0.02), rough=0.75, metal=0.1))
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=cells, y_subdivisions=cells, size=size, location=(0, 0, 0))
    g = bpy.context.object
    mod = g.modifiers.new("wire", "WIREFRAME")
    mod.thickness = 0.03
    assign(g, mat_glow("gridglow", color, strength))
    return base, g


def box(name, loc, dims, mat):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    bpy.ops.object.transform_apply(scale=True)
    return assign(o, mat)


def sphere(name, loc, r, mat, seg=24):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=seg, ring_count=seg // 2)
    o = bpy.context.object
    o.name = name
    bpy.ops.object.shade_smooth()
    return assign(o, mat)


def cylinder_between(name, p1, p2, r, mat):
    p1, p2 = Vector(p1), Vector(p2)
    d = p2 - p1
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d.length, location=(p1 + p2) / 2)
    o = bpy.context.object
    o.name = name
    o.rotation_mode = "QUATERNION"
    o.rotation_quaternion = d.to_track_quat("Z", "Y")
    return assign(o, mat)


def avatar(name, body_color, visor_color=PALETTE["white"], ghost=False, alpha=0.3):
    """Capsule 'hologram soldier'. Origin at the feet, facing +X."""
    parts = []
    if ghost:
        body = mat_ghost(name + "_body", body_color, alpha=alpha, strength=2.0)
        visor = mat_ghost(name + "_visor", visor_color, alpha=min(1.0, alpha + 0.2), strength=4.0)
    else:
        body = _principled(name + "_body", tuple(c * 0.25 for c in body_color), 0.3, 0.5,
                           emit=body_color, emit_strength=0.6)
        visor = mat_glow(name + "_visor", visor_color, 8.0)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.0, location=(0, 0, 0.8))
    parts.append(assign(bpy.context.object, body))
    for z in (0.3, 1.3):
        parts.append(sphere(name + "_cap", (0, 0, z), 0.3, body))
    parts.append(sphere(name + "_head", (0, 0, 1.82), 0.22, body))
    parts.append(box(name + "_visor", (0.17, 0, 1.85), (0.1, 0.34, 0.09), visor))
    # stripe
    parts.append(box(name + "_stripe", (0.29, 0, 0.9), (0.04, 0.2, 0.6), mat_glow(name + "_stripeglow", body_color, 5)))
    bpy.ops.object.select_all(action="DESELECT")
    for p in parts:
        p.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()
    o = bpy.context.object
    o.name = name
    bpy.context.scene.cursor.location = (0, 0, 0)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    return o


def text3d(name, body, loc, size, mat, rot=(math.radians(90), 0, 0)):
    bpy.ops.object.text_add(location=loc, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.data.body = body
    o.data.size = size
    o.data.align_x = "CENTER"
    o.data.extrude = 0.02
    return assign(o, mat)


# ------------------------------------------------------------------ animation
def frame_of(t_game, slowmo, t0=0.0):
    return 1 + int(round((t_game - t0) * slowmo * FPS))


def key_visible(obj, visible_fn, f_start, f_end):
    """Keyframe hide_render/hide_viewport so obj is visible only where visible_fn(frame) is True."""
    last = None
    for f in range(f_start, f_end + 1):
        v = bool(visible_fn(f))
        if v != last:
            obj.hide_render = not v
            obj.hide_viewport = not v
            obj.keyframe_insert("hide_render", frame=f)
            obj.keyframe_insert("hide_viewport", frame=f)
            last = v
    for fc in obj.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = "CONSTANT"


def key_path(obj, pos_fn, f_start, f_end, rot_fn=None, scale_fn=None):
    for f in range(f_start, f_end + 1):
        obj.location = pos_fn(f)
        obj.keyframe_insert("location", frame=f)
        if rot_fn:
            obj.rotation_euler = rot_fn(f)
            obj.keyframe_insert("rotation_euler", frame=f)
        if scale_fn:
            s = scale_fn(f)
            obj.scale = (s, s, s) if isinstance(s, (int, float)) else s
            obj.keyframe_insert("scale", frame=f)


def camera(name, loc, target, lens=35):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = lens
    bpy.ops.object.empty_add(location=target)
    tgt = bpy.context.object
    tgt.name = name + "_target"
    c = cam.constraints.new("TRACK_TO")
    c.target = tgt
    c.track_axis = "TRACK_NEGATIVE_Z"
    c.up_axis = "UP_Y"
    return cam, tgt


def lights(key=(6, -6, 10), energy=3.0):
    bpy.ops.object.light_add(type="SUN", location=key)
    s = bpy.context.object
    s.data.energy = energy
    s.rotation_euler = (math.radians(50), 0, math.radians(30))
    bpy.ops.object.light_add(type="AREA", location=(0, 0, 12))
    a = bpy.context.object
    a.data.energy = 120
    a.data.size = 20
    a.data.color = (0.5, 0.7, 1.0)


def render(cam, out_dir, f_start, f_end):
    sc = bpy.context.scene
    sc.camera = cam
    sc.frame_start, sc.frame_end = f_start, f_end
    os.makedirs(out_dir, exist_ok=True)
    sc.render.filepath = os.path.join(out_dir, "f_")
    bpy.ops.render.render(animation=True)
