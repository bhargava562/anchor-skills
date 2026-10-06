# Phase 1 Specification — Reusable English Writing Skill & Resume Consumer

This document specifies the architecture, contracts, reference modules, and execution sequence for **Phase 1 of Anchor Skills**:
* **Milestone 1A**: `skills/english-writing/` (Independent Reusable Language Capability)
* **Milestone 1B**: `skills/resume-generator/` (Domain Consumer Skill)
* **Milestone 1C**: Cross-Skill Integration & Architectural Proof

---

## 1. Architectural Core: Language Layer vs. Domain Layers

Anchor Skills establishes a strict separation of concerns between general language quality and domain-specific document conventions:

```text
resume-generator   ──────────────► english-writing (Language Capability)
email-writing      ──────────────► english-writing
linkedin-writing   ──────────────► english-writing
report-writing     ──────────────► english-writing
```

* **English Writing Skill**: Owns language correctness (grammar, sentence structure, tense, agreement, punctuation) and prose quality (clarity, conciseness, naturalness, meaning preservation). It provides a reusable **language-quality capability**, not domain document standards.
* **Domain Consumer Skills**: Own their respective format, structure, and content rules:
  * `resume-generator`: Sections, 1-page constraints, JD alignment, evidence mapping, layout tokens.
  * `email-writing`: Subject lines, greetings, purpose, calls-to-action, sign-offs.
  * `linkedin-writing`: Hooks, narrative pacing, engagement structure.

### Strict One-Way Dependency
`resume-generator` requires $\rightarrow$ `english-writing`. 
`english-writing` has **zero knowledge** of resumes, emails, or job descriptions. It remains completely decoupled and reusable across future skills.

---

## 2. Milestone 1A: `skills/english-writing/` (v0.1)

### 2.1 Behavior vs. Knowledge Mental Model
The AI model already knows English grammar rules. We are not training the model from scratch.

The English Writing Skill is a **behavioral operating guide**:
* **Without the skill**: An AI tends to rewrite text into inflated corporate buzzwords, often hallucinating claims, altering metrics, and distorting technical precision.
* **With the skill**: The AI diagnoses before editing, adheres to 5 simplified priority rules, enforces Meaning & Claim Invariants, obeys "Do Not Overcorrect" constraints, and consults modular grammar references only on demand.

### 2.2 Directory Structure
```text
skills/english-writing/
├── SKILL.md                         # Portable manifest & behavioral operating guide
├── references/                      # Selective, modular knowledge (Original synthesis)
│   ├── sentence-structure.md        # [v0.1] Simple/compound/complex, clauses, fragments, run-ons, parallel structure
│   ├── verb-system.md               # [v0.1] Main verbs, Auxiliaries (be/have/do), Modals, Tenses, Aspect, Voice
│   └── professional-writing.md      # [v0.1] Clarity, naturalness, conciseness, fluff elimination, tone calibration
│   (v0.2 planned: conditionals.md, verb-patterns.md)
│   (v0.3 planned: phrasal-verbs.md, articles-determiners.md)
├── examples/
│   └── before-after.md              # Real-world benchmark corrections exposing specific error categories
└── tests/
    ├── grammar-pressure.md          # TDD test scenarios: agreement, fragments, auxiliary misuse
    ├── meaning-preservation.md      # TDD test scenarios: technical nouns, metrics, factual freezing
    ├── voice-and-tone.md            # TDD test scenarios: appropriate active vs. valid passive, parallel lists
    └── domain-independence.md       # Proves skill operates on email, LinkedIn, and technical docs without resume bias
```

### 2.3 Synthesis from Raymond Murphy's *English Grammar in Use*
The source grammar book (5th Edition, Cambridge) provides a comprehensive topic map across 145 units. We extract high-leverage structural concepts without reproducing copyrighted textbook content:
* **`sentence-structure.md`**: Focuses on subject-verb agreements, simple vs. compound vs. complex sentences (coordination via coordinating conjunctions *for, and, nor, but, or, yet, so*; subordination via *although, because, since, while, after*), eliminating fragments and comma splices, word order with adverbs (Murphy Units 109–110), and parallel structure.
* **`verb-system.md`**: Dedicated treatment of auxiliary verbs (*be, have, do* for questions, negations, and continuous/perfect aspects from Murphy Units 1–16, 49–52), modal verbs (*can, could, must, should, would* from Units 26–36), tense consistency across clauses, and active vs. passive voice (Units 42–44).
* **`professional-writing.md`**: Prefer direct, clear sentence openings appropriate to the writing context (strictly domain-neutral), trimming wordy padding (*"in order to"*, *"due to the fact that"*), removing empty corporate filler (*"passionate"*, *"results-driven"*), and maintaining generic parallel list structures.

