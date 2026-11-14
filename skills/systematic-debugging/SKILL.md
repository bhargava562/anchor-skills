---
name: systematic-debugging
description: Use when diagnosing bugs, unexpected failures, test breakages, performance regressions, or production incidents requiring rigorous root-cause analysis before applying fixes.
---

# Systematic Debugging

## 1. Purpose
Eliminate guesswork, trial-and-error edits, and speculative patching. Apply a disciplined 4-phase root-cause investigation that isolates failures through empirical evidence and seals fixes with regression tests.

---

## 2. When to Use & When NOT to Use

### Use When:
* Diagnosing unexpected test failures, crashes, exceptions, or timeouts.
* Investigating subtle logic bugs, state corruption, or race conditions.
* Addressing performance regressions or memory leaks.
* Resolving integration defects across API, database, or service boundaries.

### Do NOT Use When:
* Designing new features or greenfield systems (use planning-and-architecture).
* Conducting structural code reviews on working diffs (use code-review).
* Fixing cosmetic prose or documentation formatting (use english-writing).

---

## 3. The 4-Phase Root-Cause Workflow

```text
┌───────────────────────┐     ┌───────────────────────┐
│ Phase 1: Reproduce    │ ──► │ Phase 2: Gather &     │
│ Deterministic failure │     │ Bisect Evidence       │
└───────────────────────┘     └───────────┬───────────┘
                                          │
┌───────────────────────┐     ┌───────────▼───────────┐
│ Phase 4: Surgical Fix │ ◄── │ Phase 3: Isolate &    │
│ & Regression Test     │     │ Prove Hypothesis      │
└───────────────────────┘     └───────────────────────┘
```

### Phase 1: Problem Characterization & Minimal Reproduction
* Define exact **Expected Behavior** vs. **Actual Behavior**.
* Construct a minimal, deterministic reproduction script or unit test that triggers the defect every time.
* If a bug cannot be reproduced reliably, instrument logging and isolate environment variables before proceeding.

### Phase 2: Evidence Gathering & Bisecting
* Trace execution flow, inputs, outputs, and intermediate state mutations leading to the failure.
* Use binary search or git bisect to isolate the fault domain.
* **Hard Invariant**: Zero production code changes during this phase. Do not guess or apply speculative edits.

### Phase 3: Root Cause Isolation & Hypothesis Proof
* Identify the exact line, state mutation, or contract violation.
* State a falsifiable hypothesis: *"The system fails with error X when input Y causes state Z."*
* Prove the hypothesis empirically using targeted assertions or test harness diagnostics before authoring the fix.

### Phase 4: Targeted Fix & Regression Test
* Apply the minimal, surgical fix addressing the root cause—not just the symptom.
* Verify the automated regression test fails without the fix and passes with it.
* Run the complete test suite to prove zero collateral damage.

---

## 4. Non-Negotiable Invariants
1. **Evidence Before Hypothesis**: Never guess or touch production logic without observable proof.
2. **No Masking**: Never wrap unexplained failures in empty `try/catch` blocks or defensive `null` checks that conceal the true defect.
3. **Regression Test Mandate**: Every bug fix must commit an automated test reproducing the issue.

---

## 5. Checklists & Overrides
* Complete diagnostic procedures: [root-cause-checklist.md](references/root-cause-checklist.md).
* Project-specific diagnostic tools and overrides: [overrides.md](overrides.md).
