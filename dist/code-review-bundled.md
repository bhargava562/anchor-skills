---
name: code-review
description: Use when conducting or requesting code reviews, auditing pull requests or git diffs, triaging findings by severity (Critical/Important/Minor), identifying anti-patterns, or verifying test execution before task completion.
---

# Code Review

## 1. Purpose
Conduct rigorous, objective code reviews that catch defects, security vulnerabilities, and architectural violations before code reaches production, backed by mandatory test execution verification.

---

## 2. When to Use & When NOT to Use

### Use When:
* Auditing git diffs, pull requests, or patch files.
* Evaluating work produced by subagents or peers before merging.
* Triaging review comments into Critical, Important, and Minor tiers.
* Validating test execution and exit codes prior to completing a task.

### Do NOT Use When:
* Designing overall system architectures or task plans (use planning-and-architecture).
* Diagnosing unknown bugs or investigating runtime crashes (use systematic-debugging).
* Editing documentation prose or resume text (use english-writing).

---

## 3. Severity Triage Matrix

Every review finding must be classified into one of three explicit severity tiers:

| Severity | Definition | Policy |
| :--- | :--- | :--- |
| **Critical** (P0) | Security flaws, data loss/corruption, broken runtime execution, contract breakage, missing regression tests for bug fixes. | **Blocker**: Must be resolved before merge. |
| **Important** (P1) | Architectural leaks, unhandled edge cases, performance bottlenecks, inadequate test coverage, poor error propagation. | **Must Fix**: Address before merge or record explicit tracking issue. |
| **Minor** (P2) | Naming clarity, non-blocking style inconsistencies, comment typos, minor readability improvements. | **Advisory**: Optional polish; does not block completion. |

---

## 4. Red Flags Table

Instantly reject or flag the following code smells during review:

| Red Flag Pattern | Operational Risk | Required Remediation |
| :--- | :--- | :--- |
| **Silent Error Swallowing** (`catch (e) {}`) | Masks fatal runtime failures | Log error context and rethrow or return typed Result. |
| **Hardcoded Secrets / URLs** | Credential leak, environment fragility | Extract to validated environment configuration. |
| **Unbounded Queries / Loops** | N+1 database queries, OOM crashes | Add pagination, batching, and query indexes. |
| **Untested Branches** | Silent logic regressions | Add automated unit or integration tests exercising edge paths. |
| **Boundary Leaks** | Persistence models exposed in API | Introduce dedicated DTOs and mapper functions. |
| **Unsafe Concurrency** | Race conditions, data races | Implement synchronization, atomic types, or immutable state. |
| **Commented-Out Code / TODOs** | Code rot and ambiguous intent | Delete dead code; convert valid TODOs into tracked tasks. |

---

## 5. Verification-Before-Completion Protocol
Never accept or approve code changes based on visual inspection alone:
1. **Execute Tests**: Run the repository's automated test command on the modified code.
2. **Inspect Output**: Verify exit code is 0 and output confirms tests passed.
3. **Verify Coverage**: Ensure newly added logic branches are exercised by passing tests.

---

## 6. Subagent Review & Interaction Workflow
* **Requesting Review**: Present a succinct summary of changes, rationale, list of modified files, and proof of passing test execution.
* **Receiving Review**: Address every finding directly. Fix Critical and Important findings with targeted commits; provide empirical justification if disputing.
* **Rubric & Overrides**: Detailed review criteria in [review-rubric.md](references/review-rubric.md); repository policies in [overrides.md](overrides.md).

---

# ============================================================
# PROGRESSIVE DISCLOSURE REFERENCES
# ============================================================

## Reference: references/review-rubric.md

# Code Review Rubric & Quality Standards

Use this comprehensive rubric when auditing diffs, evaluating pull requests, conducting subagent reviews, or validating code before task completion.

---

## 1. Review Dimensions

### A. Correctness & Functional Invariants
* Does the code solve the stated requirement without introducing regressions?
* Are boundary conditions handled (empty collections, zero values, off-by-one indices, null/undefined)?
* Are edge cases and failure paths handled gracefully?
* Are state mutations predictable and contained?

### B. Security & Vulnerability Defense
* **Input Validation**: Are external inputs validated against strict schemas before consumption?
* **Injection Defense**: Are database queries parameterized? Are shell commands avoided or strictly sanitized?
* **Authentication & Authorization**: Are identity and permission checks enforced on every sensitive endpoint?
* **Secrets Hygiene**: Are API keys, passwords, private keys, or tokens completely absent from source code and git history?
* **Data Leakage**: Are sensitive PII fields masked in logs and excluded from client-facing responses?

