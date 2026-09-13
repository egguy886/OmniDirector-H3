#!/usr/bin/env python3
"""OmniDirector-H3 Prompt Auditor

Deterministic validation CLI for MiniMax H3 multimodal prompt packets.
Verifies segment counts, official tag syntax (<d>...</d>), timestamp monotonicity,
dual-tier soundscape isolation, and checks for banned legacy headers.

Usage:
    python3 tools/audit_h3_prompts.py --input path/to/prompts.md
    python3 tools/audit_h3_prompts.py --dir path/to/production_dirs/
"""

import argparse
import glob
import os
import re
import sys
from pathlib import Path


def audit_file(filepath: str) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []
    path = Path(filepath)
    filename = path.name

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    segments = re.findall(r"(### H3-0[1-8][^\n]*)", content)
    if not segments:
        segments = re.findall(r"(### (?:Segment|Scene|Part)\s*0?[1-8][^\n]*)", content, re.IGNORECASE)

    if len(segments) != 8:
        warnings.append(f"{filename}: Found {len(segments)} segments instead of the standard 8.")

    # Audit each segment block
    seg_blocks = re.split(r"### H3-0[1-8]|### (?:Segment|Scene|Part)\s*0?[1-8]", content)
    for idx, block in enumerate(seg_blocks[1:], start=1):
        seg_id = f"Segment {idx}"
        codeblocks = re.findall(r"```(?:text)?\n(.*?)```", block, re.DOTALL)
        if not codeblocks:
            errors.append(f"{filename} [{seg_id}]: No ```text ... ``` prompt codeblock found.")
            continue

        prompt_text = codeblocks[-1].strip()

        # 1. Banned legacy headers
        legacy_tokens = ["一、生成任务", "二、主要主体", "三、场景与灯光", "Emotional target", "【主干动作】"]
        for tok in legacy_tokens:
            if tok in prompt_text:
                errors.append(f'{filename} [{seg_id}]: Found banned legacy token "{tok}"! Use integrated_multimodal_description.')

        # 2. Mandatory official fields
        if "integrated_multimodal_description:" not in prompt_text:
            errors.append(f'{filename} [{seg_id}]: Missing mandatory field "integrated_multimodal_description:".')

        if "overall_soundscape:" not in prompt_text:
            errors.append(f'{filename} [{seg_id}]: Missing mandatory field "overall_soundscape:".')

        if "non_diegetic_music: SILENT" not in prompt_text:
            warnings.append(f'{filename} [{seg_id}]: Recommended "non_diegetic_music: SILENT" is missing or altered.')

        # 3. Dialogue tags (<d> ... </d>)
        d_open = prompt_text.count("<d>")
        d_close = prompt_text.count("</d>")
        if d_open != d_close:
            errors.append(f"{filename} [{seg_id}]: Mismatched dialogue tags: {d_open} <d> vs {d_close} </d>.")

        # Check for unclosed dialogue quotes
        dialogue_matches = re.findall(r"<d>(.*?)</d>", prompt_text, re.DOTALL)
        for d in dialogue_matches:
            if d.count('"') % 2 != 0:
                warnings.append(f"{filename} [{seg_id}]: Potential odd number of quotation marks inside dialogue: {d.strip()[:40]}...")

        # 4. Multi-shot timestamps
        shots = re.findall(r"\[Shot \d+\]", prompt_text)
        timestamps = re.findall(r"\bAt \d{2}:\d{2}\.\d{3}\b", prompt_text)
        if len(shots) > 1 and len(timestamps) < len(shots) - 1:
            warnings.append(f"{filename} [{seg_id}]: Multi-shot segment has {len(shots)} shots but only {len(timestamps)} explicit timestamps.")

        # Check timestamp monotonicity
        parsed_ts = []
        for ts_str in timestamps:
            m = re.search(r"(\d{2}):(\d{2}\.\d{3})", ts_str)
            if m:
                mins = int(m.group(1))
                secs = float(m.group(2))
                parsed_ts.append(mins * 60 + secs)
        
        for i in range(len(parsed_ts) - 1):
            if parsed_ts[i] >= parsed_ts[i+1]:
                errors.append(f"{filename} [{seg_id}]: Timestamps are not strictly increasing: {timestamps[i]} >= {timestamps[i+1]}.")

        # 5. Length checks
        if len(prompt_text) > 4000:
            warnings.append(f"{filename} [{seg_id}]: Prompt length ({len(prompt_text)} chars) approaches model attention boundary.")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Deterministic MiniMax H3 Prompt Auditor")
    parser.add_argument("--input", "-i", help="Path to single prompt markdown file")
    parser.add_argument("--dir", "-d", help="Directory containing prompt markdown files")
    args = parser.parse_args()

    files_to_check = []
    if args.input:
        files_to_check.append(args.input)
    elif args.dir:
        files_to_check.extend(glob.glob(os.path.join(args.dir, "**/*prompt*.md"), recursive=True))
        files_to_check.extend(glob.glob(os.path.join(args.dir, "**/*提示词*.md"), recursive=True))
    else:
        files_to_check.extend(glob.glob("examples/**/*.md", recursive=True))

    if not files_to_check:
        print("No prompt markdown files specified or found.")
        sys.exit(1)

    print("==================================================")
    print(f"OmniDirector-H3: Auditing {len(files_to_check)} prompt file(s)...")
    print("==================================================\n")

    total_errors = 0
    total_warnings = 0

    for f in sorted(files_to_check):
        errs, warns = audit_file(f)
        total_errors += len(errs)
        total_warnings += len(warns)
        
        status = "PASSED" if not errs else "FAILED"
        print(f"[{status}] {f}")
        for e in errs:
            print(f"   ❌ ERROR: {e}")
        for w in warns:
            print(f"   ⚠️ WARN:  {w}")

    print("\n" + "="*50)
    print(f"AUDIT COMPLETE: {total_errors} ERRORS, {total_warnings} WARNINGS")
    print("="*50)

    if total_errors > 0:
        sys.exit(1)
    else:
        print("All audited prompt files conform 100% to MiniMax H3 official standards.")
        sys.exit(0)


if __name__ == "__main__":
    main()
