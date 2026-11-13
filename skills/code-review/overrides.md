# Code Review — Project Overrides

This file defines repository-specific overrides and configuration rules for the `code-review` skill. Rules defined here take precedence over defaults in `SKILL.md`.

---

## 1. Project Static Analysis & Lint Commands

* **Typecheck Command**: [e.g., `npm run typecheck` or `mypy src/`]
* **Linter Command**: [e.g., `npm run lint` or `ruff check .`]
* **Formatter Command**: [e.g., `npm run format:check` or `prettier --check .`]

---

## 2. Test Coverage & Severity Thresholds

* **Minimum Test Coverage**: [e.g., 80% line coverage for new code in domain and service layers]
* **Zero Critical Findings**: No PR may merge with unresolved Critical (P0) or Important (P1) findings.
* **Regression Test Mandate**: Any PR addressing an issue marked `bug` must include an automated regression test.

---

## 3. Review Exclusion Paths

The following paths are excluded from strict style and test coverage audits:
* `dist/`, `build/`, `out/` (Compiled artifacts)
* `*.generated.ts`, `*_pb2.py` (Code generator outputs)
* Database migration scripts (audited for safety, excluded from unit test requirements)