### 2.4 Standard Portable Frontmatter (`SKILL.md`)
```yaml
---
name: english-writing
description: Use when drafting, correcting, rewriting, or reviewing English writing where grammar, sentence structure, clarity, or professional phrasing needs attention.
---
```

### 2.5 Four Predictable Operating Modes
* **Mode A — Grammar Correction**: Fix grammatical, tense, agreement, and punctuation errors. Make the minimum necessary changes to achieve correctness. Zero stylistic rewriting.
* **Mode B — Clarity Improvement**: Fix awkward phrasing, comma splices, run-ons, and fragments. Preserve original sentence length, tone, and vocabulary where valid.
* **Mode C — Professional Rewrite**: Polish sentence structure to clean, natural, professional standards. Eliminate wordiness and filler while strictly safeguarding all facts, technical tools, and metrics.
* **Mode D — Review & Critique**: Diagnose language problems first (explaining root causes), then provide the corrected version.

### 2.6 Meaning & Claim Invariants (Frozen Elements)
The AI is strictly prohibited from altering, exaggerating, or generalizing:
1. **Entities & Names**: People, companies, universities, products, libraries.
2. **Dates & Timelines**: Years, durations, months.
3. **Numbers & Quantitative Metrics**: Percentages, scale, monetary values (e.g., *"decreased latency by 32%"* must never be changed or rounded).
4. **Technical Terminology**: Specific technical nouns (*Spring Boot*, *PostgreSQL*, *Kubernetes*, *JWT*).
5. **Scope of Claims**: *"Assisted with"* must not become *"Architected"*; *"Maintained a service"* must not become *"Spearheaded an enterprise transformation"*.
6. **Relationships & Responsibility**: Do not change who performed an action, who owned it, or the level of responsibility (*"Worked with PostgreSQL"* must not become *"Designed PostgreSQL infrastructure"*; *"Assisted the team"* must not become *"Led the team"*).
7. **Degree of Certainty**: Definite statements must remain definite; qualified statements (*"may indicate"*) must remain qualified.

### 2.7 The "Do Not Overcorrect" Rule
* **If the source text is already grammatically correct and the requested mode is correction, return it unchanged.**
* **Do not change correct writing merely to make it different.**
* **Do not rewrite for style when the requested mode is correction.**
* **Do not replace valid technical terminology with simpler words merely for variety.**
* **Do not manufacture artificial sophistication or corporate buzzwords.**

### 2.8 Nuanced Voice Rule
* Passive voice is grammatically valid and often the correct choice (*"The security patch was deployed at midnight"*).
* **Rule**: Prefer active voice when it improves clarity, conciseness, or when the consuming skill explicitly requests it. Do **not** convert valid passive constructions mechanically.

### 2.9 Simplified 5-Tier Priority Hierarchy
1. **Preserve factual meaning & intent.**
2. **Preserve technical terms, names, numbers, relationships, and scope of claims.**
3. **Correct grammar and sentence structure.**
4. **Improve clarity and naturalness.**
5. **Match the requested tone and formality.**

*Guiding Directive*: **Make the smallest change necessary.**

---

## 3. Milestone 1B: `skills/resume-generator/` (Consumer Skill)

### 3.1 Overview & Dependency Hook
`skills/resume-generator/` is a domain consumer skill that orchestrates resume generation and delegates language quality to `skills/english-writing/`.

