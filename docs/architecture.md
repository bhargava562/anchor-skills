# Anchor Skills — System Architecture

This document articulates the architecture of **Anchor Skills**, defining how instructions are structured, partitioned into progressive disclosure tiers, decoupled from personal memory, and consumed by AI execution engines.

---

## 1. System Vision: The Five-Box Model

Anchor Skills is a **passive, provider-independent skill library** stored on GitHub. It is **not** an executable software application, a background service, or a custom AI runtime.

The system is governed by five distinct entities:

```text
┌────────────────────────────────┐
│           1. NOTION            │
│       "What is true about      │  CANONICAL PERSONAL MEMORY
│           Bhargava?"           │  (Already built; queried on demand)
└───────────────┬────────────────┘
                │ optional scoped context
                ▼
┌────────────────────────────────┐
│        2. ANCHOR SKILL         │
│     "How should this task      │  MODULAR INSTRUCTION PACKAGE
│         be performed?"         │  (Self-contained markdown workflows)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│           3. GITHUB            │
│      Stores, versions, and     │  PASSIVE LIBRARY & CATALOG
│         organizes skills       │  (No code execution, no daemon)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│        4. AI PROVIDER          │
│       Claude / Gemini /        │  EXECUTION RUNTIME
│          OpenAI, etc.          │  (Discovers, reads & executes skill)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│           5. OUTPUT            │
│    High-quality, validated     │  DELIVERABLE ARTIFACT
│        task deliverable        │
└────────────────────────────────┘
```

External skills (e.g., `obra/superpowers`) plug cleanly into the skill layer as referenced dependencies:

```text
                  YOUR DOMAIN SKILL (e.g., Resume, Coding)
                              ▲
                              │
                    ┌─────────┴─────────┐
                    │                   │
             EXTERNAL BASE SKILL   SHARED SKILLS
             (e.g., Superpowers)   (e.g., OOP, SOLID, Grammar)
```

---

## 2. Why a Passive Skill Library?

Traditional prompt setups fail in one of two ways:
1. **The Giant Master Prompt**: Cramming identity, coding rules, resume guidelines, and hackathon strategies into a massive prompt. Every interaction burns thousands of tokens on irrelevant rules and confuses the AI with context noise.
2. **Ad-hoc Re-prompting**: Manually typing out rules, quality checks, and background details from scratch every session.

Anchor Skills solves this by storing instructions as a **modular tree of skills**. The AI loads only the specific branch relevant to the active task.

---

## 3. Skill Tree & Progressive Disclosure

Each skill is a self-contained directory designed around **progressive disclosure**. The root file contains only the core workflow and contracts, pointing to supporting documentation when deeper context is needed:

```text
skills/resume-generator/
│
├── SKILL.md                 # Primary workflow: triggers, inputs, outputs, rules
│
├── references/              # Deep heuristics (loaded only on demand)
│   ├── jd-analysis.md       # Classification taxonomy for job requirements
│   ├── content.md           # Bullet formulas: Action + Technical Work + Result
│   ├── grammar.md           # Linguistic standards, active voice, tense consistency
│   ├── layout.md            # Typography, spacing tokens, column geometry
│   └── validation.md        # Measurable ATS extraction & formatting checks
│
├── examples/                # High-quality reference inputs & outputs
│   └── sample-output.md
│
└── links/                   # Pointers to external dependencies and shared rules
    ├── shared-skills.md     # Pointers to shared/engineering/solid.md, etc.
    └── external-skills.md   # Pointers to upstream external repositories
```

### Navigating the Tree
When the AI encounters a resume request:
1. It reads `SKILL.md` (Level 1 overview).
2. If it reaches the JD analysis phase, `SKILL.md` instructs:
   > *"Classify terminology following `references/jd-analysis.md`."*
3. The AI reads `references/jd-analysis.md` (Level 2 reference).
4. If it needs to verify engineering bullet structure, it follows the pointer to `shared/engineering/oop.md` (Level 3 shared skill).
5. It **never** reads coding, hackathon, or LinkedIn instructions during a resume task.

---

## 4. Skill Hierarchy Levels (Levels 0–4)

To prevent coupling and maintain strict separation of concerns, skills are organized into five architectural tiers:

