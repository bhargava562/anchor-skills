#!/usr/bin/env bash
# ==============================================================================
# SYNOPSIS
#   Synchronizes skill-shelf skills to standard AI agent discovery directories.
#
# TARGET DIRECTORIES:
#   - Antigravity / Gemini: ~/.gemini/skills/
#   - Claude Code:          ~/.claude/skills/
#   - Codex / OpenCode:     ~/.codex/skills/
#   - Hermes Agent:         ~/.hermes/skills/
#
# USAGE:
#   ./scripts/sync.sh [OPTIONS]
#
# OPTIONS:
#   --link         Create symbolic links (default).
#   --copy         Copy files instead of symlinking.
#   --target NAME  Sync only specific agent (gemini|claude|codex|hermes|all).
#   -h, --help     Show this help message.
# ==============================================================================

set -euo pipefail

MODE="link"
TARGET_FILTER="all"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --link)
      MODE="link"
      shift
      ;;
    --copy)
      MODE="copy"
      shift
      ;;
    --target)
      TARGET_FILTER="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: $0 [--link | --copy] [--target all|gemini|claude|codex|hermes]"
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Error: Skills directory not found at $SKILLS_DIR" >&2
  exit 1
fi

USER_HOME="${HOME:-$(getent passwd "$(whoami)" | cut -d: -f6)}"

declare -A AGENT_TARGETS
AGENT_TARGETS["gemini"]="$USER_HOME/.gemini/skills"
AGENT_TARGETS["claude"]="$USER_HOME/.claude/skills"
AGENT_TARGETS["codex"]="$USER_HOME/.codex/skills"
AGENT_TARGETS["hermes"]="$USER_HOME/.hermes/skills"

echo "======================================================================"
echo "SKILL-SHELF ENVIRONMENT SYNCHRONIZER (POSIX Bash)"
echo "Source: $SKILLS_DIR"
echo "Mode:   $MODE"
echo "======================================================================"

# Find skills containing SKILL.md
SKILL_PATHS=()
for dir in "$SKILLS_DIR"/*; do
  if [[ -d "$dir" && -f "$dir/SKILL.md" ]]; then
    SKILL_PATHS+=("$dir")
  fi
done

if [[ ${#SKILL_PATHS[@]} -eq 0 ]]; then
  echo "No valid skills with SKILL.md found in $SKILLS_DIR"
  exit 0
fi

success_count=0
total_operations=0

for agent in "${!AGENT_TARGETS[@]}"; do
  if [[ "$TARGET_FILTER" != "all" && "$TARGET_FILTER" != "$agent" ]]; then
    continue
  fi

  target_root="${AGENT_TARGETS[$agent]}"
  echo ""
  echo "Target [$agent]: $target_root"
  mkdir -p "$target_root"

  for skill_path in "${SKILL_PATHS[@]}"; do
    skill_name="$(basename "$skill_path")"
    dest="$target_root/$skill_name"
    total_operations=$((total_operations + 1))

    if [[ "$MODE" == "copy" ]]; then
      rm -rf "$dest"
      cp -R "$skill_path" "$dest"
      echo "  [OK] $skill_name -> Copy"
      success_count=$((success_count + 1))
    else
      # Symbolic link
      rm -rf "$dest"
      ln -sfn "$skill_path" "$dest"
      echo "  [OK] $skill_name -> Symlink"
      success_count=$((success_count + 1))
    fi
  done
done

echo ""
echo "----------------------------------------------------------------------"
echo "Synchronization complete: $success_count/$total_operations operations succeeded."
exit 0
