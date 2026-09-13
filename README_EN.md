# OmniDirector-H3
## The Industrial Screenplay-to-Video Production Engine for MiniMax H3 & Next-Generation Diffusion Models

---

## 1. Executive Summary & The Core Dilemma

Generative video diffusion models (such as MiniMax H3, Kling, Runway Gen-3, Sora, and Hailuo) have unlocked unprecedented fidelity in synthetic video generation. However, when deployed in commercial episodic production (e.g. 120-second vertical micro-dramas for platforms like ReelShort, DramaBox, ShortMax, or TikTok), production teams encounter a severe **"Literary-to-Diffusion Incompatibility"**:

1. **Diffusion Melting & Anatomical Hallucinations**:
   Traditional screenplays rely on compound verbs and simultaneous actions (*e.g., "He sprints into the room, sits on the chair, drinks coffee, and glares furiously at her"*). In video diffusion models, multi-action concurrency triggers latent collapse, resulting in mutated limbs, third arms, melting faces, and chaotic spatial warping.
2. **Spatial Disorientation & The 180° Axis Collapse**:
   Text prompts lack a persistent 3D spatial coordinate system. When switching shots across scenes, characters randomly flip from screen-left to screen-right, breaking the fundamental 180° line-of-action rule and causing acute viewer disorientation.
3. **Safety Censorship False Positives**:
   Vertical short dramas thrive on athletic charisma, romantic tension, and visceral stakes. Naive prompt engineering using explicit sensory words (*"sexy"*, *"touching breasts"*, *"erotic kiss"*) triggers automated safety guardrails, resulting in massive job rejection rates.
4. **Hallucinated Background Scores Corrupting Master Audio**:
   End-to-end multimodal generators often hallucinate low-quality, tinny synthesizer music beds that bleed into the dialogue and physical Foley, completely preventing professional sound re-recording and master score mixing.
5. **Human Fatigue & Compute Budget Inefficiency**:
   A 10-episode micro-drama season requires generating 80 discrete 15-second segments (1,200 seconds of finished footage). Manually generating and checking clips through web UIs is physically exhausting and misses off-peak GPU discount windows (e.g. 50% discount between 00:01 and 08:00).

**OmniDirector-H3** was built to eliminate these hurdles. It is an end-to-end industrial operating system comprising four tightly coupled tiers: script adaptation, 3D spatial blocking, prompt compilation, and autonomous unattended batch rendering.

---

## 2. In-Depth Architectural Tiers

### Tier 1: Screenplay Dramaturgy & Momentum Decoupling (`01_screenplay_dramaturgy`)

*Translating literary drama into diffusion-executable atomic kinetic vectors.*

- **Mode B Bilingual Standard**:
  - **Action & Direction Lines (`△`)**: Authored in high-density Chinese, leveraging its rich inventory of precise causal verbs and directional spatial markers.
  - **Spoken Dialogue**: Authored in natural, idiomatic American English tailored for international audiences, reflecting youth athletics and suspense genres.
  - **Subtext Channel**: Annotated as `[Subtext: ...]`, preserved solely for human editorial review and strictly isolated from the dialogue synthesis engine.
- **Atomic Momentum Decoupling**:
  - **Single Kinetic Vector Rule**: Exactly one dominant physical action per shot beat.
  - **Causal Triad Sequence**:
    $$\text{Contact / Initiation} \longrightarrow \text{Physical Reaction} \longrightarrow \text{Release / Steady State}$$
  - Sprints, grabs, lines of dialogue, and head turns are cleanly decoupled across consecutive shots.
- **Implicit Physiological Tension (Safety-Compliant Writing)**:
  - Subjective, high-risk adjectives are completely replaced with observable, objective physical phenomena:
    - *Athletic Physique* $\rightarrow$ Sweat-dampened jersey clinging tightly to the contours of pectoral muscles; sweat droplets catching directional rim light in the hollow of the clavicle; flexed forearm veins.
    - *Intense Proximity & Romantic Heat* $\rightarrow$ Distance closing to an exact 10-centimeter threshold; heavy breathing producing visible white condensation clouds in 4°C ambient air; pulse visibly thumping at the jugular notch.

