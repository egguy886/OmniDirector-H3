# MiniMax H3 Syntax Reference & Tagging Standard

## 1. Dialogue Tag Rules

### Valid Syntax
```text
<d> Cade: "Get off the lane." </d>
<d> Reeve: "Make me." </d>
```

### Prohibited Syntax
- ❌ `Cade: <d> "Get off the lane." </d>` (Speaker name outside tag)
- ❌ `<d> Cade: "Get off the lane."` (Unclosed tag - crashes parser)
- ❌ `<d> Cade: "Get off the lane." (angrily) </d>` (Actor direction inside dialogue)
- ❌ `<d> Cade: "Get off the lane." and then walks away. </d>` (Action inside dialogue)

## 2. Multi-Shot Timestamp Protocol

| Shot | Nominal Timestamp | Typical Purpose |
|---|---|---|
| `[Shot 1]` | `00:00.000` (Implicit) | Master establishing or immediate kinetic disruption |
| `[Shot 2]` | `At 00:03.500` | Medium reverse angle or character arrival |
| `[Shot 3]` | `At 00:07.800` | Tight close-up on physical contact or spoken line |
| `[Shot 4]` | `At 00:12.200` | Decelerating steady state / reaction lock for tail relay |

## 3. Reference Asset Mapping Protocol

```text
ref_image_0: S01_North_Ridge_dawn_track_reference_v2.png (Scene Backdrop)
ref_image_1: C01_Cade_reference_v1.png (Primary Protagonist)
ref_image_2: C04_Reeve_reference_v1.png (Antagonist / Rival)
ref_audio_0: VOICE_CADE_v2_age18_h3_32k.wav (Speaker 1)
ref_audio_1: VOICE_REEVE_v2_age18_h3_32k.wav (Speaker 2)
```
