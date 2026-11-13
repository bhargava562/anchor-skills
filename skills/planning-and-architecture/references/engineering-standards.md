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
