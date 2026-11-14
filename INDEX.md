# Skill Shelf: Master Intent-to-Skill Routing Index

> **Instant intent-to-skill resolution table for AI agents and human operators.**
> This index enables zero-shot skill discovery, preserving token budget through 2-tier progressive disclosure.

---

## 1. How to Use This Index

When an agent receives a user request, it must **not** load all skills into context. Instead:
1. **Match Intent**: Locate the user's core intent in the [Master Routing Table](#2-master-routing-table).
2. **Load Entry Point**: Fetch only the target `SKILL.md` (<120 lines) into context.
3. **Progressive Disclosure**: Read linked documents in `references/` or `assets/` only when executing specific phases requiring deep heuristics.
4. **Apply Overrides**: Inspect `overrides.md` in the skill folder for project- or user-specific constraints.

---

## 2. Master Routing Table

| Skill Name | Domain | Primary Triggers & Intent Patterns | Entry Point | Key Sub-Resources | Primary Output Deliverable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`core-thinking`** | Cognitive | First-principles decomposition, evaluating complex trade-offs, making architectural or product decisions, preemptive failure mode analysis, structured analytical reasoning, clarifying ambiguity. | [`skills/core-thinking/SKILL.md`](skills/core-thinking/SKILL.md) | `references/mental-models.md`<br>`overrides.md` | Decision matrix with weighted criteria, explicit failure modes, and high-density recommendation. |
| **`brainstorm-and-validate`** | Cognitive / Product | Ideating new features or ventures, stress-testing concepts, 4-step wedge discovery, competitor / ROI gating, narrowing ambiguous problems, interactive specification via one-question-at-a-time loop. | [`skills/brainstorm-and-validate/SKILL.md`](skills/brainstorm-and-validate/SKILL.md) | `references/discovery-framework.md`<br>`references/validation-rubric.md`<br>`overrides.md` | Validated wedge proposal, competitor moat analysis, or structured product spec. |
| **`planning-and-architecture`** | Engineering | System design, technical architecture, component boundaries, applying SOLID/Clean Code, writing Architecture Decision Records (ADRs), generating bite-sized testable task plans with exact file paths and commands. | [`skills/planning-and-architecture/SKILL.md`](skills/planning-and-architecture/SKILL.md) | `references/task-plan-template.md`<br>`references/engineering-standards.md`<br>`assets/adr-template.md`<br>`overrides.md` | Formatted ADR, component interface diagrams, and phased execution plan with test verifications. |
| **`systematic-debugging`** | Engineering | Triaging bugs, fixing failing tests, diagnosing unexpected runtime behaviors, analyzing stack traces, reproducing intermittent errors, verifying fixes before committing. | [`skills/systematic-debugging/SKILL.md`](skills/systematic-debugging/SKILL.md) | `references/root-cause-checklist.md`<br>`overrides.md` | 4-phase root-cause analysis, reproduction script/test, validated surgical fix, and regression test. |
| **`code-review`** | Engineering | Inspecting git diffs or pull requests, subagent work verification, code quality audits, detecting architectural leaks and security bugs, severity triage (Critical, Important, Minor), test suite verification. | [`skills/code-review/SKILL.md`](skills/code-review/SKILL.md) | `references/review-rubric.md`<br>`overrides.md` | Structured review report with severity-graded findings, red-flag checklist, and pass/fail verdict. |
| **`english-writing`** | Language / Prose | Drafting, rewriting, or polishing English text, resume bullets, technical documentation, emails, executive memos, fixing grammar/syntax, enforcing active voice and high prose density while freezing factual claims. | [`skills/english-writing/SKILL.md`](skills/english-writing/SKILL.md) | `references/composition-and-prose-craft.md`<br>`references/professional-writing.md`<br>`references/sentence-structure.md`<br>`references/verb-system.md`<br>`overrides.md` | Clear, concise, grammatically flawless prose with 100% preservation of technical and factual claims. |

---

## 3. Detailed Intent Mapping Matrix

Use this matrix to map user conversational prompts directly to the appropriate skill:

