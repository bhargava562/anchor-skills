# Root-Cause Investigation Checklist

Use this comprehensive diagnostic checklist to systematically isolate, prove, and resolve defects without guesswork or trial-and-error patching.

---

## Phase 1: Problem Characterization & Minimal Reproduction Checklist

* [ ] **Exact Error Signature**: Capture full stack traces, error codes, HTTP status, and console/terminal logs.
* [ ] **Expected vs. Actual**: Write down in one explicit sentence:
  * *Expected*: What the system should have done under valid specifications.
  * *Actual*: What the system actually did (crashed, returned wrong payload, timed out).
* [ ] **Environment Verification**:
  * Runtime version (Node.js, Python, Go, Java, etc.)
  * OS and platform differences (Windows line endings `CRLF` vs Linux `LF`, filesystem case-sensitivity)
  * Active environment variables and configuration flags
  * System timezone and locale settings
* [ ] **Input Minimization**:
  * Strip optional fields, query parameters, or extraneous data from the failing request until you have the minimal payload that reproduces the defect.
* [ ] **Deterministic Reproduction Script**:
  * Isolate the failure into a standalone script, CLI command, or automated test case.
  * If the failure is intermittent (flaky), run the reproduction script in a loop (e.g., 50 iterations) to measure frequency and isolate timing dependencies.

---

## Phase 2: Evidence Gathering & Bisecting Checklist

* [ ] **Differential Analysis (What Changed?)**:
  * Inspect recent commits: `git log -p -n 10`
  * Inspect dependency upgrades in lockfiles (`package-lock.json`, `poetry.lock`, `go.sum`).
  * Check infrastructure, database migration, or external API contract changes.
* [ ] **Git Bisect (for Regressions)**:
  ```bash
  git bisect start
  git bisect bad HEAD
  git bisect good <known-working-commit>
  git bisect run <reproduction-test-command>
  ```
* [ ] **Trace Execution & Intermediate State**:
  * Add temporary structured logging or inspect breakpoints immediately preceding the failure point.
  * Verify function inputs, return values, and internal state at each boundary.
  * Confirm assumptions: do not assume a variable has the value you expect—print or assert it.
* [ ] **Strict Disciplinary Rule**:
  * DO NOT touch production implementation code during this phase. Only insert diagnostics or tests.

---

## Phase 3: Root-Cause Isolation & Hypothesis Proof Checklist

* [ ] **Identify the Fault Category**:
  * **State Mutation**: Shared mutable object modified unexpectedly by reference.
  * **Async / Concurrency**: Race condition, unhandled Promise rejection, out-of-order event delivery, deadlock.
  * **Boundary / Off-by-One**: Slice boundaries, loop indices, pagination offsets.
  * **Null / Undefined Handling**: Accessing properties on uninitialized objects or optional fields.
  * **Type Coercion / Serialization**: JSON date serialization, integer vs string mismatch, floating-point precision.
  * **Stale Cache / Invalidation**: Cache key collision, missing eviction on write, outdated TTL.
  * **Error Suppression**: Upstream code swallowing exceptions and returning falsy defaults.
* [ ] **The "5 Whys" Depth Check**:
  * *Why did the request fail?* -> The database returned null for user profile.
  * *Why was user profile null?* -> The cache key had an extra trailing slash.
  * *Why did the cache key have a trailing slash?* -> String concatenation used an un-trimmed path parameter.
  * *Root Cause*: URL path normalization is missing at the route parsing boundary.
* [ ] **Falsifiable Hypothesis Formulation**:
  * Write: *"The bug occurs because [root cause condition]. If I [manipulate variable/state X], the failure will [change/disappear] predictably."*
* [ ] **Hypothesis Proof**:
  * Prove the hypothesis using an assertion or unit test in the test harness BEFORE modifying production code.

---

## Phase 4: Targeted Fix & Regression Test Checklist

* [ ] **Automated Regression Test**:
  * Write an automated test that mirrors the minimal reproduction.
  * Verify: The test **FAILS** against the current codebase.
* [ ] **Surgical Root-Cause Fix**:
  * Apply the minimal necessary change to address the identified root cause.
  * Do not perform tangential refactoring or "clean up" unrelated code in the same commit.
  * Verify: The regression test now **PASSES**.
* [ ] **Blast Radius & Side-Effect Verification**:
  * Run the full unit, integration, and linter test suite across the repository.
  * Verify: Zero existing tests are broken by the fix.
* [ ] **Defensive Invariant Hardening**:
  * Add schema validation or invariant assertions at boundaries to prevent this class of bug from reoccurring silently.
