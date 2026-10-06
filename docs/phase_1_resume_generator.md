# Phase 1 Specification — Resume Generator & English Writing Skills

This document specifies the design, structure, and execution contracts for **Phase 1: Resume Generator**, which introduces the first two skills in **Anchor Skills**: `skills/english-writing/` and `skills/resume-generator/`.

---

## 1. Architectural Milestone: Two-Skill Composition

Phase 1 proves the core architectural power of Anchor Skills: **modular skill composition and DRY instruction reuse**.

Instead of embedding grammar rules inside the resume skill, we establish two decoupled skills:
1. **`skills/english-writing/`**: A standalone, reusable skill that knows *how to write correct, active, professional English*.
2. **`skills/resume-generator/`**: A domain skill that knows *how to build a targeted, high-impact resume*. It invokes `english-writing` as an explicit sub-skill dependency.

```text
                      english-writing (Skill)
                      ▲       ▲       ▲       ▲
                      │       │       │       │
                      │ (used)│       │       │
                      │       │       │       │
               resume-generator  email   linkedin  reports
```

### The Skill vs. Reference Distinction
* **Make it a Skill** when it has its own active behavior, workflow, triggers, and deliverable:
  * `english-writing` takes input text $\rightarrow$ preserves factual meaning $\rightarrow$ enforces active voice $\rightarrow$ checks tenses $\rightarrow$ returns polished output.
* **Make it a Reference** when it is passive knowledge, syntax, or lookup tables:
  * `grammar-rules.md` is a passive reference module inside `english-writing/references/`.

---

## 2. Directory Structure for Phase 1

```text
skills/
├── english-writing/                 # Independent Reusable Skill
│   ├── SKILL.md                     # Workflow: Meaning preservation -> Tense -> Voice -> Clean text
│   └── references/
│       └── grammar-rules.md         # Passive rules: Tenses, parallel structure, voice, punctuation
│
└── resume-generator/                # Domain Consumer Skill
    ├── SKILL.md                     # Master workflow: Calls english-writing before finalizing text
    ├── config.yaml                  # Layout tokens: 1-page 2-col default, 1-col override, typography
    ├── references/
    │   ├── jd-analysis.md           # Classification taxonomy for requirements & terminology
    │   ├── content.md               # Bullet formulas: Action Verb + Tech Core + Measurable Result
    │   ├── layout.md                # Geometry tokens, vertical rhythm, and 1-page budgeting guidelines
    │   └── validation.md            # Pre-flight verification checklist (structural, evidence, ATS)
    ├── examples/
    │   ├── sample-jd.md             # Benchmark job description
    │   ├── sample-candidate.md      # Verified candidate evidence profile
    │   └── sample-output.md         # Validated 1-page resume deliverable
    └── links/
        └── dependencies.md          # Declares explicit required pointer to english-writing
```

---

## 3. Dependency Direction & Shallow Chains

* **One-Way Dependency**: `resume-generator` depends on `english-writing`. `english-writing` has **zero knowledge** of `resume-generator`.
* **Shallow Chains**: Cross-skill references are strictly **1 level deep**. We avoid deep chains (Resume $\rightarrow$ Writing $\rightarrow$ Grammar $\rightarrow$ Language $\rightarrow$ Rules) that lead to context fragmentation.
* **On-Demand Loading**: During resume generation, the AI does not load `english-writing` at the start. It loads it only when entering Step 5 (Writing Quality & Grammar Check).

### How the Pointer is Declared in `resume-generator/SKILL.md`

```markdown
## Step 5: Writing Quality & Grammar Enforcement

Before finalizing any resume text or bullet points, use:

**REQUIRED SUB-SKILL:** `skills/english-writing/SKILL.md`

Execute the `english-writing` workflow to:
1. Preserve factual candidate meaning with zero distortion.
2. Enforce active voice and strong action verbs.
3. Enforce strict tense consistency (past tense for completed roles, present for current roles).
4. Enforce parallel grammatical structure across bullets in each section.
5. Eliminate corporate fluff words and passive constructions.

Do NOT duplicate or maintain grammar rules inside `resume-generator`.
```

---

## 4. Frozen Requirements & Precedence Hierarchy

The Resume Generator operates on five inputs:

