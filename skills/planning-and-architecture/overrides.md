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
