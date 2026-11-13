# Systematic Debugging — Project Overrides

This file defines repository-specific overrides and configuration rules for the `systematic-debugging` skill. Rules defined here take precedence over defaults in `SKILL.md`.

---

## 1. Project Diagnostic Commands

* **Single Test Execution**: [e.g., `npm test -- -t "test name"` or `pytest -k "test_name"`]
* **Verbose / Debug Output**: [e.g., `DEBUG=* npm test` or `pytest -vv --capture=no`]
* **Debugger Invocation**: [e.g., `node --inspect-brk ...` or `python -m pdb ...`]

---

## 2. Regression Test Conventions

* **Test Location**: [e.g., Place regression tests in `tests/regression/` or adjacent to unit tests `*.spec.ts`]
* **Naming Standard**: [e.g., `test_issue_<number>_<description>.py` or `<feature>.regression.spec.ts`]
* **Test Isolation**: All regression tests must execute in isolation without requiring external network connectivity.

---

## 3. Allowed Loggers & Diagnostic Tools

* [Specify allowed logging frameworks and required cleanup rules for diagnostic logs before PR submission]
