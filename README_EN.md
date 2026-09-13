# OmniDirector-H3
## The Industrial Screenplay-to-Video Production Engine Specially Engineered for MiniMax H3

---

## 1. Naming & Architectural Philosophy: What Does "Omni" Mean?

### The Meaning of "Omni"
**"Omni"** (/ˈɒmni/) originates from the Latin root *omnis*, signifying **"all", "universal", "all-encompassing", and "all-knowing"**. It represents apex architectural control in philosophy and technology:
* **Philosophy**: *Omniscient* (all-knowing, understanding every root cause), *Omnipotent* (all-powerful, possessing absolute generative agency);
* **Cutting-Edge Technology**: *NVIDIA Omniverse* (the universal simulation and virtual reality platform);
* **Enterprise Commerce**: *Omnichannel* (seamless, universal multi-platform integration).

### The Role of "OmniDirector"
In conventional AI video creation, most users operate as mere "Prompt Typers"—feeding raw novels into diffusion models and suffering from grotesque anatomical melting, disorienting 180° axis flips, desynchronized dialogue, and random synthesizer music that ruins post-production.

**OmniDirector** elevates the human creator and autonomous agent into an **all-encompassing cinematic director**:
1. **Omni-Dimensional**: Transcending plain text by integrating narrative literature, 3D Euclidean geometry, 24fps physical kinetics, micro-facial physiology, and acoustic Foley into one unified specification.
2. **Omni-Market**: Natively delivering dual-standard support: **Mode A (Domestic Chinese Micro-Dramas)** and **Mode B (Global Overseas Streaming Micro-Dramas)**.
3. **Omni-Consistent**: Defending the 180° camera action axis, tracking prop damage state machines, and enforcing `TAIL_RELAY` steady-state inheritance across multi-episode productions.

---

## 2. Engineered Specifically for MiniMax H3

**OmniDirector-H3 is custom-built to exploit the native architecture of MiniMax H3, MiniMax's flagship multimodal foundation model.**

Empirical testing reveals that legacy custom "6-module" Chinese formats dilute diffusion cross-attention, causing missed timestamp cuts and composition drift. OmniDirector-H3 strictly adheres to the **Official MiniMax H3 Standard**:

* **Official Millisecond-Precision Shot Cuts**: Injects absolute timestamps inside `integrated_multimodal_description:` (e.g. `[Shot 2] At 00:03.500, the camera cuts to...`), enabling broadcast-grade multi-shot cuts within a single 15-second generation.
* **Official Dialogue Enclosures (`<d>` Tags)**: Wraps spoken lines into strict `<d> Speaker: "..." </d>` tags to align mouth movement, pauses, and speaker characteristics.
* **Acoustic Stems Isolation (`non_diegetic_music: SILENT`)**: Hard-locks non-diegetic background score to `SILENT`, generating pristine dialogue and Foley stems, leaving musical scoring to post-production sound engineers.
* **Deterministic Tag & Syntax Gate**: Ships with `tools/audit_h3_prompts.py` to ensure zero unclosed tags, monotonic timestamps, and zero attention-diluting legacy headers before submission.

---


---

## 3. Visual & Audio Asset Directives

To guarantee reliable character face locks, lighting continuity, and vocal timing in MiniMax H3, the framework enforces strict asset interface standards (see [`templates/asset_production_spec.md`](templates/asset_production_spec.md)):

### 1. Visual Asset Generation Strategy
* 🌟 **Primary Recommended**: Invoke **`imagegem`** inside **Codex**.
  * *Rationale*: Natively synergistic with AI agent prompt engineering. Produces mathematically grounded 3-view character references, 45° profile turns, and authentic skin textures without plastic CG artifacts.
* 🥈 **Secondary Recommended**: **`nanonanana`**.
  * *Use Case*: Ideal for high-concept empty background environments, complex prop textures, and cinematic visual styling moodboards.
* **Key Visual Criteria**:
  * **Characters**: Neutral micro-expression front + 45° turn + full-body wardrobe anchor;
  * **Scenes**: Strictly empty plates without extraneous bystanders; locked key-light vectors;
  * **Props**: Clear silhouette and perspective supporting a physical damage state machine.

### 2. Audio Asset Generation Strategy
* 🔇 **No Generator Recommended (Creator Choice)**:
  * **This pipeline does not mandate or recommend any specific voice synthesis tool.**
  * Whether utilizing studio recordings from human voice actors, open-source models (VoxCPM, CosyVoice, GPT-SoVITS, F5-TTS), or commercial TTS providers (ElevenLabs), creators choose freely based on vocal timbre and commercial licensing.
* **MiniMax H3 Interface Specifications**:
  * **Format**: Lossless **WAV** (Mono);
  * **Sample Rate**: Standard **32kHz** (or 44.1kHz / 48kHz);
  * **Acoustic Purity**: **Strictly dry voice**, completely free of background music, noise, or reverberation;
  * **Duration**: 5.0 to 15.0 seconds containing 2–3 sentences with representative pacing and emotional pitch.
