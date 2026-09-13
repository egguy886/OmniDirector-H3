---
name: omni-director-h3
description: Industrial-grade screenplay-to-video production pipeline for MiniMax H3 and modern diffusion models. Covers Mode B bilingual scriptwriting (with atomic momentum decoupling, physiological tension, and pacing), Blender 3D spatial proxy blocking and 180° continuity audit, official MiniMax H3 multimodal prompt compilation (<d> tags, timestamps, silent non-diegetic music), and automated unattended off-peak batch orchestration.
---

# OmniDirector-H3: Industrial Screenplay-to-Video Production Engine

**OmniDirector-H3** is a full-stack, battle-tested AI cinematic production framework. It bridges the critical gap between literary screenwriting and AI video diffusion generation, transforming narrative intentions into high-fidelity, continuity-locked 15-second micro-drama video segments.

---

## The Core Problem It Solves

When traditional screenplays or amateur AI prompts are fed into state-of-the-art video models (such as MiniMax H3, Kling, Runway Gen-3, Sora), generation frequently fails due to:
1. **Diffusion Melting & Extra Limbs**: Complex compound verbs (e.g. *"he walks over, sits down, and smiles while grabbing her hand"*) cause spatial morphing and limb duplication.
2. **Axis Jumping & Spatial Disorientation**: AI generators lack 3D spatial awareness, constantly flipping character left/right positioning and breaking the 180° rule.
3. **Dialogue & Audio Desynchronization**: Spoken lines desync from mouth movement, while random hallucinated background music ruins professional post-production.
4. **Safety Filter Rejections**: Clumsy romance and high-emotion descriptions trigger censorship blocks, leading to high rejection rates.
5. **Manual Production Bottlenecks**: Creating hundreds of 15s clips manually results in human fatigue, inconsistent prompts, and wasted GPU discount windows.

OmniDirector-H3 eliminates these issues through a rigorous 4-tier pipeline.

---

## 4-Tier Pipeline Architecture

```
[ Tier 1: Screenplay Dramaturgy ]
  Mode B Bilingual Script -> Atomic Momentum Decoupling (△) -> Implicit Tension Design
             │
             ▼
[ Tier 2: Spatial Blocking & Continuity Audit ]
  Blender 3D Proxy Staging -> 180° Axis Defense -> 24fps Motion Budget -> Prop State Machine
             │
             ▼
[ Tier 3: H3 Multimodal Prompt Compiler ]
  Official MiniMax H3 Syntax -> Timestamped Cuts -> Dual-Tier Audio Isolation -> CLI Tag Audit
             │
             ▼
[ Tier 4: Autonomous Production Orchestrator ]
  AutoDL/ComfyUI API Adapter -> Off-Peak Discount Window Daemon -> Resumable Checkpoint State
```

---

## Sub-Skills Breakdown

### 1. `01_screenplay_dramaturgy` (剧作重构与动力学解耦)
- **Mode B Bilingual Spec**: Chinese action lines (`△`) for nuanced directional staging + English spoken dialogue for global streaming release.
- **Atomic Momentum Decoupling**: Decomposes complex human interaction into distinct `touch → reaction → hold/release` units. Exactly one primary kinetic vector per shot beat.
- **Implicit Physiological Tension**: Evokes intense emotional, athletic, and romantic chemistry via sensory details (perspiration sheen, breath vapor in low ambient temperatures, clavicle shadows, micro-hesitations) without triggering safety filters.
- **Micro-Drama Pacing**: 15s hook intervals within 120s vertical episode structures.

### 2. `02_spatial_blocking_audit` (Blender 3D空间调度与分镜连续性校验)
- **3D World Coordinate Anchor**: Proxy models in Blender verify exact character positions, gaze vectors, and the 180° camera axis before prompt generation.
- **24fps Motion Budget**: Calculates realistic physical displacement (e.g., maximum 3.5 seconds for a hand movement from desk to pocket) to prevent action overcrowding.
- **Transition Continuity Arbiter**:
  - `TAIL_RELAY`: Inherits the verified tail-frame (`0.5s - 1.5s` steady state) of segment N as reference image for segment N+1.
  - `HARD_CUT`: Clean spatial transitions with zero tail-frame inheritance.
  - `CAUSAL_MATCH_CUT`: Dynamic kinetic or object matching across scene boundaries.
- **Prop & Injury State Machine**: Formally tracks damage, wardrobe alterations, and handheld object lifecycles across shots.

### 3. `03_h3_prompt_compiler` (MiniMax H3 官方提示词编译器与语法合规)
- **Official MiniMax H3 Syntax**:
  - Reference alignment declaration (`<Picture 1> from [Shot 1] aligns with 0.00s...`).
  - `integrated_multimodal_description:` containing sequential `[Shot X]` definitions with millisecond timestamps (`At 00:03.500`).
  - Official voice tags: `<d> Speaker: "Exact spoken line" </d>`.
- **Dual-Tier Audio Engineering**:
  - `overall_soundscape:` Foley footsteps, fabric friction, spatial reverberation, wind and mechanical drone.
  - `non_diegetic_music: SILENT`: Generates clean, isolated production dialogue and foley, allowing professional score laying in post-production.
- **Automated Syntax Auditor**: Regex validation verifying 100% tag closure, punctuation compliance, and timestamp ordering.

### 4. `04_production_orchestrator` (无人值守批处理调度与自动化生产引擎)
- **Off-Peak Discount Window Daemon**: Schedules execution down to the exact second (e.g., 00:01:00 to 08:00:00) with OS anti-sleep (`caffeinate`) lock.
- **Resumable Fault-Tolerant Engine**: `batch_progress.json` tracks the state of every segment (`PENDING` -> `SUBMITTED` -> `COMPLETED`), preventing redundant API spend.
- **Automatic Asset Packaging**: Encodes character portraits, scene backdrops, and audio references into compliant base64 payloads.
- **Batch Video QC & Stitching**: Automatically downloads rendered MP4s and compiles contact-sheet validation logs.

---

## Directory Quick Reference

| Directory / File | Description |
|---|---|
| `subskills/` | Granular specifications and rules for each of the 4 tiers |
| `tools/audit_h3_prompts.py` | CLI tool to audit syntax and tag balance of H3 prompt files |
| `tools/compile_screenplay_to_h3.py` | CLI compiler translating script segments into H3 scaffolds |
| `tools/run_overnight_batch.py` | Autonomous off-peak batch production engine |
| `tools/blender_proxy_previz.py` | Headless Blender script for 3D camera & blocking previsualization |
| `templates/` | Standard templates for scripts, prompts, and continuity contracts |
| `examples/` | Battle-tested sample scripts and prompt sets from E01–E02 |

---

## Usage Workflow

1. **Step 1 - Script**: Author or adapt narrative using `subskills/01_screenplay_dramaturgy`. Apply atomic action decoupling.
2. **Step 2 - Spatial QC**: Run `tools/blender_proxy_previz.py` to verify camera line-of-action and 180° rule.
3. **Step 3 - Compile Prompts**: Assemble prompts following `subskills/03_h3_prompt_compiler` and validate using `tools/audit_h3_prompts.py`.
4. **Step 4 - Batch Render**: Set schedule and execute `tools/run_overnight_batch.py` to produce broadcast-grade video unattended.