| User Utterance / Prompt Scenario | Primary Skill | Secondary Skill (if compound) | Action Flow |
| :--- | :--- | :--- | :--- |
| *"I have this raw idea for a developer tool, but I don't know if it's viable."* | `brainstorm-and-validate` | `core-thinking` | Run 4-step wedge discovery, evaluate competitor moat, and validate ROI before designing architecture. |
| *"We need to decide whether to migrate our monolith to microservices or modular monolith."* | `core-thinking` | `planning-and-architecture` | Apply first-principles decomposition, build a weighted trade-off matrix, surface failure modes upfront, then draft an ADR. |
| *"Write a technical architecture plan to implement OAuth2 PKCE in our React + FastAPI app."* | `planning-and-architecture` | `code-review` | Produce component interface specs, define thin controllers, and generate bite-sized testable tasks with file paths. |
| *"My test is failing with a NullPointerException in payment_worker.go, fix it."* | `systematic-debugging` | — | Halt guessing. Reproduce with minimal test, trace causal chain backwards to root trigger, apply surgical fix, verify zero regression. |
| *"Review this git diff / pull request before I merge it to main."* | `code-review` | `systematic-debugging` | Triage changes into Critical / Important / Minor findings, check red flags (hidden mutations, missing errors, untracked async), verify test coverage. |
| *"Polish this technical design document for leadership review. Make it punchy and professional."* | `english-writing` | — | Activate Mode B/C, eliminate filler words, enforce active verbs, maximize prose economy, and freeze all technical facts. |
| *"A bug was reported in production. After we fix it, we need to update our incident post-mortem."* | `systematic-debugging` | `english-writing` | Phase 1-4 systematic diagnosis and verified repair; then compose post-mortem prose with factual invariants. |
| *"How should we design our database schema for high-throughput multi-tenant billing?"* | `planning-and-architecture` | `core-thinking` | Isolate domain models, evaluate normalization vs denormalization trade-offs, draft ADR with rollback strategies. |
| *"We need an interactive interview to narrow down requirements for our new CLI tool."* | `brainstorm-and-validate` | `planning-and-architecture` | Execute one-question-at-a-time discovery loop, clarify user pain points, lock scope, then hand off to architecture. |

---

## 4. Compound Multi-Skill Pipelines

Complex projects often traverse multiple skills in sequence. Agents should execute these handoffs sequentially, shedding previous reference context to maintain hygiene:

### Pipeline A: Feature Concept to Implementation
```text
┌───────────────────────────┐      ┌───────────────────────────────┐      ┌───────────────────────┐
│ brainstorm-and-validate   ├─────►│ planning-and-architecture     ├─────►│ code-review           │
│ (Wedge, ROI, Scope Gate)  │      │ (ADR, Interfaces, Task Steps) │      │ (Diff audit, Triage)  │
└───────────────────────────┘      └───────────────────────────────┘      └───────────────────────┘
```

### Pipeline B: Incident Triage to Post-Mortem
```text
┌───────────────────────────┐      ┌───────────────────────────────┐      ┌───────────────────────┐
│ systematic-debugging      ├─────►│ code-review                   ├─────►│ english-writing       │
│ (Root Cause, Surgical Fix)│      │ (Regression & Safety Verdict) │      │ (Post-Mortem Prose)   │
└───────────────────────────┘      └───────────────────────────────┘      └───────────────────────┘
```

### Pipeline C: High-Stakes Architecture Decision
```text
┌───────────────────────────┐      ┌───────────────────────────────┐
│ core-thinking             ├─────►│ planning-and-architecture     │
│ (First Principles, Risks) │      │ (Formal ADR & Task Plan)      │
└───────────────────────────┘      └───────────────────────────────┘
```

---

## 5. Skill Directory Layout Reference

```text
skills/
├── core-thinking/
│   ├── SKILL.md                          # Primary entry point (<120 lines)
│   ├── overrides.md                      # Personal/project overlay rules
│   └── references/
│       └── mental-models.md              # First-principles heuristics & matrices
├── brainstorm-and-validate/
│   ├── SKILL.md                          # Primary entry point (<120 lines)
│   ├── overrides.md                      # Personal/project overlay rules
│   └── references/
│       ├── discovery-framework.md        # 4-step wedge discovery methodology
│       └── validation-rubric.md          # Competitor, ROI, & scope gating
├── planning-and-architecture/
│   ├── SKILL.md                          # Primary entry point (<120 lines)
│   ├── overrides.md                      # Personal/project overlay rules
│   ├── assets/
│   │   └── adr-template.md               # Standard Architecture Decision Record
│   └── references/
│       ├── task-plan-template.md         # Phased task execution structure
│       └── engineering-standards.md      # SOLID, Clean Code, boundaries
├── systematic-debugging/
│   ├── SKILL.md                          # Primary entry point (<120 lines)
│   ├── overrides.md                      # Personal/project overlay rules
│   └── references/
│       └── root-cause-checklist.md       # 4-phase causal tracing protocol
├── code-review/
│   ├── SKILL.md                          # Primary entry point (<120 lines)
│   ├── overrides.md                      # Personal/project overlay rules
│   └── references/
│       └── review-rubric.md              # Severity grading & red flags
└── english-writing/
    ├── SKILL.md                          # Primary entry point (legacy core)
    ├── overrides.md                      # Personal/project overlay rules
    ├── examples/
    │   └── before-after.md
    ├── references/
    │   ├── composition-and-prose-craft.md
    │   ├── professional-writing.md
    │   ├── sentence-structure.md
    │   └── verb-system.md
    └── tests/
```

---

## 6. Maintenance & Integrity Checks

To ensure the routing table remains synchronized with the physical repository:
- Run `python scripts/validate_skills.py` after adding or updating any skill.
- Confirm every entry point links to a valid `skills/<name>/SKILL.md`.
- Ensure new skills do not exceed the 120-line ceiling in their primary entry point.
- Ensure every skill directory contains an `overrides.md`.
