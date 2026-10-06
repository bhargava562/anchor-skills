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

External skills (e.g., `obra/superpowers`) and shared skills plug cleanly into the skill layer as referenced dependencies:

```text
                  YOUR DOMAIN SKILL (e.g., Resume, Email, LinkedIn)
                              ▲
                              │
                    ┌─────────┴─────────┐
                    │                   │
             EXTERNAL BASE SKILL   REUSABLE SUB-SKILLS
             (e.g., Superpowers)   (e.g., english-writing)
```

---

## 2. Core Architectural Distinction: Skill vs. Reference

To keep skills clean, maintainable, and token-efficient, we enforce an explicit boundary between **Skills** and **References**:

| Dimension | Skill | Reference |
| :--- | :--- | :--- |
| **Definition** | An active, executable procedure with its own workflow, decision logic, and output. | Passive knowledge, definitions, syntax rules, lookup tables, or checklists. |
| **Structure** | Contains a `SKILL.md` (purpose, triggers, steps, quality checks). | Plain markdown files in `references/` (e.g., `grammar-rules.md`, `jd-analysis.md`). |
| **Execution Flow** | $\text{Input} \rightarrow \text{Analyze} \rightarrow \text{Transform} \rightarrow \text{Validate} \rightarrow \text{Output}$. | Queried on demand by the AI when executing a specific skill step. |
| **Example** | `skills/english-writing/` (actively corrects prose across resumes, emails, and posts). | `references/grammar-rules.md` (passive lookup tables for tenses, punctuation, and voice). |

---

## 3. The Reusable Skill Graph & Direction of Dependency

When a capability is needed across multiple domains (such as writing clear, grammatically correct English), it is structured as an **independent reusable skill**.

### Strict One-Way Dependency
Dependencies in Anchor Skills must flow in one direction from consumer to required capability:

```text
resume-generator   ──────────────► english-writing (Language Capability)
email-writing      ──────────────► english-writing
linkedin-writing   ──────────────► english-writing
report-writing     ──────────────► english-writing
```

* Consumers request `english-writing`.
* `english-writing` knows nothing about those consumers.
* **DRY Guarantee**: Grammar and linguistic rules are maintained in exactly one place, never copy-pasted into multiple domain skills.

### Shallow Dependency Chains
To prevent token bloat and ensure the AI does not lose track of the primary goal, skill chains must remain **shallow** (generally 1 level deep):

$$\text{Resume Generator} \rightarrow \text{English Writing (1 level)}$$

We explicitly prohibit deep 4–5 level chains ($\text{Resume} \rightarrow \text{Writing} \rightarrow \text{Grammar} \rightarrow \text{Language} \rightarrow \text{Rules}$).

---

## 4. Skill Tree & Progressive Disclosure

Each skill is a self-contained directory designed around **progressive disclosure**. The root file contains only the core workflow and contracts, pointing to supporting documentation when deeper context is needed:

```text
skills/resume-generator/
│
├── SKILL.md                 # Primary workflow: triggers, inputs, outputs, rules
│
├── config.yaml              # Visual tokens: 1-page 2-col default, 1-col override
│
├── references/              # Deep heuristics (loaded only on demand)
│   ├── jd-analysis.md       # Classification taxonomy for job requirements
│   ├── content.md           # Bullet formulas: Action + Technical Work + Result
│   ├── layout.md            # Typography, spacing tokens, column geometry
│   └── validation.md        # Measurable ATS extraction & formatting checks
│
├── examples/                # High-quality reference inputs & outputs
│   └── sample-output.md
│
└── links/                   # Pointers to external dependencies and shared sub-skills
    └── dependencies.md      # Declares pointer: REQUIRED SUB-SKILL: english-writing
```

### Navigating the Tree
When the AI encounters a resume request:
1. It reads `skills/resume-generator/SKILL.md` (Level 1 overview).
2. It executes Step 1 (Input Validation) and Step 2 (JD Analysis).
3. At Step 2, it loads `references/jd-analysis.md` on demand to classify skills and responsibilities.
4. At Step 4, it drafts accomplishment bullets using `references/content.md`.
5. At Step 5 (Writing Quality), `SKILL.md` directs:
   > *"Execute REQUIRED SUB-SKILL: `skills/english-writing/SKILL.md`."*
6. The AI invokes `english-writing`, loads its `references/grammar-rules.md`, verifies active voice and tenses, and returns polished text to the resume pipeline.
7. Unrelated domains (coding, hackathon, email) are **never** loaded.

---

## 5. Skill Hierarchy Levels (Levels 0–4)

To prevent coupling and maintain strict separation of concerns, skills are organized into five architectural tiers:

| Tier | Category | Role | Example |
| :---: | :--- | :--- | :--- |
| **Level 0** | **Anchor Core Principles** | Foundational system tenets, authority hierarchy, minimum context rule. | `docs/architecture.md`, `docs/design_principles.md` |
| **Level 1** | **Shared Reusable Skills** | Common cross-cutting workflows used by multiple domain tasks. | `skills/english-writing/` |
| **Level 2** | **Domain Skills** | Self-contained, task-specific workflow packages. | `skills/resume-generator/`, `skills/hackathon-evaluator/` |
| **Level 3** | **Task-Specific Overlays** | Context-specific rule additions or overrides for a domain. | `skills/resume-generator/overlays/jpmorgan.md` |
| **Level 4** | **Provider Adapters** | Provider-specific delivery files (Claude prompts/tools, Gemini builtins). | `adapters/claude/`, `adapters/gemini/` |

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

* **Memory is optional**: A pure skill declares `memory: forbidden`.
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