---

### Tier 2: 3D Spatial Blocking & Continuity Audit (`02_spatial_blocking_audit`)

*Defending physical world geometry using low-cost headless 3D proxy scenes.*

- **180° Action Axis Enforcement**:
  - A headless Blender Python pipeline establishes the virtual line-of-action between interlocutors.
  - Camera coordinates are mathematically bound to one side of the axis ($Y < 0$); axis crossovers require an explicit on-axis neutral transition (e.g. bird's-eye overhead or reverse tracking shot).
- **24fps Motion Budget Allocation**:
  - Within a 3.5-second shot budget ($3.5 \times 24 = 84$ frames), physical displacement is capped by human anatomical speed (sprint max 10 m/s, walk 1.2 m/s, arm reach 0.8s), preventing comical hyperspeed twitching.
- **Transition Continuity Arbiter**:
  - `TAIL_RELAY`: For continuous time/space, extracts the final 1.0s steady-state frame of segment $N$ as the seed image (`ref_image_0`) for segment $N+1$.
  - `HARD_CUT`: For spatial transitions, cuts off image inheritance and initializes fresh scene environment anchors.
  - `CAUSAL_MATCH_CUT`: Matches dynamic vector momentum across distinct environments.
- **Prop & Injury State Machine**:
  - Tracks physical modifications (e.g. sealed dossier $\rightarrow$ ripped wax seal $\rightarrow$ scattered pages; dry shirt $\rightarrow$ drenched sweat), preventing magical self-healing continuity errors.

---

### Tier 3: MiniMax H3 Multimodal Prompt Compiler (`03_h3_prompt_compiler`)

*Discarding legacy custom headers; aligning with native MiniMax cross-attention.*

Empirical production tests prove that legacy custom "6-module" Chinese formats dilute diffusion cross-attention, causing missed timestamp cuts and composition drift. OmniDirector-H3 enforces the **Official MiniMax H3 4-Field Standard**:

1. **Reference Picture Alignment Header**:
   ```text
   For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
   ```
2. **Multimodal Sequential Script (`integrated_multimodal_description:`)**:
   - Shot 1 establishes global cinematic lighting, aspect ratio (9:16 vertical), and camera lens profile.
   - Subsequent shots use millisecond-precision monotonically increasing cut timestamps (`[Shot 2] At 00:03.500, the camera cuts to...`).
   - Official dialogue enclosures: `<d> Speaker: "Exact spoken line" </d>`.
3. **Diegetic Soundscape (`overall_soundscape:`)**:
   - Exhaustively itemizes physical Foley, acoustic room tones, footwear traction, and industrial ventilation hum.
4. **Music Isolation Lock (`non_diegetic_music: SILENT`)**:
   - **Crucial Industry Standard**: Hard-locked to `SILENT` during AI video generation. This isolates voice and Foley tracks, allowing human re-recording engineers to layer cinematic musical scores in post-production.
5. **Deterministic Tag & Syntax Auditor (`tools/audit_h3_prompts.py`)**:
   - Automated CLI validating tag balancing, timestamp sorting, token boundaries, and structural validity.

---

### Tier 4: Autonomous Production Orchestrator (`04_production_orchestrator`)

*Precision off-peak batch rendering with fault-tolerant state recovery.*

- **Discount Window Wake-Up Lock (00:01:00 Start)**:
  - Many GPU clouds (such as AutoDL) offer a 50% discount on compute between 00:01:00 and 08:00:00.
  - Built-in timer calculates the exact sleep delay, activates macOS `caffeinate` or Linux systemd power assertions, and wakes the workstation at 00:01:00 sharp.
  - Enforces a hard cutoff at 08:00:00 to prevent higher peak-rate billing.
- **Resumable State Machine (`batch_progress.json`)**:
  - Tracks the lifecycle of every 15-second clip: `PENDING` $\rightarrow$ `SUBMITTING` $\rightarrow$ `RUNNING` $\rightarrow$ `COMPLETED`.
  - In the event of network dropouts or reboots, restarting the orchestrator automatically resumes from the last unfinished clip with **zero redundant API cost**.
- **Automated Base64 Asset Assembly**:
  - Dynamically packages character face references, wardrobe locks, scene backgrounds, and 32kHz reference voice clips into compliant JSON payloads.
- **Post-Production Download & Automated Contact Sheets**:
  - Polls completion endpoints, verifies MP4 container headers via ffprobe, and renders visual audit contact sheets.

---

## 3. Directory Layout

```text
OmniDirector-H3/
├── README.md                          # Flagship Landing Page
├── README_CN.md                       # Comprehensive Technical Manual (Chinese)
├── README_EN.md                       # Comprehensive Technical Manual (English)
├── SKILL.md                           # AI Agent Standard Skill Specification
├── LICENSE                            # MIT License
│
├── subskills/                         # Granular Sub-Skill Modules
│   ├── 01_screenplay_dramaturgy/      # Scriptwriting, Mode B, Atomic Decoupling
│   │   ├── SKILL.md
│   │   └── rules.md
│   ├── 02_spatial_blocking_audit/     # Blender 3D Previz, 180° Axis, Transitions
│   │   ├── SKILL.md
│   │   └── blocking_contract.md
│   ├── 03_h3_prompt_compiler/         # MiniMax H3 Syntax, Dialogue Tags, Timestamps
│   │   ├── SKILL.md
│   │   └── syntax_guide.md
│   └── 04_production_orchestrator/    # Unattended Batch Engine, Off-Peak Timers
│       ├── SKILL.md
│       └── checkpoint_spec.md
│
├── tools/                             # Production-Ready CLI Utilities
│   ├── audit_h3_prompts.py            # Syntax & tag auditor (zero error gate)
│   ├── compile_screenplay_to_h3.py   # Screenplay to H3 prompt scaffold compiler
│   ├── run_overnight_batch.py         # Autonomous off-peak batch production daemon
│   ├── blender_proxy_previz.py        # Headless Blender 3D spatial validator
│   └── push_to_github.sh              # One-click repository publish assistant
│
├── templates/                         # Industrial Production Templates
│   ├── screenplay_spec_b_template.md  # Mode B bilingual screenplay template
│   ├── h3_prompt_template.md          # Official 15s H3 multimodal prompt template
│   └── continuity_contract_template.md# Multi-episode asset & prop state contract
│
└── examples/                          # Battle-Tested Real World Assets (E01)
    ├── E01_screenplay_sample.md       # Production screenplay with physical tension
    ├── E01_h3_prompts_sample.md       # Compiled 8-segment prompt packet (Audit: 0 errors)
    └── batch_progress_example.json    # Production state checkpoint schema
```

---

## 4. Quick Start in 5 Minutes

### Step 1: Clone Repository & Grant Permissions
```bash
git clone https://github.com/egguy886/OmniDirector-H3.git
cd OmniDirector-H3
chmod +x tools/*.py tools/*.sh
```

### Step 2: Audit Prompts Before Submission
Verify that your prompts contain zero syntax bugs, unclosed tags, or legacy headers:
```bash
python3 tools/audit_h3_prompts.py --input examples/E01_h3_prompts_sample.md
```

### Step 3: Compile Screenplay into MiniMax H3 Prompt Scaffolds
```bash
python3 tools/compile_screenplay_to_h3.py \
  --input templates/screenplay_spec_b_template.md \
  --output my_episode_prompts.md
```

### Step 4: Launch Unattended Overnight Batch Production
Set your API key and launch the orchestrator with anti-sleep protection:
```bash
export AUTODL_API_KEY="your_api_key_here"

# On macOS, prevent machine sleep while counting down to 00:01:00:
caffeinate -d -i -m -u python3 tools/run_overnight_batch.py

# Or perform an instant dry-run simulation:
python3 tools/run_overnight_batch.py --dry-run
```

---

## 5. Open Source License
OmniDirector-H3 is open-sourced under the **MIT License**. Contributions, issues, and pull requests from indie creators, AI studios, and developers worldwide are warmly welcome!
