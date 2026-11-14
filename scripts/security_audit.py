#!/usr/bin/env python3
"""
Security Audit Scanner for skill-shelf repository.

Automated guardrail verifying repository integrity against:
1. Hidden/Obfuscated Text: Zero-width Unicode characters, bidirectional overrides,
   and suspicious HTML comments inside skills/.
2. Prompt Injection Patterns: Case-insensitive instruction hijacking phrases.
3. Dangerous Execution Patterns: Unsanitized remote execution pipes, arbitrary code
   evaluation, destructive commands, and sensitive path access.
4. Hardcoded Secrets: GitHub tokens, OpenAI/Anthropic/Google API keys, and raw Bearer tokens.

Standard library only (re, pathlib, json, sys, unicodedata, argparse).
Exit code:
  0 on clean audit, 1 if security violations are detected.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata
from typing import Any, NamedTuple


class Finding(NamedTuple):
    file_path: str
    line_number: int
    category: str
    rule_name: str
    snippet: str


def _build_signatures() -> dict[str, Any]:
    """
    Constructs signatures dynamically using character codes and string concatenation
    to prevent false positives when this script scans its own source code.
    """
    # 1. Zero-width Unicode characters
    zero_width = {
        chr(0x200B): "Zero-Width Space (U+200B)",
        chr(0x200C): "Zero-Width Non-Joiner (U+200C)",
        chr(0x200D): "Zero-Width Joiner (U+200D)",
        chr(0xFEFF): "Zero-Width No-Break Space / BOM (U+FEFF)",
    }

    # 2. Bidirectional override characters (Trojan Source attack vectors)
    bidi_overrides = {}
    for code in list(range(0x202A, 0x202F)) + list(range(0x2066, 0x206A)):
        bidi_overrides[chr(code)] = f"Bidirectional Override (U+{code:04X})"

    # 3. HTML comment pattern (suspicious when placed inside skills/ playbooks)
    html_comment = re.compile(r"<!--[\s\S]*?-->")

    # 4. Prompt injection & instruction-hijacking signatures (dynamically concatenated)
    _p_ign = "".join(["ign", "ore"])
    _p_dis = "".join(["dis", "regard"])
    _p_byp = "".join(["by", "pass"])
    _p_you = "".join(["you", " are", " now"])
    _p_exf = "".join(["exf", "iltrat"])
    _p_ovr = "".join(["over", "ride"])

    prompt_injections = [
        ("Instruction Reset", re.compile(rf"\b{_p_ign}\s+(?:all\s+)?previous\s+instructions\b", re.IGNORECASE)),
        ("Prior Context Reset", re.compile(rf"\b{_p_ign}\s+all\s+prior\b", re.IGNORECASE)),
        ("System Prompt Bypass", re.compile(rf"\b{_p_dis}\s+(?:the\s+)?system\b", re.IGNORECASE)),
        ("Safety Filter Bypass", re.compile(rf"\b{_p_byp}\s+(?:all\s+)?safety\b", re.IGNORECASE)),
        ("Persona Hijack", re.compile(rf"\b{_p_you}\b", re.IGNORECASE)),
        ("Data Exfiltration Command", re.compile(rf"\b{_p_exf}\w*\b", re.IGNORECASE)),
        ("Rule Override Directive", re.compile(rf"\b{_p_ovr}\s+(?:all\s+)?rules\b", re.IGNORECASE)),
    ]

    # 5. Dangerous execution signatures (remote execution, code eval, destructive commands)
    _e_curl = "".join(["cu", "rl"])
    _e_wget = "".join(["wg", "et"])
    _e_iex = "".join(["Invoke", "-Expression"])
    _e_eval = "".join(["ev", "al"])
    _e_b64 = "".join(["base", "64"])
    _e_rmrf = "".join(["r", "m"])
    _e_dels = "".join(["d", "el"])

    dangerous_exec = [
        ("Remote Script Pipe (curl)", re.compile(rf"\b{_e_curl}\b[^\n|]*\|\s*(?:ba|z|da)?sh\b", re.IGNORECASE)),
        ("Remote Script Pipe (wget)", re.compile(rf"\b{_e_wget}\b[^\n|]*\|\s*(?:ba|z|da)?sh\b", re.IGNORECASE)),
        ("Arbitrary Evaluation (iex)", re.compile(rf"\b{_e_iex}\b|\bIEX\b")),
        ("Arbitrary Evaluation (eval)", re.compile(rf"\b{_e_eval}\s*\(")),
        ("Obfuscated Payload Decode (b64)", re.compile(rf"\b{_e_b64}\s+-(?:d|-decode)\b", re.IGNORECASE)),
        ("Root Filesystem Deletion (rm)", re.compile(rf"\b{_e_rmrf}\s+-(?:rf|fr)\s+/(?:\s|$)", re.IGNORECASE)),
        ("Recursive Force Delete (del)", re.compile(rf"\b{_e_dels}\s+/(?:[sS]\s+/[qQ]|[qQ]\s+/[sS])\b")),
    ]

    # 6. Sensitive path access signatures (host keyrings, cloud configs, secrets files)
    _s_ssh = "".join(["~/", r"\.s", "sh"])
    _s_aws = "".join(["~/", r"\.a", "ws"])
    _s_env = "".join([r"\.", "env"])
    _s_cred = "".join(["credentials", r"\.json"])

    sensitive_paths = [
        ("Sensitive Path Access (ssh)", re.compile(rf"{_s_ssh}\b")),
        ("Sensitive Path Access (aws)", re.compile(rf"{_s_aws}\b")),
        ("Sensitive File Access (env)", re.compile(rf"(?<!process\.)(?<!\$)(?<!\w){_s_env}(?:\.[a-zA-Z0-9_-]+)?\b")),
        ("Sensitive File Access (credentials)", re.compile(rf"\b{_s_cred}\b")),
    ]

    # 7. Hardcoded secrets signatures (tokens, private keys, authorization headers)
    _k_ghp = "".join(["gh", "p_"])
    _k_pat = "".join(["github_", "pat_"])
    _k_sk = "".join(["s", "k-"])
    _k_aiza = "".join(["AI", "za"])
    _k_bearer = "".join(["Bea", "rer"])

    secret_patterns = [
        ("Hardcoded GitHub Token (classic)", re.compile(rf"\b{_k_ghp}[a-zA-Z0-9]{{36}}\b")),
        ("Hardcoded GitHub Fine-Grained PAT", re.compile(rf"\b{_k_pat}[a-zA-Z0-9_]{{22,}}\b")),
        ("Hardcoded Provider API Key", re.compile(rf"\b{_k_sk}(?:ant-)?[a-zA-Z0-9]{{20,}}\b")),
        ("Hardcoded Google API Key", re.compile(rf"\b{_k_aiza}[0-9A-Za-z-_]{{30,40}}\b")),
        ("Hardcoded Bearer Token", re.compile(rf"\b{_k_bearer}\s+([^\s\"'`<>]{{20,}})")),
    ]

    return {
        "zero_width": zero_width,
        "bidi_overrides": bidi_overrides,
        "html_comment": html_comment,
        "prompt_injections": prompt_injections,
        "dangerous_exec": dangerous_exec,
        "sensitive_paths": sensitive_paths,
        "secret_patterns": secret_patterns,
    }


def _is_doc_or_governance(rel_path: str) -> bool:
    """
    Checks if a file is documentation, repository governance, or architecture guidance
    where security concepts, policies, and prohibited patterns are legitimately documented.
    """
    norm = rel_path.replace("\\", "/")
    if norm.startswith("docs/"):
        return True
    if norm in {"SECURITY.md", "AGENTS.md", "README.md", "INDEX.md"}:
        return True
    return False


def _is_scanner_script(rel_path: str) -> bool:
    """Identifies this audit scanner script to prevent self-referential false positives."""
    norm = rel_path.replace("\\", "/")
    return norm.endswith("scripts/security_audit.py") or norm == "security_audit.py"


def _is_example_secret(snippet: str) -> bool:
    """
    Determines if a matched secret pattern is an illustrative documentation example,
    placeholder token, template variable, or non-sensitive dummy string.
    """
    placeholders = [
        "<YOUR_",
        "<YOUR-",
        "YOUR_TOKEN",
        "YOUR_FINE_GRAINED_TOKEN",
        "EXAMPLE",
        "PLACEHOLDER",
        "${",
        "$GITHUB_TOKEN",
        "$NOTION",
        "xxx",
        "XXX",
        "...",
    ]
    return any(p in snippet for p in placeholders)


def scan_file(file_path: Path, repo_root: Path, sigs: dict[str, Any]) -> list[Finding]:
    """
    Scans a single file against all security rules with contextual boundary awareness.
    """
    try:
        rel_path = str(file_path.relative_to(repo_root)).replace("\\", "/")
    except ValueError:
        rel_path = str(file_path).replace("\\", "/")

    findings: list[Finding] = []

    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = file_path.read_text(encoding="latin-1")
        except Exception as e:
            return [Finding(rel_path, 1, "SCAN_ERROR", "Unreadable File", str(e))]
    except Exception as e:
        return [Finding(rel_path, 1, "SCAN_ERROR", "Read Error", str(e))]

    lines = content.splitlines()
    is_skills_dir = rel_path.startswith("skills/")
    is_docs = _is_doc_or_governance(rel_path)
    is_self = _is_scanner_script(rel_path)

    # -------------------------------------------------------------------------
    # 1. Hidden / Obfuscated Text: Zero-Width Characters & Bidirectional Overrides
    # -------------------------------------------------------------------------
    for line_idx, line in enumerate(lines, start=1):
        for char, desc in sigs["zero_width"].items():
            if char in line:
                findings.append(Finding(
                    rel_path, line_idx, "HIDDEN_TEXT", desc,
                    f"Forbidden zero-width character detected (U+{ord(char):04X})"
                ))
        for char, desc in sigs["bidi_overrides"].items():
            if char in line:
                findings.append(Finding(
                    rel_path, line_idx, "OBFUSCATION", desc,
                    f"Forbidden bidirectional Trojan Source character detected (U+{ord(char):04X})"
                ))

    # Suspicious HTML comments inside skills/ playbooks
    if is_skills_dir:
        for match in sigs["html_comment"].finditer(content):
            line_no = content[:match.start()].count("\n") + 1
            raw_comment = match.group(0)
            snippet = raw_comment if len(raw_comment) <= 60 else raw_comment[:57] + "..."
            findings.append(Finding(
                rel_path, line_no, "SUSPICIOUS_COMMENT", "HTML Comment inside skills/", snippet
            ))

    # -------------------------------------------------------------------------
    # 2. Prompt Injection Patterns (Case-insensitive instruction hijacking)
    # -------------------------------------------------------------------------
    # Enforced strictly across skills/ and executable scripts.
    # Docs/governance and the scanner itself are contextually exempt from self-triggering on pattern names.
    if not is_docs and not is_self:
        for line_idx, line in enumerate(lines, start=1):
            for rule_name, pattern in sigs["prompt_injections"]:
                if pattern.search(line):
                    snippet = line.strip()
                    if len(snippet) > 80:
                        snippet = snippet[:77] + "..."
                    findings.append(Finding(
                        rel_path, line_idx, "PROMPT_INJECTION", rule_name, snippet
                    ))

    # -------------------------------------------------------------------------
    # 3. Dangerous Execution Patterns (Remote execution, eval, destructive commands)
    # -------------------------------------------------------------------------
    if not is_self:
        for line_idx, line in enumerate(lines, start=1):
            for rule_name, pattern in sigs["dangerous_exec"]:
                if pattern.search(line):
                    snippet = line.strip()
                    if len(snippet) > 80:
                        snippet = snippet[:77] + "..."
                    findings.append(Finding(
                        rel_path, line_idx, "DANGEROUS_EXECUTION", rule_name, snippet
                    ))

    # Sensitive Path Access (~/.ssh, ~/.aws, .env, credentials.json)
    # In skills/ playbooks and runtime scripts, touching sensitive paths is forbidden.
    # In governance/docs (SECURITY.md, AGENTS.md, checklist), enumerating prohibited paths is policy.
    if not is_docs and not is_self:
        for line_idx, line in enumerate(lines, start=1):
            for rule_name, pattern in sigs["sensitive_paths"]:
                if pattern.search(line):
                    snippet = line.strip()
                    if len(snippet) > 80:
                        snippet = snippet[:77] + "..."
                    findings.append(Finding(
                        rel_path, line_idx, "SENSITIVE_PATH", rule_name, snippet
                    ))

    # -------------------------------------------------------------------------
    # 4. Hardcoded Secrets (Tokens, Keys, Authorization Headers)
    # -------------------------------------------------------------------------
    for line_idx, line in enumerate(lines, start=1):
        for rule_name, pattern in sigs["secret_patterns"]:
            match = pattern.search(line)
            if match:
                snippet = line.strip()
                # If in docs/governance, verify if it is an example/placeholder
                if is_docs and _is_example_secret(snippet):
                    continue
                # For Bearer tokens specifically, ignore shell variable expressions like $TOKEN or ${TOKEN}
                if "Bearer" in rule_name:
                    token_val = match.group(1).strip()
                    if token_val.startswith(("$", "${", "<", "{", "[")) or _is_example_secret(token_val):
                        continue
                if len(snippet) > 80:
                    snippet = snippet[:77] + "..."
                findings.append(Finding(
                    rel_path, line_idx, "HARDCODED_SECRET", rule_name, snippet
                ))

    return findings


def discover_files(repo_root: Path) -> list[Path]:
    """
    Discovers all target files (.md, .py, .sh, .ps1) excluding .git, dist/, and scratch/.
    """
    target_extensions = {".md", ".py", ".sh", ".ps1"}
    excluded_dirs = {".git", "dist", "scratch", "__pycache__", ".pytest_cache", "node_modules"}

    valid_files: list[Path] = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        # Check if any parent directory is excluded
        if any(part in excluded_dirs for part in path.parts):
            continue
        if path.suffix.lower() in target_extensions:
            valid_files.append(path)

    return valid_files


def run_audit(repo_root: Path, verbose: bool = False, as_json: bool = False) -> int:
    """
    Executes the full repository security audit.
    Returns: 0 if clean, 1 if violations found.
    """
    sigs = _build_signatures()
    files = discover_files(repo_root)

    all_findings: list[Finding] = []

    for file_path in files:
        file_findings = scan_file(file_path, repo_root, sigs)
        all_findings.extend(file_findings)

    if as_json:
        results = {
            "total_files_scanned": len(files),
            "total_violations": len(all_findings),
            "passed": len(all_findings) == 0,
            "findings": [
                {
                    "file": f.file_path,
                    "line": f.line_number,
                    "category": f.category,
                    "rule": f.rule_name,
                    "snippet": f.snippet,
                }
                for f in all_findings
            ],
        }
        print(json.dumps(results, indent=2))
        return 0 if len(all_findings) == 0 else 1

    # Standard human-readable terminal report
    print("=" * 72)
    print("SKILL-SHELF SECURITY AUDIT SCANNER")
    print(f"Target Root:    {repo_root.resolve()}")
    print(f"Files Scanned:  {len(files)}")
    print("=" * 72)

    if not all_findings:
        print("\n[PASS] 0 security violations detected. Repository is clean.\n")
        return 0

    print(f"\n[FAIL] {len(all_findings)} security violation(s) detected:\n")
    for f in all_findings:
        print(f"  {f.file_path}:{f.line_number}: [{f.category}] {f.rule_name}")
        print(f"      Snippet: {f.snippet}\n")

    return 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Security Audit Scanner for skill-shelf (zero-width chars, injections, execution, secrets)."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Path to repository root (defaults to current directory)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose scanning progress",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format",
    )

    args = parser.parse_args()
    repo_root = Path(args.root).resolve()

    if not repo_root.is_dir():
        print(f"Error: Target path '{repo_root}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    exit_code = run_audit(repo_root, verbose=args.verbose, as_json=args.json)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
