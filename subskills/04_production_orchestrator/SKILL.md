---
name: omni-director-production-orchestrator
description: Unattended batch scheduling, off-peak discount window daemon, resumable checkpointing, and multi-backend API production execution.
---

# Sub-Skill 04: Production Orchestrator

## Purpose
Rendering an entire 10-episode micro-drama season requires generating 80 discrete 15-second high-resolution video clips ($80 \times 15s = 1,200s$ of finished film). Doing this manually through web interfaces is error-prone, exhausting, and wastes platform discount windows (e.g. 50% off compute between 00:01:00 and 08:00:00).

This sub-skill provides an enterprise-grade autonomous batch orchestrator with precision wake-up timers, OS anti-sleep locks, resumable JSON state machines, exponential backoff retries, and automated asset payload construction.

---

## Core Principles

### 1. Off-Peak Discount Window Timing Lock
- Many cloud GPU clusters (AutoDL, RunPod, etc.) and model API providers offer heavy discounts during off-peak hours (e.g., 00:01:00 to 08:00:00).
- The orchestrator calculates the exact sleep duration down to the second, locks the machine with `caffeinate` (macOS) or systemd inhibitions (Linux), and wakes up precisely at 00:01:00.
- Hard cutoff at 08:00:00 stops dispatching new tasks to avoid full-price billing.

### 2. Resumable State Machine (`batch_progress.json`)
- Every clip transitions through strict states:
  $$\text{PENDING} \longrightarrow \text{SUBMITTING} \longrightarrow \text{RUNNING} \longrightarrow \text{COMPLETED} \mid \text{FAILED}$$
- If a network drop, system reboot, or rate limit occurs, running the orchestrator again seamlessly resumes from the last unfinished segment. Zero redundant GPU spend.

### 3. Automated Reference Asset Packaging
- Automatically parses prompt dependencies.
- Encodes scene reference PNGs, character face portraits, and voice WAV files into Base64 buffers or presigned S3 URLs on the fly.
- Maps speaker voice tokens to clean 32kHz reference audio tracks.

### 4. Post-Production Auto-Assembly
- As clips finish rendering, the orchestrator:
  1. Downloads and validates MP4 containers (ffprobe header check).
  2. Extracts keyframes at $t = 0.5s, 7.5s, 14.5s$ for automated contact-sheet generation.
  3. Concatenates 8 clips into a single 120-second continuous episode cut via headless ffmpeg.
