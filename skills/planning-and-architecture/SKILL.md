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
