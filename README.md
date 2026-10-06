# Anchor Skills (`skill-shelf`)

> **A passive, provider-independent library of modular AI skills, workflows, and personal overlays.**

---

## 1. Project Identity & Purpose

**Anchor Skills** is a portable collection of reusable AI skills and task workflows stored as clean, structured markdown packages on GitHub.

When interacting with modern AI environments (Claude, Gemini, OpenAI/ChatGPT, Kimi, etc.), a user repeatedly has to re-explain:
* Who they are and their background
* What rules, quality standards, and constraints the AI must follow
* How to approach recurring tasks (resumes, coding, code reviews, technical research, brainstorming)

Anchor Skills solves this fragmentation by treating skills as **passive, modular knowledge packages**:

```text
┌──────────────┐
│    NOTION    │
│ (Already     │  "What is true about Bhargava?"
│   built)     │  Personal Memory / Context Layer
└──────┬───────┘
       │ (optional query on demand)
       ▼
┌──────────────┐
│ ANCHOR SKILL │  "How should this task be performed?"
│   LIBRARY    │  Modular, portable instructions & workflows
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    GITHUB    │  Passive storage, catalog, and version history
│ (Repository) │  (Does NOT run code or execute a server)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ AI PROVIDER  │  The actual execution engine
│ Claude/Gemini│  Discovers and reads the required skill,
│ OpenAI, etc. │  follows its workflow, and uses native tools
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    OUTPUT    │  Verified, high-quality task deliverable
└──────────────┘
```

> [!IMPORTANT]
> **Anchor Skills is NOT an application or a custom runtime.**
> We are **not** building a Python/Java backend, a PDF-generation server, a custom vector DB, or a middleware agent.
> **GitHub is simply a passive skill shelf.** The native AI provider is the runtime that discovers, loads, and executes the markdown instructions.

---

## 2. Why OOP, SOLID, and DRY for Skill Instructions?

In Anchor Skills, **Object-Oriented Programming (OOP), SOLID, and DRY principles are applied to organize instruction sets and documentation**—not to build software applications.

Without software engineering discipline, AI knowledge repos quickly turn into:
* A giant, noisy master prompt where every task loads irrelevant rules and wastes context tokens.
* Copied-and-pasted external skills that become impossible to maintain.
* Conflicting instructions scattered across random markdown files.

Anchor Skills applies engineering rigor to prompt and skill design:

| Principle | Meaning in Skill Instruction Architecture |
| :--- | :--- |
| **Abstraction** | The main `SKILL.md` defines *what* the task does, its workflow, triggers, inputs, and outputs—without dumping hundreds of lines of reference minutiae into one file. |
| **Encapsulation & Progressive Disclosure** | Each skill is a self-contained folder. Deep heuristics live in `references/`, examples in `examples/`, and pointers in `links/`. The AI loads only what is necessary for the current task. |
| **Composition & Overlays** | External skills (e.g., `obra/superpowers`) are reused directly as dependencies. Personal rules are attached as lightweight **overlays** (`ADD`, `REPLACE`, `RESTRICT`, `PRIORITISE`) rather than forking upstream files. |
| **Polymorphism & Portability** | The core skill instructions remain provider-agnostic. Provider-specific delivery files (Claude commands, Gemini builtins) adapt the skill without rewriting the core workflow. |
| **Dependency Inversion** | Skills declare the capabilities they need (`memory: optional`, `web: optional`, `tools: [filesystem]`). They never hardcode vendor-specific APIs or concrete storage systems. |
| **DRY (Don't Repeat Yourself)** | Shared knowledge (e.g., core OOP principles, grammar standards, research guidelines) is stored once in shared reference skills and linked via pointers, never duplicated across skills. |
| **Single Responsibility (SRP)** | Each document has one distinct purpose: `SKILL.md` guides execution flow; `references/grammar.md` defines linguistic rules; `references/jd-analysis.md` classifies job description terms. |

---

## 3. Skill Tree & Progressive Disclosure

The repository functions as a navigable knowledge tree. The AI does **not** ingest the entire repository into its prompt:

```text
                     ANCHOR SKILLS
                          │
                    Skill Catalog
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
  Resume Generator    Hackathon         Coding
         │
         ├── SKILL.md (Core Workflow & Input/Output Contracts)
         ├── references/
         │   ├── jd-analysis.md (Taxonomy of skills & expectations)
         │   ├── content.md     (Action + Technical Work + Result)
         │   ├── grammar.md     (Tense, active voice, parallel rules)
         │   └── layout.md      (Geometry, vertical rhythm tokens)
         ├── examples/
         └── links/
             ├── shared-skills.md   (Pointers to common principles)
             └── external-skills.md (Pointers to Superpowers, etc.)
```

When a user asks:
> *"Create a resume for this Stripe Job Description."*

The AI:
1. Discovers and opens `skills/resume-generator/SKILL.md`.
2. Inspects its declared needs (requires JD + candidate memory; web search optional; codebase not needed).
3. Reads only the necessary reference documents (e.g., `references/jd-analysis.md`, `references/grammar.md`) when executing those specific steps.
4. Leaves unrelated domains (coding, hackathons, LinkedIn) completely untouched.

---

## 4. Documentation Index

The full system architecture, instruction design rules, and phase roadmaps are documented in the [docs/](file:///d:/skill-shelf/docs) directory:

| Document | Description |
| :--- | :--- |
| [docs/architecture.md](file:///d:/skill-shelf/docs/architecture.md) | Passive skill library architecture, Notion brain integration, skill tree hierarchy (Levels 0–4), progressive disclosure, and provider adapters. |
| [docs/design_principles.md](file:///d:/skill-shelf/docs/design_principles.md) | How OOP, SOLID, DRY, and clean architecture govern instruction organization, prompt tokens, and reference pointers. |
| [docs/phase_1_resume_generator.md](file:///d:/skill-shelf/docs/phase_1_resume_generator.md) | Complete specification for Phase 1: the `resume-generator` skill package, reference documents, 1-analysis / 1-fix workflow, and layout tokens. |
| [docs/roadmap.md](file:///d:/skill-shelf/docs/roadmap.md) | Incremental delivery roadmap for building, organizing, and linking skills across the repository. |

---

## 5. Current Milestone: Phase 1 — Resume Generator Skill

Phase 1 focuses on designing and validating the first complete, self-contained skill package: **Resume Generator**.

```text
Job Description (JD)
       +
Candidate Memory (from Notion Brain)
       +
Optional Old Resume (Historical artifact)
       +
Layout Configuration (1-page 2-col default / 1-col override)
       │
       ▼
skills/resume-generator/SKILL.md
       │
       ├── Progressive reference loading (references/jd-analysis.md, references/grammar.md)
       ├── One-Analysis Pass (Generates consolidated Issue Manifest)
       ├── One-Correction Pass (Direct targeted fixes)
       ├── Zero-Fabrication Rule (Candidate evidence outranks all inference)
       └── Measurable ATS & Layout Guidelines (references/layout.md)
       │
       ▼
High-Quality, Professional 1-Page Resume
```

---

## 6. Repository Layout (Target Structure)

```text
skill-shelf/
├── README.md                           # Root catalog & library architecture
├── docs/                               # System architecture & design guidelines
│   ├── architecture.md
│   ├── design_principles.md
│   ├── phase_1_resume_generator.md
│   └── roadmap.md
├── shared/                             # Level 1: Shared reusable knowledge & rules
│   ├── engineering/
│   │   ├── oop.md
│   │   ├── solid.md
│   │   └── dry.md
│   └── writing/
│       ├── grammar.md
│       └── active-voice.md
├── skills/                             # Level 2: Domain skill packages
│   └── resume-generator/               # Phase 1 skill package
│       ├── SKILL.md
│       ├── config.yaml
│       ├── references/
│       │   ├── jd-analysis.md
│       │   ├── content.md
│       │   ├── grammar.md
│       │   ├── layout.md
│       │   └── validation.md
│       ├── examples/
│       └── links/
└── adapters/                           # Level 4: Provider-specific delivery definitions
    ├── claude/
    ├── gemini/
    └── openai/
```
