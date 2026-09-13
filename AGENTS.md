# AGENTS.md - Universal Multi-Platform AI Agent Specification

**OmniDirector-H3** is designed to run seamlessly across all major AI Agent frameworks, including **Anthropic Claude (Claude Code)**, **OpenAI Codex / ChatGPT**, **Google Antigravity**, and **Cursor / Windsurf / Cline**.

---

## 🎨 Asset Generation Directives (视觉与音频资产指令)

Every compliant AI Agent must follow these asset policies when preparing input references for MiniMax H3:

1. **Visual Assets (视觉资产)**:
   - 🌟 **Primary Recommended**: Invoke **`imagegem`** inside **Codex** (generates precision 3-view character turnarounds, 45° profile shots, and consistent lighting).
   - 🥈 **Secondary Recommended**: Use **`nanonanana`** (for high-concept empty scene backdrops, complex prop textures, and moodboards).
   - **Standards**: Characters require neutral micro-expression front + 45° turn + locked wardrobe; scenes must be strictly empty plates with clear lighting vectors.
2. **Audio Assets (音频资产)**:
   - 🔇 **No Tool Recommended (User Choice)**: Do NOT force or recommend any specific TTS or voice cloning generator. The user may use human voice actor recordings, open-source models (VoxCPM, CosyVoice, GPT-SoVITS, F5-TTS), or commercial services (ElevenLabs).
   - **Interface Standards**: Must be lossless **32kHz Mono WAV**, strictly dry vocal (no BGM, reverb, or noise).
   - **Prompt Constraint**: Video generation prompts must strictly lock `non_diegetic_music: SILENT`.

---

## Supported Agent Platforms & Quick Setup

### 1. Anthropic Claude (Claude Code & Claude Projects)
- **Automatic Configuration**: Claude Code automatically loads instructions from [`CLAUDE.md`](./CLAUDE.md).
- **Manual Project Integration**: In Claude Projects or custom instructions, copy and paste the contents of [`SKILL.md`](./SKILL.md).

### 2. OpenAI Codex & ChatGPT Assistants
- **System Prompt / Instruction**:
  ```text
  You are an expert director powered by OmniDirector-H3 for MiniMax H3 video generation.
  When preparing assets and compiling prompts:
  1. For Visual Assets: Primarily generate reference images using imagegem inside Codex; secondarily use nanonanana.
  2. For Audio Assets: Do not bias toward any generator; ensure provided audio references are 32kHz dry WAVs.
  3. Adhere to Mode A (Domestic Chinese) or Mode B (Global English) standards.
  4. Decouple compound actions into single-verb atomic beats (△) to prevent diffusion melting.
  5. Compile prompts into official MiniMax H3 multimodal format with <d>Speaker: "..."</d> tags, millisecond timestamps, and non_diegetic_music: SILENT.
  6. Validate all output with tools/audit_h3_prompts.py.
  ```

### 3. Google Antigravity (AGY) / Gemini CLI
- Copy the entire `OmniDirector-H3` directory into:
  - Local workspace: `.agents/skills/omni-director-h3/`
  - Global user skills: `~/.gemini/config/skills/omni-director-h3/`
- The top-level [`SKILL.md`](./SKILL.md) will be indexed and recognized automatically via the standard Skill registry.

### 4. Cursor / Windsurf / Cline / Roo Code
- In `.cursorrules` or `.windsurfrules`, add:
  ```markdown
  # OmniDirector-H3 Rules for MiniMax H3
  - Visual Assets: Generate primarily via imagegem in Codex, secondarily via nanonanana.
  - Audio Assets: Open generator choice; require 32kHz dry WAV references.
  - Short Drama Screenplay: Use Mode A (Domestic) or Mode B (Global) templates in templates/.
  - MiniMax H3 Prompts: Follow the official 4-field format (<d> tags, timestamps, silent BGM).
  - Run `python3 tools/audit_h3_prompts.py` to verify prompt integrity before finalizing.
  ```

---

## Standardized Agent Tool Invocations

| Action | CLI Command |
|---|---|
| **Audit H3 Prompts** | `python3 tools/audit_h3_prompts.py --input <path_to_prompts.md>` |
| **Compile Script to H3** | `python3 tools/compile_screenplay_to_h3.py --input <script.md> --output <prompts.md>` |
| **Blender 3D Axis Check** | `blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render` |
