# Task Implementation Plan Template

Use this template to decompose architectural designs and complex features into sequential, bite-sized, testable tasks before modifying any codebase.

---

# Feature / Epic Title: [Feature Name]

## 1. Context & Objectives
* **Goal**: [Clear statement of what this work accomplishes]
* **User Value**: [Why this change is needed and who benefits]
* **Non-Goals**: [Explicit boundaries on what is out of scope]
* **Key Invariants**: [Critical behaviors, security invariants, or API contracts that must remain intact]

---

## 2. File Impact Manifest
List all affected files with exact repository paths. Do not use wildcards or vague directory references.

| Operation | Exact File Path | Responsibility / Purpose |
| :--- | :--- | :--- |
| **Create** | `path/to/new_module.ts` | Implements domain logic for X |
| **Create** | `tests/unit/new_module.spec.ts` | Unit tests for new_module |
| **Modify** | `path/to/existing_service.ts` | Integrates new_module via dependency injection |
| **Delete** | `path/to/deprecated_helper.ts` | Superseded by new_module |

---

## 3. Architecture & Boundary Alignments
* **Layering**: Confirm how Presentation, Application, Domain, and Infrastructure boundaries are respected.
* **Controller Impact**: Ensure HTTP/RPC controllers remain thin; no business logic in entrypoints.
* **Dependencies**: Explicitly identify injected dependencies or external services.
* **ADR Reference**: Link to related Architecture Decision Record (e.g., `docs/adr/0002-cache-invalidation.md`), if applicable.

---

## 4. Sequential Task Breakdown

Decompose the work into discrete, verifiable tasks. Each task should represent an atomic unit of change with an automated test or command that proves success before proceeding to the next task.

---

### Task 1: [Title of First Atomic Task]
* **Files Affected**:
  * `path/to/target_file.ts` (Lines: ~45-80)
  * `tests/unit/target_file.spec.ts`
* **Changes Required**:
  ```typescript
  // Exact interface or code snippet to implement
  export interface TargetContract {
    execute(input: InputPayload): Promise<ResultPayload>;
  }
  ```
* **Step-by-Step Instructions**:
  1. Define the interface contract in `target_file.ts`.
  2. Write unit tests exercising the contract and boundary cases in `target_file.spec.ts`.
  3. Implement the minimal logic to make tests pass.
* **Automated Verification Command**:
  ```bash
  npm test tests/unit/target_file.spec.ts
  # Or: pytest tests/unit/test_target_file.py
  ```
* **Expected Output**:
  ```text
  PASS tests/unit/target_file.spec.ts
  Test Suites: 1 passed, 1 total
  Tests:       4 passed, 4 total
  ```
* **Git Commit**: `feat(scope): implement target contract and unit tests`

---

### Task 2: [Title of Second Atomic Task]
* **Files Affected**:
  * `path/to/consumer_service.ts`
  * `tests/integration/consumer_service.spec.ts`
* **Changes Required**:
  * Wire `TargetContract` into `consumer_service.ts` via constructor dependency injection.
  * Update service call paths without altering outer API contracts.
* **Automated Verification Command**:
  ```bash
  npm test tests/integration/consumer_service.spec.ts
  ```
* **Expected Output**:
  ```text
  PASS tests/integration/consumer_service.spec.ts
  Test Suites: 1 passed, 1 total
  Tests:       3 passed, 3 total
  ```
* **Git Commit**: `refactor(scope): wire target contract into consumer service`

---

## 5. End-to-End Verification Gate
Specify the comprehensive command suite required before marking the feature complete:

```bash
# 1. Typecheck and Lint
npm run typecheck && npm run lint

# 2. Complete Test Suite
npm test

# 3. Integration / Boundary Test
npm run test:e2e
```

* **Pass Criteria**: 0 lint errors, 0 type errors, 100% passing tests, no uncommitted changes outside the manifest.
