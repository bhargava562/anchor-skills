#!/usr/bin/env python3
"""
Bundle script for skill-shelf.

Bundles each skill in skills/ into a standalone, self-contained markdown file:
    dist/<name>-bundled.md

Includes:
1. Primary orchestration manifest (SKILL.md)
2. All progressive disclosure references (references/*.md)
3. Any static assets/templates (assets/*.md)
4. Local customization overlay (overrides.md)

Designed for copy-pasting into mobile or web chat interfaces (ChatGPT, Claude web,
Grok, Meta AI) where MCP servers or local filesystem access are unavailable.

Standard library only (zero external dependencies).
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def bundle_skill(skill_dir: Path, dist_dir: Path) -> Path | None:
    """Bundles a single skill directory into dist/<name>-bundled.md."""
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        print(f"Skipping '{skill_name}': No SKILL.md found.", file=sys.stderr)
        return None

    try:
        skill_content = skill_md.read_text(encoding="utf-8").strip()
    except Exception as e:
        print(f"Error reading SKILL.md in '{skill_name}': {e}", file=sys.stderr)
        return None

    sections: list[str] = [skill_content]

    # 1. References (references/*.md)
    ref_dir = skill_dir / "references"
    if ref_dir.is_dir():
        ref_files = sorted(ref_dir.glob("*.md"))
        if ref_files:
            sections.append(
                "\n\n---\n\n"
                "# ============================================================\n"
                "# PROGRESSIVE DISCLOSURE REFERENCES\n"
                "# ============================================================"
            )
            for ref_file in ref_files:
                try:
                    ref_text = ref_file.read_text(encoding="utf-8").strip()
                    sections.append(
                        f"\n\n## Reference: references/{ref_file.name}\n\n"
                        f"{ref_text}"
                    )
                except Exception as e:
                    print(f"Warning: Failed to read {ref_file}: {e}", file=sys.stderr)

    # 2. Assets (assets/*.md)
    asset_dir = skill_dir / "assets"
    if asset_dir.is_dir():
        asset_files = sorted(asset_dir.glob("*.md"))
        if asset_files:
            sections.append(
                "\n\n---\n\n"
                "# ============================================================\n"
                "# TEMPLATES & ASSETS\n"
                "# ============================================================"
            )
            for asset_file in asset_files:
                try:
                    asset_text = asset_file.read_text(encoding="utf-8").strip()
                    sections.append(
                        f"\n\n## Asset Template: assets/{asset_file.name}\n\n"
                        f"{asset_text}"
                    )
                except Exception as e:
                    print(f"Warning: Failed to read {asset_file}: {e}", file=sys.stderr)

    # 3. Overrides (overrides.md)
    overrides_md = skill_dir / "overrides.md"
    if overrides_md.is_file():
        try:
            overrides_text = overrides_md.read_text(encoding="utf-8").strip()
            sections.append(
                "\n\n---\n\n"
                "# ============================================================\n"
                "# LOCAL CONFIGURATION OVERRIDES (overrides.md)\n"
                "# ============================================================\n\n"
                f"{overrides_text}"
            )
        except Exception as e:
            print(f"Warning: Failed to read overrides.md in '{skill_name}': {e}", file=sys.stderr)

    bundle_content = "".join(sections) + "\n"
    out_file = dist_dir / f"{skill_name}-bundled.md"
    out_file.write_text(bundle_content, encoding="utf-8")
    return out_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bundle skill-shelf skills into standalone markdown files for web/mobile chat paste."
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=None,
        help="Path to skills directory (default: <repo_root>/skills)",
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        default=None,
        help="Path to output dist directory (default: <repo_root>/dist)",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    skills_dir = args.skills_dir if args.skills_dir else repo_root / "skills"
    dist_dir = args.dist_dir if args.dist_dir else repo_root / "dist"

    if not skills_dir.is_dir():
        print(f"Error: Skills directory not found at: {skills_dir}", file=sys.stderr)
        return 1

    dist_dir.mkdir(parents=True, exist_ok=True)

    skill_folders = sorted([d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])

    if not skill_folders:
        print(f"No skill folders found in {skills_dir}")
        return 0

    print("=" * 70)
    print("SKILL-SHELF BUNDLER (Standalone Web / Mobile Distributions)")
    print(f"Source Directory: {skills_dir}")
    print(f"Output Directory: {dist_dir}")
    print("=" * 70)

    bundled_count = 0
    for skill_dir in skill_folders:
        out_path = bundle_skill(skill_dir, dist_dir)
        if out_path and out_path.is_file():
            bundled_count += 1
            line_count = len(out_path.read_text(encoding="utf-8").splitlines())
            byte_size = out_path.stat().st_size
            rel_out = out_path.relative_to(repo_root)
            print(f"[BUNDLED] {skill_dir.name:<25} -> {rel_out} ({line_count} lines, {byte_size:,} bytes)")

    print("-" * 70)
    print(f"Summary: Successfully bundled {bundled_count}/{len(skill_folders)} skills into {dist_dir.relative_to(repo_root)}/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
