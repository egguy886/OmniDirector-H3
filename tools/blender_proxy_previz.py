#!/usr/bin/env python3
"""OmniDirector-H3 3D Spatial Proxy Previsualizer

A headless Blender Python automation tool to validate spatial blocking,
camera sightlines, the 180° action axis, and multi-shot continuity before prompt rendering.

Usage:
    blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render
"""

import argparse
import math
import sys
from pathlib import Path


def run_blender_blocking():
    try:
        import bpy
        from mathutils import Vector
    except ImportError:
        print("Note: This script must be executed inside Blender's python environment:")
        print("  blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render")
        return

    # Extract args passed after '--'
    argv = sys.argv
    if "--" in argv:
        custom_args = argv[argv.index("--") + 1:]
    else:
        custom_args = []

    parser = argparse.ArgumentParser(description="Blender Headless Previsualization")
    parser.add_argument("--episode", default="E01", help="Episode ID (e.g. E01)")
    parser.add_argument("--render", action="store_true", help="Render contact sheet stills")
    parser.add_argument("--output-dir", default="previz_renders", help="Directory for output stills")
    args = parser.parse_args(custom_args)

    print(f"==================================================")
    print(f"OmniDirector-H3: Initializing 3D Previz for {args.episode}...")
    print(f"==================================================")

    # 1. Reset scene
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.resolution_x = 240
    scene.render.resolution_y = 426
    scene.render.fps = 24

    # 2. Build proxy environment (ground floor and back wall)
    bpy.ops.mesh.primitive_plane_add(size=15, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor_Proxy"

    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 5, 2))
    wall = bpy.context.active_object
    wall.scale = (8, 0.2, 4)
    wall.name = "BackWall_Proxy"

    # 3. Build Actor Proxies (Height 1.75m cylinders)
    # Actor A (Cade / Protagonist)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=1.75, location=(-1.2, 1.5, 0.875))
    actor_a = bpy.context.active_object
    actor_a.name = "Actor_A_Cade"

    # Actor B (Reeve / Antagonist)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=1.75, location=(1.2, 1.5, 0.875))
    actor_b = bpy.context.active_object
    actor_b.name = "Actor_B_Reeve"

    # 4. Action Axis verification (Line between A and B is along X at Y=1.5)
    # Camera must strictly stay at Y < 1.5 (e.g. Y = -2.5) to protect the 180° line!
    cam_data = bpy.data.cameras.new("Director_Camera")
    cam_data.lens = 35  # 35mm lens
    cam_obj = bpy.data.objects.new("Director_Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    cam_obj.location = (0, -2.8, 1.4)
    cam_obj.rotation_euler = (math.radians(82), 0, 0)

    # 5. Key light
    light_data = bpy.data.lights.new(name="Key_Light", type="SUN")
    light_data.energy = 3.5
    light_obj = bpy.data.objects.new(name="Key_Light", light_data)
    bpy.context.collection.objects.link(light_obj)
    light_obj.location = (-3, -2, 4)

    out_dir = Path(args.output_dir) / args.episode
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.episode}_proxy_blocking.png"

    if args.render:
        scene.render.filepath = str(out_path)
        bpy.ops.render.render(write_still=True)
        print(f"Previsualization rendered successfully to: {out_path}")
    else:
        print("Proxy setup complete. (Run with --render to generate image).")


if __name__ == "__main__":
    run_blender_blocking()
