---
name: omni-director-prompt-compiler
description: MiniMax H3 multimodal prompt compilation, millisecond timestamp syntax, dialogue tag formatting, and audio isolation standards.
---

# Sub-Skill 03: H3 Multimodal Prompt Compiler

## Purpose
MiniMax H3 is a dual-stream multimodal video-and-audio generation architecture. Empirical production testing shows that legacy custom "6-module" Chinese prompt formats dilute the model attention mechanism, resulting in hallucinated camera movements, composition drift, and lost cut points.

This sub-skill compiles screenplays and continuity contracts into strict **Official MiniMax H3 Multimodal Specifications**, guaranteeing precise multi-shot camera cuts, accurate dialogue delivery, and pristine audio stems.

---

## Core Specification Structure

Every 15.0-second prompt packet consists of four mandatory fields:

```text
[Reference Alignment Header]
integrated_multimodal_description:
  [Shot 1] ...
  [Shot 2] At 00:03.500, ...
  [Shot 3] At 00:08.200, ...
overall_soundscape:
  ...
non_diegetic_music: SILENT
```

### 1. Reference Alignment Header
- **I2VA Mode (First frame seeded)**:
  `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`
- **Ref2VA Mode (Multiple keyframes / tail relays)**:
  `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 2) aligns with the 04.50-second mark of the target video.`

### 2. `integrated_multimodal_description:`
- **Shot 1**: Must state the global cinematic aesthetic, resolution/aspect ratio, lighting conditions, and camera lens profile.
- **Subsequent Shots**: Must include an explicit, monotonically increasing timestamp:
  `[Shot 2] At 00:03.500, the camera snaps into a close-up profile...`
- **Camera Dynamics**: Defined via `[Vector] + [Speed] + [Framing]` (e.g. `Low-angle tracking dolly push, steady 0.8 m/s`).
- **Dialogue Tags**: Strictly enclosed within `<d>` and `</d>`:
  `<d> Cade: "I did not sign that transfer." </d>`
  - Single speaker per dialogue window rule.
  - Zero unclosed tags.
  - Subtext and emotional qualifiers belong in the character action sentence, never inside quotes.

### 3. `overall_soundscape:`
- Captures all diegetic environmental sound effects (Foley, acoustics, machine hum, ambient weather).
- Example: `Deep sub-bass hum of industrial ventilation, squeak of rubber soles against wet polyurethane flooring, labored nasal breathing, metallic clank of steel door lock.`

### 4. `non_diegetic_music: SILENT`
- **Hard Rule**: Must be set to `SILENT`.
- Allowing diffusion models to hallucinate background score creates muddy, distorted audio stems that cannot be mixed or equalized during master video editing.

---

## Automated CLI Validation
Prompts are verified using the deterministic auditor:
```bash
python3 tools/audit_h3_prompts.py --input examples/E01_h3_prompts_sample.md
```
Passes only when:
- Segment count matches expected (8 segments per episode).
- `<d>` and `</d>` tag counts are identical.
- All timestamps follow `At MM:SS.mmm` format and increase strictly monotonically.
- Legacy custom module headers are completely absent.
