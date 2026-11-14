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
