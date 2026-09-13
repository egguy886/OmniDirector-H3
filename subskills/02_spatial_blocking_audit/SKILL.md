---
name: omni-director-spatial-blocking
description: 3D Blender proxy previsualization, 180-degree axis defense, 24fps motion budget calculation, and transition continuity arbitration.
---

# Sub-Skill 02: Spatial Blocking & Continuity Audit

## Purpose
Generative video diffusion models have no intrinsic 3D world model. When a character looks screen-left in shot 1, a naive prompt in shot 2 often flips them screen-right or inverts the room lighting. 

This sub-skill uses headless Blender 3D proxy staging to validate camera angles, verify the 180° action line, enforce physical motion budgets at 24fps, and formally classify shot-to-shot transitions before prompts are compiled.

---

## Core Principles

### 1. The 180° Action Axis Rule
- In every dialogue and confrontation space, an invisible line of action connects Actor A and Actor B.
- All cameras across contiguous shots must stay strictly on one side of this axis.
- Crossing the line requires an explicit on-screen neutral shot (e.g. looking straight down the axis or a high overhead top-down view) to re-orient the audience.

### 2. 24fps Motion Budget Allocation
- Video models fail when tasked with impossible physical travel within small time windows.
- In a 3.5-second shot budget ($3.5 \times 24 = 84$ frames):
  - Normal walking speed = 1.2 m/s $\implies$ max displacement $\approx$ 4.2 meters.
  - Sled push / heavy struggle $\implies$ max displacement $\approx$ 1.5 meters.
  - Arm extension and grab $\implies$ max displacement $\approx$ 0.8 meters (duration 0.8s).
- Overcrowding actions within a 15-second generation causes the diffusion model to speed up like a silent slapstick comedy or distort geometry.

### 3. Transition Continuity Arbiter
Every 15-second segment boundary must be explicitly classified into one of four transition contracts:

| Transition Type | Visual State | Audio Bridge | Reference Inheritance |
|---|---|---|---|
| `TAIL_RELAY` | Same scene, contiguous time. | Ambient bed continues uninterrupted. | Previous segment tail frame ($t = 14.0s$) becomes `ref_image_0` for the next segment. |
| `HARD_CUT` | Instant jump to new scene/location. | Hard sound transition or acoustic clash. | Zero tail frame inheritance. Initial frame uses new Scene reference. |
| `CAUSAL_MATCH_CUT` | Graphic/motion match across different spaces. | Action sound impact matches on cut. | Inherit specific object or vector prompt anchor, but independent image asset. |
| `CROSS_CUT` | Parallel action unfolding simultaneously. | L-cut or J-cut dialogue overlap. | Independent scene reference assets. |

### 4. Prop & Injury State Machine
Objects and physical states cannot magically heal or reset between shots. Track the lifecycle:
- **Clean / Intact** $\longrightarrow$ **Damaged / Stained** $\longrightarrow$ **Broken / Destroyed**
- Examples: Wet training shirt cannot dry within 30 seconds; ripped sleeve remains torn; opened dossier remains unsealed.