| Tier | Category | Role | Example |
| :---: | :--- | :--- | :--- |
| **Level 0** | **Anchor Core Principles** | Foundational system tenets, authority hierarchy, minimum context rule. | `docs/architecture.md`, `docs/design_principles.md` |
| **Level 1** | **Shared Reusable Knowledge** | Common engineering and communication standards referenced across skills. | `shared/engineering/solid.md`, `shared/writing/active-voice.md` |
| **Level 2** | **Domain Skills** | Self-contained, task-specific workflow packages. | `skills/resume-generator/`, `skills/hackathon-evaluator/` |
| **Level 3** | **Task-Specific Overlays** | Context-specific rule additions or overrides for a domain. | `skills/resume-generator/overlays/jpmorgan.md` |
| **Level 4** | **Provider Adapters** | Provider-specific delivery files (Claude prompts/tools, Gemini builtins). | `adapters/claude/`, `adapters/gemini/` |

---

## 5. References vs. Dependencies vs. Optional Dependencies

Instructions maintain explicit distinctions between how related resources are connected:

```text
Resume Skill
  ├── [Reference]            → references/grammar.md (advisory linguistic guidelines)
  ├── [Shared Dependency]    → shared/engineering/dry.md (required engineering standard)
  └── [External Dependency]  → superpowers/systematic-debugging (external base skill)
```

1. **Reference (`references/`)**: Internal guidance within the skill package. Provides heuristics, definitions, or rubrics that aid execution.
2. **Shared Dependency (`shared/`)**: A common rule or skill residing elsewhere in Anchor Skills. Referenced by pointer to avoid duplicating text (DRY).
3. **External Dependency (`external/`)**: A skill hosted in an upstream open-source repository (e.g., `obra/superpowers`). Referenced as an external baseline without cloning or forking.

---

## 6. Base + Overlay Model for External Skills

Anchor Skills avoids forking or copying external skills. Instead, it pairs an external base skill with a personal **overlay**:

```text
Upstream Base Skill (e.g., superpowers/systematic-debugging)
                 │
                 ▼
        Personal Overlay (Anchor instructions)
        • Explain root cause before proposing code
        • Verify the fix against edge cases
        • Do not blindly copy-paste snippets
                 │
                 ▼
          Effective Skill (Executed by the AI)
```

### Deterministic Overlay Operations
* **`ADD`**: Appends specific constraints, evidence requirements, or verification steps.
* **`REPLACE`**: Replaces a default tool or methodology with a user-preferred alternative.
* **`RESTRICT`**: Prohibits certain actions (e.g., "Do not auto-commit without review").
* **`PRIORITISE`**: Elevates certain principles above defaults (e.g., "Prioritize maintainability over micro-benchmarks").

### Conflict Resolution Hierarchy
If instructions appear contradictory, the AI resolves precedence deterministically:
$$\text{Global Safety / Security} > \text{User Hard Constraints} > \text{Provider Capability Limits} > \text{Base Skill Defaults}$$

---

## 7. Decoupled Memory & Capability Scoping

Anchor Skills adheres to the **principle of least privilege**. A skill does not automatically inherit ambient personal data.

### Declared Needs in `SKILL.md`
Every skill explicitly declares its resource requirements in its frontmatter:

```yaml
name: resume-generator
description: Creates a targeted, professional 1-page resume for a job description.
capabilities:
  memory: required     # forbidden | optional | required
  web: optional        # forbidden | optional | required
  codebase: forbidden  # forbidden | optional | required
memory_scopes:
  - identity.education
  - experience.backend
  - projects.relevant
  - style.communication
```

* **Memory is optional**: A pure skill (like JSON formatting) declares `memory: forbidden`.
* **Scoped memory access**: The Resume Skill requests only education, backend experience, and relevant projects. It never accesses private personal journals or unrelated hobby notes.

---

## 8. Provider Portability & Adapters

Anchor Skills is completely decoupled from any single AI vendor:

```text
                       Anchor Skill (SKILL.md)
                                  │
                                  ▼
                          Provider Adapter
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
       Claude Adapter       Gemini Adapter       OpenAI Adapter
```

* If you switch from Claude to Gemini or OpenAI, the **core skill instructions never change**.
* The **adapter** merely maps the skill to the provider's native delivery mechanism (e.g., system instructions, custom GPT action schemas, or agent skills directories).

---

## 9. The Role of Antigravity vs. GitHub

* **Antigravity**: The **developer's workbench**. Used to inspect, design, draft, refine, test, and document skills. It is an authoring tool, not a background server.
* **GitHub**: The **library and version history**. Houses the authoritative, structured skill repository (`bhargava562/anchor-skills`).
* **The AI Provider**: The **runtime engine**. Reads the skills directly from the repository or local filesystem and carries out user requests.
