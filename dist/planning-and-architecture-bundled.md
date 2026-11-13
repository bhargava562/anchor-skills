---
name: planning-and-architecture
description: Use when designing software architectures, breaking complex features into actionable implementation plans, authoring Architecture Decision Records (ADRs), or establishing system boundaries and contracts before writing code.
---

# Planning and Architecture

## 1. Purpose
Define clear system architectures, establish clean module boundaries, document technical decisions, and produce granular, testable task implementation plans before writing production code.

---

## 2. When to Use & When NOT to Use

### Use When:
* Architecting new systems, modules, or services.
* Breaking down large epics or ambiguous user requests into bite-sized, sequential tasks.
* Making high-impact technical choices requiring an Architecture Decision Record (ADR).
* Defining data contracts, interfaces, and boundary layers between components.

### Do NOT Use When:
* Fixing a localized single-line bug or minor typo (use systematic-debugging).
* Brainstorming raw product ideas or feature validation (use brainstorm-and-validate).
* Reviewing completed diffs or pull requests (use code-review).

---

## 3. Core Architectural Principles
* **SOLID Principles**: Enforce Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.
* **Clean Boundaries**: Strict separation between Presentation/API, Application/Service, Domain, and Persistence/Infrastructure layers.
* **Thin Controllers**: Controllers and HTTP handlers handle only routing, request validation, and status mapping. All domain logic resides in isolated domain services or entities.
* **Explicit Contracts**: Define data schemas, DTOs, and interface signatures before implementing behavior.
* Full standards reference: [engineering-standards.md](references/engineering-standards.md).

---

## 4. Architecture Decision Records (ADRs)
When introducing architectural trade-offs, new dependencies, or irreversible structural changes:
1. Document context, constraints, and decision drivers.
2. Evaluate at least two viable alternatives with explicit pros/cons.
3. State the chosen outcome, rationale, and consequences (positive and negative).
4. Use the canonical template: [adr-template.md](assets/adr-template.md).

---

## 5. Implementation Planning Workflow
Before touching code, decompose work into an actionable plan:
1. **Context & Invariants**: Define the goal, non-goals, and invariants that must not break.
2. **File Impact Manifest**: Explicitly enumerate files to create, modify, or delete.
3. **Bite-Sized Task Breakdown**:
   * Each task must be scoped to an atomic, verifiable unit of work.
   * Specify **exact file paths** and target line ranges or functions.
   * Include exact code snippets, signatures, or diff specifications.
   * Provide an **automated verification command** (e.g., `npm test path/to/spec.ts`, `pytest tests/test_foo.py`).
   * Define expected command output and commit message.
4. Structure plans using: [task-plan-template.md](references/task-plan-template.md).

---

## 6. Overrides & Project Adaptations
Check [overrides.md](overrides.md) for repository-specific framework conventions, test runner preferences, and architectural invariants.

---

# ============================================================
# PROGRESSIVE DISCLOSURE REFERENCES
# ============================================================

## Reference: references/engineering-standards.md

# Engineering Standards & Architectural Principles

This reference defines the technical design standards for systems, module boundaries, and service architectures authored under `planning-and-architecture`.

---

## 1. SOLID Principles in Practice

### Single Responsibility Principle (SRP)
* A module, class, or service must have one, and only one, reason to change.
* Separate business rules from transport mechanisms, serialization formats, and persistence logic.
* **Violation**: A `UserService` that validates passwords, hashes them, writes to PostgreSQL, and sends a welcome email.
* **Correction**: Decompose into `PasswordHasher`, `UserRepository`, `EmailNotifier`, orchestrated by a focused `UserRegistrationService`.

### Open/Closed Principle (OCP)
* Software entities must be open for extension, but closed for modification.
* Introduce new behaviors via polymorphism, strategy patterns, or dependency injection rather than editing existing `if/else` or `switch` blocks.

### Liskov Substitution Principle (LSP)
* Subtypes must be substitutable for their base types without altering program correctness.
* Derived classes must adhere to base type contracts, invariants, and exception specifications.
* Do not throw unexpected exceptions or return incompatible types in derived implementations.

### Interface Segregation Principle (ISP)
* Clients should not be forced to depend upon interfaces they do not use.
* Favor small, focused role interfaces (e.g., `Reader`, `Writer`, `Validator`) over monolithic "god" interfaces.

### Dependency Inversion Principle (DIP)
* High-level modules should not depend on low-level modules; both should depend on abstractions.
* Abstractions should not depend on details; details should depend on abstractions.
* Core domain logic must never import database drivers, cloud SDKs, or transport libraries directly.

---

## 2. Layered Architecture & Boundary Rules

```text
┌────────────────────────────────────────────────────────┐
│           Presentation Layer (Controllers, CLI)        │
│    Thin controllers: routing, schema validation, HTTP  │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│           Application Layer (Use Cases, Services)      │
│    Workflow orchestration, transaction management      │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│           Domain Layer (Entities, Value Objects)       │
│    Pure business rules, domain invariants, zero IO    │
└───────────────────────────┬────────────────────────────┘
                            ▲
┌───────────────────────────┴────────────────────────────┐
│           Infrastructure Layer (DB, APIs, Filesystem)  │
│    Implements domain interfaces, external adapters     │
└────────────────────────────────────────────────────────┘
```