### 3.2 Directory Structure
```text
skills/resume-generator/
├── SKILL.md                 # Master workflow: invokes english-writing in Step 5
├── config.yaml              # Visual layout tokens: 1-page 2-col default, 1-col override
├── references/
│   ├── jd-analysis.md       # Terminology classification taxonomy (skills, responsibilities, practices)
│   ├── content.md           # Bullet formulas: Action Verb + Tech Core + Measurable Result
│   ├── layout.md            # Geometry tokens, vertical rhythm, and 1-page budgeting guidelines
│   └── validation.md        # Pre-flight verification checklist (structural, evidence, ATS)
├── examples/
│   ├── sample-jd.md         # Benchmark job description
│   ├── sample-candidate.md  # Verified candidate evidence profile
│   └── sample-output.md     # Validated 1-page resume deliverable
└── links/
    └── dependencies.md      # Declares explicit required pointer to english-writing
```

### 3.3 The Step 5 Pointer Pattern
Inside `skills/resume-generator/SKILL.md`:

```markdown
## Step 5: Writing Quality & Grammar Enforcement

Before finalizing any resume text or bullet points, use:

**REQUIRED SUB-SKILL:** `skills/english-writing/SKILL.md` (Mode C: Professional Rewrite)

Execute the `english-writing` workflow to:
1. Preserve candidate facts, metrics, and technical tools with zero distortion.
2. Enforce active voice and action verbs where appropriate for resume bullets.
3. Enforce strict tense consistency (past tense for previous roles, present for current roles).
4. Enforce parallel grammatical structure across bullets in each section.
5. Eliminate corporate fluff words and passive constructions.

Do NOT duplicate or maintain grammar rules inside `resume-generator`.
```

### 3.4 Precedence Hierarchy & Zero-Fabrication Rule
$$\text{Verified Current Candidate Data} > \text{Explicit User Instruction} > \text{Old Resume Content} > \text{AI Inference}$$
* If a JD demands a skill (e.g., Kubernetes) and the candidate profile lacks verified evidence, Kubernetes **cannot** be added to skills or bullets.

### 3.5 Layout Tokens (`config.yaml`)
* **Default**: 1 Page / 2 Columns (62% primary / 38% secondary).
* **Explicit Override**: 1 Page / 1 Column (Single vertical flow).

---

## 4. Test-Driven Skill Validation Execution Sequence

In accordance with Superpowers' test-driven authoring approach:

1. **Step 1: Contract First**:
   Author `skills/english-writing/SKILL.md` (portable frontmatter, 4 modes, Meaning & Claim Invariants, 5-tier priority hierarchy, do-not-overcorrect rule).
2. **Step 2: Red Phase (Baseline Pressure Scenarios)**:
   Author test scenarios P01 through P07 in `tests/`. Run/observe baseline AI behavior without the skill to identify real failure points and loopholes.
3. **Step 3: Green Phase (Targeted References)**:
   Author original, compact concept cards in:
   * `references/sentence-structure.md`
   * `references/verb-system.md`
   * `references/professional-writing.md`
4. **Step 4: Refine & Verify**:
   Verify that tests P01 through P07 pass invariant-based checks. Verify domain independence (P07) and architecture regression test (P08: zero dependencies on resume).
5. **Step 5: Resume Consumer (Milestone 1B)**:
   Scaffold `skills/resume-generator/`, author `config.yaml`, `references/`, and `SKILL.md` with the Step 5 pointer to `english-writing`.
6. **Step 6: Cross-Skill Integration (Milestone 1C)**:
   Execute the full chain: $\text{Resume} \rightarrow \text{english-writing} \rightarrow \text{Deliverable}$. Verify DRY inheritance.

---

## 5. Definition of Done for Phase 1

- [ ] `skills/english-writing/SKILL.md` is authored with portable frontmatter, 4 modes, Meaning & Claim Invariants, 5-tier priority hierarchy, and do-not-overcorrect rules.
- [ ] `references/sentence-structure.md`, `references/verb-system.md`, and `references/professional-writing.md` contain original, compact concept cards.
- [ ] Tests P01 through P08 pass invariant-based verification.
- [ ] `skills/resume-generator/` is authored with zero duplicated grammar rules, calling `english-writing` via explicit pointer.
- [ ] `config.yaml` provides 1-page 2-col default and 1-col override tokens.
- [ ] Cross-skill composition and DRY inheritance are proven.