### C. Architecture & Boundary Discipline
* Does the change adhere to layered boundaries (Presentation -> Application -> Domain -> Infrastructure)?
* Do controllers remain thin, delegating business logic to domain services?
* Are dependencies injected via interfaces rather than tightly coupled concrete classes?
* Is there any circular dependency between modules?

### D. Test Quality & Verification
* Does every new feature have automated unit or integration tests?
* Does every bug fix include an automated regression test?
* Are tests deterministic and isolated from external networks and third-party systems?
* Are assertions meaningful (asserting specific state or outputs, not merely asserting `not null` or `true`)?

### E. Performance & Resource Management
* Are database queries bounded with `LIMIT` and pagination?
* Are there any $N+1$ query loops or unindexed lookups?
* Are file handles, database connections, sockets, and streams cleanly closed or disposed of?
* Are memory-intensive operations streaming rather than buffering entire payloads into RAM?

### F. Observability & Maintainability
* Are errors logged with contextual details (tenant ID, request ID, entity ID)?
* Are error messages clear and actionable?
* Are function, variable, and class names self-documenting?
* Is dead, unreachable, or commented-out code eliminated?

---

## 2. Severity Classification Matrix

| Severity Tier | Criteria | Examples | Action Required |
| :--- | :--- | :--- | :--- |
| **Critical (P0)** | Flaws that cause security exposure, data loss/corruption, system crashes, or broken core contracts. | SQL injection, hardcoded credential, unbounded recursion, missing regression test on bug fix, broken build. | **Blocker**: Must be resolved immediately before code can be merged or approved. |
| **Important (P1)** | Architectural violations, missing edge-case handling, inadequate test assertions, performance degradations. | Business logic in controller, missing pagination on query, unhandled promise rejection, poor error propagation. | **Must Fix**: Must be resolved before completion or tracked with an explicit follow-up issue. |
| **Minor (P2)** | Stylistic improvements, non-critical readability enhancements, documentation typos, naming suggestions. | Renaming a local variable for clarity, fixing a markdown typo, minor whitespace or formatting consistency. | **Advisory**: Optional feedback; author may address or defer. Does not block merge. |

---

## 3. Comprehensive Red Flags Catalog

| Red Flag Pattern | Why It Is Dangerous | Immediate Remediation |
| :--- | :--- | :--- |
| `catch (err) {}` (Empty catch block) | Swallows fatal exceptions; causes silent downstream failure. | Log error with stack trace and rethrow or return typed `Result.err`. |
| `SELECT * FROM table` (No limit/filter) | Causes out-of-memory crashes as tables grow in production. | Add explicit column selection, `WHERE` clauses, and pagination limits. |
| Hardcoded environment URLs / keys | Breaks multi-environment deployments and leaks secrets. | Move to validated environment variables (`process.env.VAR` / config module). |
| Mocking the system under test | Tests pass without verifying real implementation behavior. | Mock external dependencies only; test the real unit under test. |
| Bypassing type checker (`any`, `@ts-ignore`) | Neutralizes compiler safety guarantees. | Define explicit types or interfaces representing the payload shape. |
| Commented-out blocks of code | Pollutes diffs and confuses maintainers about intent. | Delete dead code; version control preserves historical code. |

---

## 4. Verification-Before-Completion Protocol

Before any pull request, patch, or agent task is marked complete or approved:

```bash
# Step 1: Run type checking and static analysis
npm run typecheck && npm run lint

# Step 2: Execute automated unit & integration test suite
npm test

# Step 3: Verify test suite exit code and output
echo $LASTEXITCODE # Windows PowerShell: $LASTEXITCODE; POSIX: $?
```

* **Pass Criteria**:
  * Exit code must be `0`.
  * Zero test failures, zero test skips of active suites.
  * Zero lint warnings treated as errors.
* **Prohibition**: An agent must never declare "all tests pass" without executing the command and inspecting the command output.

---

## 5. Subagent Structured Review Format

When a subagent or reviewer posts feedback, structure the review report as follows:

```markdown
### Review Summary
* **Status**: [APPROVED | CHANGES REQUESTED | BLOCKED]
* **Files Inspected**: [List of files]
* **Test Verification**: [Command executed and result]

### Findings

#### [CRITICAL | IMPORTANT | MINOR] Finding Title
* **File**: `path/to/file.ts` (Lines: XX-YY)
* **Problem**: [Clear explanation of defect or risk]
* **Recommendation**:
  ```typescript
  // Suggested replacement code
  ```

### Verification Checklist
* [x] Automated test suite executed and passed (0 failures).
* [x] No secrets or sensitive data exposed.
* [x] Architectural boundaries respected.
```

---

# ============================================================
# LOCAL CONFIGURATION OVERRIDES (overrides.md)
# ============================================================

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