* **Video Generation Silence Lock**: Multi-shot prompts must hard-lock `non_diegetic_music: SILENT`. Music beds are assembled in post-production.

---

## 4. Multi-Platform AI Agent Integration (Claude Code / Codex / Antigravity)

OmniDirector-H3 natively supports major AI programming assistants and autonomous agent frameworks out of the box:

### 1. Anthropic Claude (Claude Code & Claude Projects)
* Natively configured via [`CLAUDE.md`](./CLAUDE.md) in the project root. Claude Code automatically loads all director directives upon initialization.
* For Claude Projects, import [`SKILL.md`](./SKILL.md) directly as your system prompt.

### 2. OpenAI Codex & ChatGPT Assistants
* Use the system prompt definitions in [`AGENTS.md`](./AGENTS.md) to instruct Codex to enforce Mode A/B standards and MiniMax H3 4-field prompt compilation.

### 3. Google Antigravity (AGY) / Gemini CLI
* Drop the repository into `.agents/skills/omni-director-h3/` or `~/.gemini/config/skills/`. The root [`SKILL.md`](./SKILL.md) is automatically registered as a recognized Skill.

### 4. Cursor / Windsurf / Cline / Roo Code
* Reference [`AGENTS.md`](./AGENTS.md) inside `.cursorrules` or `.windsurfrules` for real-time prompt syntax audits directly inside your IDE.

---

## 5. Tri-Tier Core Intelligence Pipeline

OmniDirector-H3's core responsibility is **compiling literary narrative into 100% compliant, failure-proof MiniMax H3 prompt packets and continuity matrices**.

```
[ Tier 1: Screenplay Dramaturgy & Momentum Decoupling ]
  Mode A (Domestic Chinese) / Mode B (Global Streaming) 
  -> Atomic Momentum Decoupling (△) -> Implicit Physiological Tension
             │
             ▼
[ Tier 2: 3D Spatial Blocking & Continuity Audit ]
  Blender 3D Proxy Staging -> 180° Axis Line Defense 
  -> 24fps Motion Budget -> Transition Arbiter (TAIL_RELAY vs HARD_CUT)
             │
             ▼
[ Tier 3: MiniMax H3 Official Prompt Compilation ]
  Official MiniMax H3 4-Field Standard -> Millisecond Precision Cuts 
  -> <d> Dialogue Tags -> Dual-Tier Audio Isolation -> Deterministic CLI Auditor
             │
             ▼
[ Standard Deliverable: Verified 15s H3 Prompt Packet + Continuity Contract ]
```

---

## 6. The Dual Production Modes (Mode A & Mode B)

| Dimension | Mode A: Domestic Chinese Standard | Mode B: Global Streaming Standard |
|---|---|---|
| **Target Distribution** | Douyin, Kuaishou, WeChat Channels, Fanqie, Hongguo | ReelShort, DramaBox, ShortMax, TikTok, ShortWave |
| **Action Staging (`△`)** | Dense Chinese verbs, atomic momentum decoupled | Dense Chinese verbs for precise spatial/momentum decoupling |
| **Character Names** | Authentic Chinese names (e.g. 林舟, 陆辰, 苏晴) | International English names (e.g. Cade, Reeve, Nia) |
| **Spoken Dialogue** | Fast-paced Chinese dialogue optimized for 3-second retention | Idiomatic, natural English with subtext and athletic rhythm |
| **Template Path** | [`templates/screenplay_spec_a_domestic_template.md`](templates/screenplay_spec_a_domestic_template.md) | [`templates/screenplay_spec_b_template.md`](templates/screenplay_spec_b_template.md) |

---

## 7. Flexible Execution: The User's Choice

Once OmniDirector-H3 delivers your verified, 0-error prompt packet, you have complete freedom in choosing your MiniMax H3 generation environment:
1. **MiniMax Official Creative Web UI**: Copy and paste prompt segments directly into the official web studio.
2. **MiniMax Open Platform REST API**: Ingest prompts into private enterprise production workflows.
3. **Cloud GPU / Local ComfyUI Nodes**: Run prompts through MiniMax H3 ComfyUI nodes on AutoDL, RunPod, or private clusters.
4. **Reference Batch Tool (Optional)**: Utilize `tools/run_overnight_batch.py` for unattended overnight rendering and checkpoint resumption.

---

## 8. Quick Start in 5 Minutes

```bash
# 1. Clone repository
git clone https://github.com/egguy886/OmniDirector-H3.git
cd OmniDirector-H3
chmod +x tools/*.py tools/*.sh

# 2. Compile screenplay into H3 prompt scaffold
python3 tools/compile_screenplay_to_h3.py \
  --input templates/screenplay_spec_a_domestic_template.md \
  --output my_episode_prompts.md

# 3. Audit prompt syntax (deterministic 0-error gate)
python3 tools/audit_h3_prompts.py --input examples/E01_h3_prompts_sample.md

# 4. Blender 3D Axis Previsualization (Optional)
blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render
```

---

## 9. License
This project is open-sourced under the **MIT License**.
