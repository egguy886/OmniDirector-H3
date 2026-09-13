# AGENTS.md - Universal Multi-Platform AI Agent Specification

**OmniDirector-H3** is designed to run seamlessly across all major AI Agent frameworks, including **Claude Code**, **OpenAI Codex / ChatGPT**, **Google Antigravity**, and **Cursor / Windsurf / Cline**.

---

## Supported Agent Platforms & Quick Setup

### 1. Anthropic Claude (Claude Code & Claude Projects)
- **Automatic Configuration**: Claude Code automatically loads instructions from [`CLAUDE.md`](./CLAUDE.md).
- **Manual Project Integration**: In Claude Projects or custom instructions, copy and paste the contents of [`SKILL.md`](./SKILL.md).

### 2. OpenAI Codex & ChatGPT Assistants
- **System Prompt / Instruction**:
  ```text
  You are an expert director powered by OmniDirector-H3 for MiniMax H3 video generation.
  When writing or editing screenplays and prompts:
  1. Adhere to Mode A (Domestic Chinese) or Mode B (Global English) standards.
  2. Decouple compound actions into single-verb atomic beats (△) to prevent diffusion melting.
  3. Compile prompts into official MiniMax H3 multimodal format with <d>Speaker: "..."</d> tags, millisecond timestamps, and non_diegetic_music: SILENT.
  4. Validate all output with tools/audit_h3_prompts.py.
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
  - For short drama screenplay: Use Mode A (Domestic) or Mode B (Global) templates in templates/.
  - For AI prompts: Follow the official MiniMax H3 multimodal format (<d> tags, timestamps, silent BGM).
  - Run `python3 tools/audit_h3_prompts.py` to verify prompt integrity before finalizing.
  ```

---

## Standardized Agent Tool Invocations

Every compliant AI Agent should invoke the following standardized CLI tools during the production lifecycle:

| Action | CLI Command |
|---|---|
| **Audit H3 Prompts** | `python3 tools/audit_h3_prompts.py --input <path_to_prompts.md>` |
| **Compile Script to H3** | `python3 tools/compile_screenplay_to_h3.py --input <script.md> --output <prompts.md>` |
| **Blender 3D Axis Check** | `blender --background --python tools/blender_proxy_previz.py -- --episode E01 --render` |