### Thin Controllers Rule
* Controllers, route handlers, and CLI commands must remain strictly thin:
  * Parse and validate incoming payloads against strict schemas.
  * Delegate business operations to application services or domain handlers.
  * Map domain results or typed errors to HTTP/protocol status codes.
  * **Never** execute database queries, external API calls, or business calculations inside a controller.

### Domain Purity
* Domain entities and value objects must have zero external dependencies on frameworks, ORMs, or network libraries.
* Entities validate their own internal invariants upon creation and mutation.

---

## 3. Data Contracts & Schema Hygiene
* **Schema Validation at Boundaries**: Validate all external inputs (HTTP requests, message queues, disk files) at the system perimeter before passing data to internal layers.
* **Explicit DTOs**: Never expose internal database entities or ORM models directly through external API endpoints.
* **Typed Errors**: Use explicit error hierarchies or Result types (`Result<T, E>`) rather than throwing generic strings or untyped exceptions.

---

## 4. Testing Hierarchy & Verification Standards
1. **Unit Tests**:
   * Test pure domain logic and isolated components.
   * Zero network calls, zero database calls, zero filesystem dependencies.
   * Execution time: sub-second.
2. **Integration Tests**:
   * Verify interactions across module boundaries (e.g., repositories against test database containers, API client against mock servers).
   * Focus on contract adherence and serialization boundaries.
3. **End-to-End (E2E) Tests**:
   * Smoke test critical user paths through real or staging infrastructure.
   * Kept lean and targeted to prevent slow, flaky test suites.

## Reference: references/task-plan-template.md

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

---

# ============================================================
# TEMPLATES & ASSETS
# ============================================================

## Asset Template: assets/adr-template.md

# Architecture Decision Record (ADR) Template

# ADR-[NUMBER]: [SHORT TITLE OF DECISION]

* **Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]
* **Date**: [YYYY-MM-DD]
* **Deciders**: [List of decision makers and stakeholders]
* **Technical Domain**: [e.g., Storage, Authentication, Caching, Messaging]

---

## 1. Context & Problem Statement
Describe the architectural context, problem, and operational reality driving this decision.
* What is the current technical limitation or challenge?
* What changed in requirements, scale, or constraints?
* What are the specific non-functional requirements (latency, throughput, cost, developer velocity)?

---

## 2. Decision Drivers
List the key forces and constraints shaping the choice:
1. [Driver 1, e.g., Must support 10,000 writes/sec without distributed deadlocks]
2. [Driver 2, e.g., Must maintain sub-50ms p99 read latency]
3. [Driver 3, e.g., Must avoid vendor lock-in for data storage]
4. [Driver 4, e.g., Team familiarity and operational overhead]

---

## 3. Considered Options

### Option 1: [Option Name, e.g., PostgreSQL with Partitioning]
* **Overview**: Brief description of this approach.
* **Pros**:
  * [Advantage 1]
  * [Advantage 2]
* **Cons**:
  * [Disadvantage 1]
  * [Disadvantage 2]

### Option 2: [Option Name, e.g., DynamoDB / NoSQL Document Store]
* **Overview**: Brief description of this approach.
* **Pros**:
  * [Advantage 1]
  * [Advantage 2]
* **Cons**:
  * [Disadvantage 1]
  * [Disadvantage 2]

---

## 4. Decision Outcome
* **Chosen Option**: [Option Name]
* **Justification**:
  [Explain why this option best addresses the decision drivers above. Acknowledge trade-offs explicitly.]

---

## 5. Consequences & Trade-offs

### Positive Consequences
* [Benefit 1: e.g., Simplified local development and testing environment]
* [Benefit 2: e.g., ACID transactions guaranteed across account balances]

### Negative Consequences & Risks
* [Trade-off 1: e.g., Requires manual sharding strategy once table exceeds 2TB]
* [Mitigation 1: e.g., Partition by tenant_id from inception]

---

## 6. Compliance & Verification
How will we verify that code adheres to this decision over time?
* [e.g., Linter rule forbidding direct database queries outside the repository package]
* [e.g., Automated integration test verifying query latency under simulated load]

---

# ============================================================
# LOCAL CONFIGURATION OVERRIDES (overrides.md)
# ============================================================

# Planning and Architecture — Project Overrides

This file defines repository-specific overrides and configuration rules for the `planning-and-architecture` skill. Rules defined here take precedence over defaults in `SKILL.md`.

---

## 1. Project-Specific Stack & Conventions

* **Primary Language / Runtime**: [e.g., TypeScript / Node.js 20+ or Python 3.11+]
* **Framework Pattern**: [e.g., Clean Architecture, NestJS modular, FastAPI domain services]
* **Default Test Runner**: [e.g., `npm test`, `pnpm test`, `pytest -v`]
* **ADR Directory**: [e.g., `docs/adr/`]

---

## 2. Architecture Boundary Overrides

* [Specify any custom layer definitions or forbidden cross-layer imports]
* [Example: Controllers in `src/interfaces/http` may never directly import from `src/infrastructure/db`]
* [Example: All external HTTP clients must implement `HttpClient` interface]

---

## 3. Plan Granularity Rules

* **Task Duration**: Tasks must be scoped to atomic operations executable and verifiable within 15 minutes.
* **Verification Command Standard**: Every task must include an executable CLI command; manual browser testing alone is unacceptable.