```text
1. Job Description (JD)               [Required]
2. Candidate Memory / Profile         [Required: from Notion Brain]
3. Old Resume                         [Optional: historical artifact]
4. Layout Override                    [Optional: default = 1-page, 2-column]
5. Additional User Instructions       [Optional]
```

### Precedence Hierarchy
$$\text{Verified Current Candidate Data} > \text{Explicit Current User Instruction} > \text{Old Resume Content} > \text{AI Inference}$$

* **Zero Fabrication**: If a JD demands *Kubernetes* and the candidate lacks verified evidence, Kubernetes **cannot** be added to skills or bullets.
* **Old Resume Authority**: Historical resumes provide phrasing and structure cues, but current verified facts always take precedence.

### Layout Configuration Overrides
```text
No explicit layout request   →   Default = 1 Page / 2 Columns (62/38 split)
Explicit "1 page 1 column"   →   Override = 1 Page / 1 Column (Single vertical flow)
```
The content pipeline remains identical; only presentation geometry adapts.

---

## 5. End-to-End Execution Flow

```text
User asks: "Create my resume for this JD"
    │
    ▼
AI loads `skills/resume-generator/SKILL.md`
    │
    ├─► Step 1: Input Validation
    ├─► Step 2: One Comprehensive Analysis
    │           (JD Classification + Evidence Mapping + Conflict Check -> Issue Manifest)
    ├─► Step 3: Resume Content Plan
    ├─► Step 4: Draft Generation (Action + Technical Work + Result)
    │
    ├─► Step 5: Writing Quality Check
    │           └── Loads `skills/english-writing/SKILL.md`
    │               └── Reads `grammar-rules.md` on demand
    │               └── Returns polished, grammatically verified text
    │
    ├─► Step 6: Layout Assembly & Vertical Rhythm Check (config.yaml & references/layout.md)
    └─► Step 7: Pre-Flight Validation (references/validation.md)
    │
    ▼
Deliverable: Verified 1-Page Resume
```

---

## 6. Implementation Sequence

We implement the skills in strict dependency order:

### Stage 1: The Independent Skill (`skills/english-writing/`)
1. Create `skills/english-writing/references/`.
2. Author `references/grammar-rules.md` (passive rule lookup: tenses, parallel structure, voice, punctuation, prohibited fluff).
3. Author `SKILL.md` (active 10-step correction workflow, pointer to `references/grammar-rules.md`).
4. Test `english-writing` in isolation on poorly framed text.

### Stage 2: The Consumer Skill (`skills/resume-generator/`)
5. Create `skills/resume-generator/` scaffolding (`references/`, `examples/`, `links/`).
6. Author `config.yaml` (tokens for margins, typography, 1-page budget, 2-col default, 1-col override).
7. Author `references/jd-analysis.md` (classification taxonomy for requirements & signals).
8. Author `references/content.md` (bullet impact formula, section priorities, zero-fabrication rule).
9. Author `references/layout.md` (margins, vertical rhythm tokens, column ratios, 1-page space budgeting).
10. Author `references/validation.md` (pre-flight verification checklist).
11. Author `links/dependencies.md` (declares pointer to `english-writing`).
12. Author `SKILL.md` (master 7-stage workflow invoking `english-writing` in Step 5).
13. Author `examples/` (`sample-jd.md`, `sample-candidate.md`, `sample-output.md`).

### Stage 3: Verification & Architectural Proof
14. Test default 2-column layout deliverable.
15. Test 1-column layout override deliverable.
16. Test old resume conflict resolution.
17. Verify DRY: Update a grammar rule in `english-writing` and confirm `resume-generator` inherits the change without modification.

---

## 7. Definition of Done (DoD)

- [ ] `skills/english-writing/` is fully authored and discoverable as an independent skill.
- [ ] `skills/english-writing/references/grammar-rules.md` contains comprehensive linguistic rules.
- [ ] `skills/resume-generator/` is authored with zero duplicated grammar rules.
- [ ] `resume-generator/SKILL.md` explicitly references `english-writing` in Step 5.
- [ ] `resume-generator/config.yaml` defines 1-page 2-col default and 1-col override.
- [ ] References in `resume-generator/references/` cover JD analysis, content, layout, and validation.
- [ ] Real benchmark examples exist in `examples/`.
- [ ] Cross-skill composition (Resume $\rightarrow$ English Writing $\rightarrow$ Output) is tested and verified.
