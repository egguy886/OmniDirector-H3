# Spatial Blocking & Continuity Contract

## 1. Segment Steady-State Rule (Tail Frame Lock)
For any segment marked as `TAIL_RELAY`:
- **Time Window [13.5s – 15.0s]**: The camera motion must decelerate to a complete stop or an imperceptible slow drift ($< 0.05$ m/s).
- **Actor State**: No new characters may enter; no violent turns or hand switches.
- **Lighting**: Light sources must remain stable (no sudden strobe or daylight switch).
- **QC Criteria**: Only tail frames passing `DECODED -> VISUALLY_CHECKED -> TAIL_APPROVED` may be passed into downstream pipeline segments.

## 2. 3D Coordinate Reference Map
In our proxy coordinate system:
- **Origin (0, 0, 0)**: Center of the key dramatic interaction zone.
- **X-Axis**: Lateral movement (Left -X / Right +X).
- **Y-Axis**: Depth / Distance from primary lens (Near -Y / Far +Y).
- **Z-Axis**: Elevation (Ground 0.0m / Eye Level 1.65m / Overhead 3.5m).

## 3. Blender Headless Verification Command
```bash
blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render
```
Generates 240x426 9:16 proxy contact sheets verifying:
1. Camera sightlines and focal lengths (28mm wide vs 50mm normal vs 85mm portrait).
2. Actor occlusion and line of sight.
3. Lighting angle relative to key facial contours.
