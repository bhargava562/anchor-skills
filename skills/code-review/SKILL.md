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
