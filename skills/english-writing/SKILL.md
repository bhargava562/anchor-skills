---
name: english-writing
description: Use when drafting, correcting, rewriting, or reviewing English writing where grammar, sentence structure, clarity, or professional phrasing needs attention.
---

# English Writing Skill

## 1. Purpose
Provide a portable, reusable language-quality capability for English writing. This skill diagnoses and corrects grammatical, structural, and stylistic flaws while strictly safeguarding factual truth, technical precision, and claim scope.

---

## 2. When to Use & When NOT to Use

### Use When:
* Drafting, revising, or proofreading text in English (resumes, emails, technical documentation, LinkedIn posts, reports).
* Correcting grammar, tense inconsistencies, subject-verb agreement, and punctuation.
* Resolving awkward sentence constructions, run-ons, comma splices, and fragments.
* Polishing prose for clarity, conciseness, and natural professional tone.
* Performing a language quality check as a sub-skill invoked by a domain workflow.

### Do NOT Use When:
* The task is purely formatting data structures (JSON, YAML, CSV) or source code syntax.
* The user requests creative fiction, humor, or intentional non-standard dialect.
* The text requires domain-specific decisions outside of language quality (e.g., job qualification decisions or resume section allocations—those belong to consuming domain skills).

---

## 3. Runtime Expectations
* **Memory**: Personal memory is not required for general language tasks. Consuming workflows may pass relevant context on demand.
* **Web Search**: Do not browse the web by default. Use external verification only when an explicit instruction requires verifying specialized domain terms or company names.
* **Codebase Access**: Not required unless reviewing documentation or comments embedded directly within source files.

---

## 4. Operating Modes

The skill operates in one of four distinct modes. If no mode is specified, default to **Mode B (Clarity Improvement)**.

| Mode | Objective | Transformation Scope |
| :--- | :--- | :--- |
| **Mode A: Grammar Correction** | Fix grammatical, tense, agreement, and punctuation errors. | **Minimal changes only.** Make only the edits required for grammatical correctness. Zero stylistic restructuring. |
| **Mode B: Clarity Improvement** *(Default)* | Fix awkward phrasing, run-ons, fragments, and poor transitions. | **Moderate targeted edits.** Improve flow and readability while preserving original sentence length, vocabulary, and tone. |
| **Mode C: Professional Rewrite** | Upgrade prose to clear, concise, active professional standards. | **Controlled restructuring.** Eliminate wordiness and filler while strictly locking all facts, metrics, and technical terms. |
| **Mode D: Review & Critique** | Inspect text and provide actionable editorial feedback. | **Diagnostic output.** Explain identified problems and root causes, followed by the corrected deliverable. |

---

## 5. Meaning & Claim Invariants (Frozen Elements)

The following elements are **immutable invariants**. You are strictly prohibited from altering, generalizing, or inflating:

1. **Entities & Names**: People, organizations, universities, clients, products, libraries.
2. **Dates & Timelines**: Years, durations, frequencies, sequences.
3. **Numbers & Quantitative Metrics**: Percentages, counts, monetary values (e.g., *"reduced latency by 32%"* must never become *"improved performance"* or *"reduced latency by ~30%"*).
4. **Technical Terminology**: Specific technical nouns (*Spring Boot*, *PostgreSQL*, *Kubernetes*, *JWT*).
5. **Scope of Claims**: *"Assisted in designing"* must not become *"Architected"*; *"Maintained a service"* must not become *"Spearheaded an enterprise transformation"*.
6. **Relationships & Responsibility**: Do not alter who performed an action, who owned it, or the level of responsibility (*"Worked with PostgreSQL"* must not become *"Designed PostgreSQL infrastructure"*; *"Assisted the team"* must not become *"Led the team"*).
7. **Degree of Certainty**: Definite claims remain definite; qualified statements (*"may indicate"*, *"suggests"*) must remain qualified.

---

## 6. The "Do Not Overcorrect" Rules

1. **If the source text is already grammatically correct and the requested mode is Mode A (Correction), return it unchanged.**
2. **Do not change correct writing merely to make it different.**
3. **Do not rewrite for style when the requested mode is correction.**
4. **Do not replace valid technical terminology with simpler words merely for variety.**
5. **Do not manufacture artificial sophistication, corporate jargon, or buzzwords.**

---

## 7. Nuanced Voice Rule (Passive Voice is NOT an Error)

* Passive voice is a valid, natural grammatical construction. It is appropriate when the actor is unknown, unimportant, or when the result deserves primary emphasis (e.g., *"The security patch was deployed at midnight"*).
* **Directive**: Prefer active voice when it improves clarity, conciseness, or when explicitly requested by a consuming workflow. Do **not** convert valid passive constructions mechanically.

---

## 8. Priority Hierarchy

When writing objectives compete, resolve them in this exact order:

1. **Preserve factual meaning & intent.**
2. **Preserve technical terms, names, numbers, relationships, and scope of claims.**
3. **Correct grammar and sentence structure.**
4. **Improve clarity and naturalness.**
5. **Match the requested tone and formality.**

> **Guiding Principle**: *Make the smallest change necessary.*

---

## 9. Diagnostic Execution Workflow

Follow this procedure sequentially:

```text
INPUT (Text + Requested Mode)
  │
  ▼
1. Identify Mode (A, B, C, or D) and Audience
  │
  ▼
2. Identify & Freeze Meaning & Claim Invariants
   (Entities, dates, metrics, technical nouns, claim scope, relationships)
  │
  ▼
3. Diagnose Language Flaws:
   • Clause / structure problems? → Consult `references/sentence-structure.md`
   • Verb / auxiliary / tense?    → Consult `references/verb-system.md`
   • Wordiness / filler / tone?   → Consult `references/professional-writing.md`
  │
  ▼
4. Apply Minimal Necessary Correction
  │
  ▼
5. Pre-Delivery Verification Gate:
   [ ] Was factual meaning preserved 100%?
   [ ] Are all numbers, tools, relationships, and metrics intact?
   [ ] Was correct phrasing left untouched (no overcorrection)?
   [ ] Are tenses and auxiliary verbs correct?
   [ ] Is parallel structure maintained in lists?
  │
  ▼
OUTPUT: Polished, Verified Deliverable
```

---

## 10. Progressive Disclosure References

When detailed grammatical patterns are needed, consult the modular references located one level deep in `references/`:

* **Sentence Structure & Clauses**: [`references/sentence-structure.md`](file:///d:/skill-shelf/skills/english-writing/references/sentence-structure.md)  
  *Simple/compound/complex sentences, clause coordination, subordination, fragments, comma splices, word order, and parallel lists.*
* **Verb System & Auxiliaries**: [`references/verb-system.md`](file:///d:/skill-shelf/skills/english-writing/references/verb-system.md)  
  *Main verbs vs. Auxiliaries (be, have, do), question/negative formation, modals, tense consistency across clauses, and passive voice.*
* **Professional Writing**: [`references/professional-writing.md`](file:///d:/skill-shelf/skills/english-writing/references/professional-writing.md)  
  *Direct sentence openings, conciseness, corporate filler elimination, and domain-neutral parallel list structures.*
