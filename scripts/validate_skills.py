#!/usr/bin/env python3
"""
Validation script for skill-shelf adhering to agentskills.io standard.

Checks:
1. agentskills.io YAML frontmatter:
   - Proper '---' bounding delimiters.
   - 'name' field present, lowercase hyphenated, exactly matching folder name.
   - 'description' field present, non-empty, and <= 1024 characters.
2. SKILL.md line count constraints:
   - < 120 lines for all new skills.
   - <= 500 lines for legacy english-writing.
3. Relative link integrity:
   - All relative links and images in SKILL.md, references/*.md, assets/*.md,
     and overrides.md resolve to existing files.
4. Presence of overrides.md in every skill directory.

Exit code:
  0 on success, 1 on validation error.
Standard library only (zero external dependencies).
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request

# Lowercase alphanumeric hyphen-separated regex (agentskills.io naming)
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Markdown link pattern: [text](target "title") or ![alt](target)
# Handles optional title, angle brackets, and url encoded chars
MD_LINK_PATTERN = re.compile(
    r"!?\[([^\]]*)\]\((<?)([^\)\s>]+)(>?)(?:\s+[\"'][^\"']*[\"'])?\)"
)

LEGACY_SKILLS = {"english-writing"}
LEGACY_LINE_LIMIT = 500
NEW_SKILL_LINE_LIMIT = 120  # strictly < 120 lines (i.e. <= 119)
MAX_DESCRIPTION_LENGTH = 1024


def parse_frontmatter(content: str) -> tuple[dict[str, str], list[str], int]:
    """
    Extracts simple key-value YAML frontmatter bounded by '---'.
    Returns: (frontmatter_dict, body_lines, frontmatter_line_count)
    """
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines, 0

    closing_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_idx = i
            break

    if closing_idx == -1:
        return {}, lines, 0

    fm_lines = lines[1:closing_idx]
    data: dict[str, str] = {}
    current_key: str | None = None
    current_val_lines: list[str] = []

    def flush_key():
        nonlocal current_key, current_val_lines
        if current_key:
            val = " ".join(current_val_lines).strip()
            # Strip surrounding quotes if present
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            data[current_key] = val
        current_key = None
        current_val_lines = []

    for line in fm_lines:
        match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
        if match and not line.startswith(" "):
            flush_key()
            current_key = match.group(1).strip()
            rest = match.group(2).strip()
            if rest in (">", "|", ">-", "|-"):
                pass  # Block scalar indicator, subsequent indented lines contain content
            elif rest:
                current_val_lines.append(rest)
        elif current_key and (line.startswith(" ") or line.startswith("\t")):
            current_val_lines.append(line.strip())
        elif not line.strip() and current_key:
            pass

    flush_key()
    return data, lines[closing_idx + 1:], closing_idx + 1


def check_relative_links(md_path: Path, repo_root: Path) -> list[str]:
    """Checks relative links within a markdown file. Returns list of error messages."""
    errors = []
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Could not read {md_path.relative_to(repo_root)}: {e}"]

    for line_no, line in enumerate(content.splitlines(), start=1):
        for match in MD_LINK_PATTERN.finditer(line):
            target = match.group(3).strip()

            if not target:
                continue

            # Skip web external URLs and non-file schemes
            if target.startswith(("http://", "https://", "mailto:", "ftp://", "tel:", "data:")):
                continue

            # In-page anchor only
            if target.startswith("#"):
                continue

            # Handle file:// URIs (e.g. Antigravity IDE markdown links)
            if target.startswith("file://"):
                parsed_url = urllib.parse.urlparse(target)
                file_path_str = urllib.request.url2pathname(parsed_url.path)
                target_path = Path(file_path_str).resolve()
                if target_path.exists():
                    continue
                # If absolute host path does not exist, try resolving the relative suffix against skill dir
                parts = Path(file_path_str).parts
                found_match = False
                for idx in range(len(parts)):
                    candidate_rel = Path(*parts[idx:])
                    candidate_path = (md_path.parent / candidate_rel).resolve()
                    if candidate_path.exists():
                        found_match = True
                        break
                if found_match:
                    continue
                rel_md = md_path.relative_to(repo_root)
                errors.append(
                    f"Broken file URI in {rel_md}:{line_no} -> '{target}' (resolved to non-existent: {target_path})"
                )
                continue

            # Separate file path from anchor
            file_part, _, _ = target.partition("#")
            if not file_part:
                continue

            # URL decode in case of spaces, %20, etc.
            decoded_file_part = urllib.parse.unquote(file_part)

            # Target is relative to the directory of the current markdown file
            resolved = (md_path.parent / decoded_file_part).resolve()

            # Fallback: check relative to repo root if path starts with slash or matches repo structure
            if not resolved.exists():
                alt_resolved = (repo_root / decoded_file_part.lstrip("/\\")).resolve()
                if alt_resolved.exists():
                    resolved = alt_resolved

            if not resolved.exists():
                rel_md = md_path.relative_to(repo_root)
                errors.append(
                    f"Broken relative link in {rel_md}:{line_no} -> '{target}' (resolved to non-existent: {resolved})"
                )

    return errors


def validate_skill(skill_dir: Path, repo_root: Path) -> tuple[bool, list[str], list[str]]:
    """
    Validates an individual skill folder.
    Returns: (is_valid, errors, warnings)
    """
    errors: list[str] = []
    warnings: list[str] = []
    skill_name = skill_dir.name

    # 1. Directory naming check
    if not SKILL_NAME_PATTERN.match(skill_name):
        errors.append(f"Directory name '{skill_name}' must be lowercase alphanumeric kebab-case.")

    # 2. Check SKILL.md existence
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"Missing mandatory entry point 'SKILL.md' in '{skill_name}'")
        return False, errors, warnings

    try:
        content = skill_md.read_text(encoding="utf-8")
    except Exception as e:
        errors.append(f"Failed to read SKILL.md in '{skill_name}': {e}")
        return False, errors, warnings

    lines = content.splitlines()
    line_count = len(lines)

    # 3. Line count limit
    if skill_name in LEGACY_SKILLS:
        if line_count > LEGACY_LINE_LIMIT:
            errors.append(
                f"Legacy skill '{skill_name}' SKILL.md has {line_count} lines (must be <= {LEGACY_LINE_LIMIT})."
            )
    else:
        if line_count >= NEW_SKILL_LINE_LIMIT:
            errors.append(
                f"New skill '{skill_name}' SKILL.md has {line_count} lines (strict limit: < {NEW_SKILL_LINE_LIMIT} lines)."
            )

    # 4. YAML Frontmatter check
    fm, body, fm_lines = parse_frontmatter(content)
    if fm_lines == 0 or not fm:
        errors.append(f"SKILL.md in '{skill_name}' is missing valid YAML frontmatter bounded by '---'.")
    else:
        # Frontmatter 'name'
        fm_name = fm.get("name", "").strip()
        if not fm_name:
            errors.append(f"Frontmatter in '{skill_name}/SKILL.md' is missing 'name'.")
        elif fm_name != skill_name:
            errors.append(
                f"Frontmatter 'name: {fm_name}' does not match directory name '{skill_name}'."
            )
        elif not SKILL_NAME_PATTERN.match(fm_name):
            errors.append(f"Frontmatter name '{fm_name}' must be lowercase alphanumeric kebab-case.")

        # Frontmatter 'description'
        fm_desc = fm.get("description", "").strip()
        if not fm_desc:
            errors.append(f"Frontmatter in '{skill_name}/SKILL.md' is missing 'description'.")
        else:
            desc_len = len(fm_desc)
            if desc_len > MAX_DESCRIPTION_LENGTH:
                errors.append(
                    f"Description length ({desc_len} chars) exceeds maximum allowed {MAX_DESCRIPTION_LENGTH} chars."
                )

    # 5. Presence of overrides.md
    overrides_md = skill_dir / "overrides.md"
    if not overrides_md.is_file():
        errors.append(f"Missing mandatory 'overrides.md' in '{skill_name}'.")

    # 6. Relative link integrity for all markdown files in skill
    for md_file in sorted(skill_dir.rglob("*.md")):
        link_errors = check_relative_links(md_file, repo_root)
        errors.extend(link_errors)

    is_valid = len(errors) == 0
    return is_valid, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate skill-shelf skills against agentskills.io and repository standards."
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=None,
        help="Path to skills directory (default: <repo_root>/skills)",
    )
    args = parser.parse_args()

    # Determine repository root (assumes scripts/ is directly inside repo root)
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    skills_dir = args.skills_dir if args.skills_dir else repo_root / "skills"
    if not skills_dir.is_dir():
        print(f"Error: Skills directory not found at: {skills_dir}", file=sys.stderr)
        return 1

    skill_folders = sorted([d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])

    if not skill_folders:
        print(f"No skill folders found in {skills_dir}")
        return 0

    print("=" * 70)
    print("SKILL-SHELF VALIDATION SUITE (agentskills.io Standard)")
    print(f"Skills Directory: {skills_dir}")
    print(f"Skills Detected:  {len(skill_folders)}")
    print("=" * 70)

    total_skills = len(skill_folders)
    passed_skills = 0
    total_errors: list[str] = []

    for skill_dir in skill_folders:
        skill_name = skill_dir.name
        is_valid, errors, warnings = validate_skill(skill_dir, repo_root)

        skill_md = skill_dir / "SKILL.md"
        line_info = ""
        if skill_md.is_file():
            try:
                line_count = len(skill_md.read_text(encoding="utf-8").splitlines())
                limit_str = f"<= {LEGACY_LINE_LIMIT}" if skill_name in LEGACY_SKILLS else f"< {NEW_SKILL_LINE_LIMIT}"
                line_info = f"({line_count} lines, limit: {limit_str})"
            except Exception:
                pass

        if is_valid:
            passed_skills += 1
            print(f"[PASS] {skill_name} {line_info}")
        else:
            print(f"[FAIL] {skill_name} {line_info}")
            for err in errors:
                print(f"       ERROR: {err}")
                total_errors.append(f"[{skill_name}] {err}")

        for warn in warnings:
            print(f"       WARN:  {warn}")

    print("-" * 70)
    print(f"Summary: {passed_skills}/{total_skills} skills passed.")

    if total_errors:
        print(f"Validation FAILED with {len(total_errors)} error(s).")
        return 1

    print("Validation PASSED: All skills conform to agentskills.io standard.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
