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
| **Mode E: Composition & Content Generation** | Generate coherent, original paragraphs, explanations, or prose from minimal prompts. | **Original composition.** Organize ideas in logical progression, vary sentence structure, maximize prose economy, and preserve technical precision. |

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

## 6. The "Do Not Overcorrect" & Lexical Precision Rules

1. **If the source text is already grammatically correct and the requested mode is Mode A (Correction), return it unchanged.**
2. **Do not change correct writing merely to make it different.**
3. **Do not rewrite for style when the requested mode is correction.**
4. **Avoid unnecessary repetition; preserve useful repetition when it improves accuracy, emphasis, or clarity. Never force unnatural synonyms.**
5. **Do not replace valid technical terminology with simpler words merely for variety.**
6. **Do not manufacture artificial sophistication, corporate jargon, or buzzwords.**
7. **Do not output an audit or vocabulary report by default in ordinary writing outputs. Deliver clean prose directly unless an audit is explicitly requested.**

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

## 9. Execution Workflows

### 9.1 Revision & Correction Workflow (Modes A, B, C, D)
1. **Identify Mode & Audience**: Set target tolerance (A: minimal, B: flow, C: professional rewrite, D: critique).
2. **Freeze Invariants**: Lock entities, metrics, technical terms, relationships, and claim scope.
3. **Diagnose & Consult References**:
   * Clause / structure problems? → Consult `references/sentence-structure.md`
   * Verb / auxiliary / tense?    → Consult `references/verb-system.md`
   * Wordiness / filler / tone?   → Consult `references/professional-writing.md`
4. **Apply Minimal Necessary Correction**.
5. **Verification Gate**: Confirm 100% meaning preservation, zero fact alteration, and absence of overcorrection.

### 9.2 Original Composition Workflow (Mode E)
1. **Identify Purpose, Audience & Format**: Determine the explanatory goal and register.
2. **Arrange Logical Progression**: Sequence ideas causally (Premise $\rightarrow$ Mechanism $\rightarrow$ Consequence $\rightarrow$ Resolution).
3. **Draft with Prose Craft**: Consult `references/composition-and-prose-craft.md` for paragraph cohesion, natural transitions, sentence rhythm, and prose economy.
4. **Maintain Lexical Precision**: Use precise domain terminology; vary secondary words naturally without forced synonyms.
5. **Eliminate Redundancy & Filler**: Strip throat-clearing preambles and empty clichés.
6. **Verification Gate**: Confirm causal soundness, factual grounding (zero fabricated statistics), and clean grammatical mechanics.

---

## 10. Progressive Disclosure References

When detailed grammatical patterns are needed, consult the modular references located one level deep in `references/`:

* **Sentence Structure & Clauses**: [`references/sentence-structure.md`](file:///d:/skill-shelf/skills/english-writing/references/sentence-structure.md)  
  *Simple/compound/complex sentences, clause coordination, subordination, fragments, comma splices, word order, and parallel lists.*
* **Verb System & Auxiliaries**: [`references/verb-system.md`](file:///d:/skill-shelf/skills/english-writing/references/verb-system.md)  
  *Main verbs vs. Auxiliaries (be, have, do), question/negative formation, modals, tense consistency across clauses, and passive voice.*
* **Professional Writing**: [`references/professional-writing.md`](file:///d:/skill-shelf/skills/english-writing/references/professional-writing.md)  
  *Direct sentence openings, conciseness, corporate filler elimination, and domain-neutral parallel list structures.*
* **Composition & Prose Craft**: [`references/composition-and-prose-craft.md`](file:///d:/skill-shelf/skills/english-writing/references/composition-and-prose-craft.md)  
  *Paragraph architecture, logical progression, coherence, lexical variety, sentence rhythm, prose economy, and redundancy elimination.*

---

# ============================================================
# PROGRESSIVE DISCLOSURE REFERENCES
# ============================================================

## Reference: references/composition-and-prose-craft.md

# Composition & Prose Craft

> **Reference Module for `english-writing`**  
> *Guidelines for paragraph architecture, logical flow, lexical variety, prose economy, and sentence rhythm.*

---

## 1. Paragraph Architecture & Logical Flow

A well-crafted paragraph is an organized unit of thought, not merely a collection of grammatically sound sentences.

### Progression Model
When developing an explanation or technical argument, structure ideas in a sensible sequence:
1. **Core Assertion / Topic Focus**: State the central reality or problem directly.
2. **Mechanism / Root Cause**: Explain how or why the phenomenon occurs.
3. **Cascading Effects / Implications**: Show the practical consequences, constraints, or trade-offs.
4. **Resolution or Concluding Insight**: State the mitigation, standard approach, or summarizing point.

### Example Progression
* *Premise*: Distributed systems struggle when incoming traffic surges unpredictably.
* *Mechanism*: Stateless services can scale horizontally, but shared stateful bottlenecks (relational databases, locks, network switches) cannot absorb exponential concurrency immediately.
* *Consequence*: Queues saturate, connection pools exhaust, and timeouts trigger cascading retry storms across upstream services.
* *Resolution*: Without backpressure or graceful shedding, the entire cluster risks degradation.

---

## 2. Coherence & Cohesion: Natural Transitions

Cohesion connects adjacent sentences so that readers follow the argument without friction.

### Natural Lexical Ties vs. Mechanical Conjuncts
* **Anti-Pattern (Mechanical Transition Stuffing)**: Beginning every sentence with a robotic linking adverb:
  * *Poor*: *"Traffic increases rapidly. Furthermore, databases become slow. Moreover, connection pools exhaust. Consequently, services crash."*
* **Best Practice (Lexical Hooks & Demonstrative Pronouns)**: Link sentences by carrying key concepts or demonstratives across clause boundaries:
  * *Effective*: *"When sudden traffic spikes hit distributed systems, downstream databases quickly become the critical bottleneck. These stateful stores cannot provision capacity instantly, causing incoming requests to queue. As queue depths grow, client timeouts trigger aggressive retries, creating a cascading failure loop that overwhelms the remaining infrastructure."*

---

## 3. Lexical Variety vs. Technical Precision

### The Golden Rule
> **Avoid unnecessary repetition; preserve useful repetition when it improves accuracy, emphasis, or clarity. Never force unnatural synonyms.**

### When to Vary Words
Vary secondary content words, verbs of action, and relational phrases when repeated use sounds monotonous:
* *Repetitive*: *"The system handles requests quickly. The system handles errors by retrying. The system handles logging separately."*
* *Varied*: *"The service processes requests quickly, recovers from errors via automated retries, and delegates logging to an external pipeline."*

### When to Preserve Words (Technical Precision Invariant)
Do **not** use thesaurus-hunting synonyms for established technical nouns, protocols, or core architectural entities:
* *Correct*: Consistently use `distributed systems`, `database`, `latency`, `cache`, `network`.
* *Harmful*: Replacing `database` with *"data repository"*, *"information vault"*, or *"electronic storehouse"* merely to avoid repeating the word. Technical precision always outranks stylistic variety.

---

## 4. Sentence Rhythm & Structural Variety

Monotonous writing uses identical sentence lengths and structures repeatedly (e.g., five medium-length Subject-Verb-Object sentences in a row).

### Techniques for Rhythm
1. **Combine Short and Complex Sentences**: Follow a detailed, compound-complex explanation with a crisp, punchy assertion.
   * *Example*: *"When connection pools exhaust and downstream dependencies stop responding, timeouts multiply across the call graph. The cluster collapses."*
2. **Vary Sentence Openers**:
   * *Subject First*: *"Sudden traffic surges saturate thread pools."*
   * *Participial Phrase*: *"Lacking automated backpressure mechanisms, upstream proxies continue forwarding traffic."*
   * *Prepositional / Conditional Clause*: *"Under sustained overload, aggressive client retries worsen the outage."*

---

## 5. Prose Economy & Eliminating Redundancy

Prose economy means maximizing information density while removing fluff, tautologies, and empty throat-clearing.

### Throat-Clearing Preambles to Eliminate
* *"It is important to understand that..."* $\rightarrow$ Delete.
* *"In the modern technological landscape of today..."* $\rightarrow$ Delete.
* *"It is widely acknowledged that distributed systems..."* $\rightarrow$ *"Distributed systems..."*

### Tautologies (Redundant Duplications)
* *"completely full"* $\rightarrow$ *"full"*
* *"future plans"* $\rightarrow$ *"plans"*
* *"unexpected surprise"* $\rightarrow$ *"surprise"*
* *"period of time"* $\rightarrow$ *"period"* / *"time"*
* *"revert back"* $\rightarrow$ *"revert"*

### Factual Grounding Rule
Never invent unverified statistics (*"99.9% of outages"*, *"studies prove that..."*) to artificially substantiate an argument. Rely strictly on causal logic, verifiable engineering mechanisms, or provided source context.

## Reference: references/professional-writing.md

# Professional Writing & Clarity Principles

> **Reference Module for `english-writing`**  
> *Domain-neutral guidelines for clear, direct, and concise professional communication.*

---

## 1. Direct Sentence Openings

### Principle
Begin sentences with the primary subject and clear, active verbs rather than burying the core message behind throat-clearing preambles.

### Anti-Patterns vs. Direct Phrasing
* *Weak/Delayed*: *"It should be noted that in our recent evaluation, the benchmark tests demonstrated higher throughput."*
* *Direct*: *"Recent benchmark tests demonstrated higher throughput."*
* *Weak/Delayed*: *"There were several team members who noticed an issue with the endpoint."*
* *Direct*: *"Several team members noticed an issue with the endpoint."*

---

## 2. Conciseness: Trimming Wordy Padding

Replace bloated multi-word idioms with direct, crisp alternatives:

| Wordy Phrase | Concise Replacement |
| :--- | :--- |
| *in order to* | **to** |
| *due to the fact that* | **because** |
| *at this point in time* | **now** / **currently** |
| *has the ability to* | **can** |
| *make an examination of* | **examine** |
| *give consideration to* | **consider** |
| *for the purpose of* | **for** / **to** |
| *with the exception of* | **except** |
| *in the event that* | **if** |
| *bring to a conclusion* | **conclude** |

---

## 3. Eliminating Empty Corporate Fluff

Professional prose gains authority through specific evidence, technical accuracy, and concrete facts—never through inflated adjectives.

### Words to Eliminate
* *"Results-driven"* / *"Dynamic"* / *"Passionate"* / *"Visionary"*
* *"World-class"* / *"Cutting-edge"* / *"Game-changing"* / *"State-of-the-art"*
* *"Seamlessly"* / *"Synergistic"* / *"Best-of-breed"*

### Concrete Replacement Principle
Replace qualitative boasting with concrete technical description:
* *Fluffy*: *"Spearheaded a dynamic, game-changing architecture that seamlessly revolutionized our workflow."*
* *Substantive*: *"Redesigned the messaging pipeline with Apache Kafka, reducing message latency from 1.2s to 180ms."*

---

## 4. Parallel Structure in Professional Lists

Whether constructing documentation bullet points, email lists, or project milestones, maintain identical grammatical forms across all items in a list:

### Consistent Part of Speech
* **Gerund Series**: All items start with an *-ing* verb:
  * *Correct*:
    * *Monitoring database health and memory utilization.*
    * *Optimizing slow queries via indexing.*
    * *Configuring read replicas for high availability.*
* **Imperative / Action Series**: All items start with an imperative verb (common in checklists or instructions):
  * *Correct*:
    * *Verify the cryptographic signature.*
    * *Inspect the payload headers.*
    * *Forward the request to the upstream proxy.*
* **Noun Phrase Series**: All items start with a noun:
  * *Correct*:
    * *Automated nightly backups.*
    * *Role-based access control.*
    * *Distributed request tracing.*

---

## 5. Tone Calibration & Levels of Formality

Adjust phrasing to match the requested level of formality without sacrificing clarity:

| Register | Context | Characteristics | Example |
| :--- | :--- | :--- | :--- |
| **Formal** | Executive briefs, whitepapers, legal/policy notes | Objective third-person, full verb forms (no contractions), measured vocabulary. | *"The committee evaluated three architectural proposals before reaching consensus."* |
| **Professional-Neutral** | Technical documentation, peer code reviews, engineering emails | Direct, respectful, standard contractions acceptable, focused on problem-solving. | *"We recommend migrating to PostgreSQL because query response times have doubled."* |
| **Conversational-Professional** | Slack/Teams messages, collaborative notes | Brief, collegial, direct calls-to-action. | *"Could you review the updated deployment config when you have a moment?"* |

## Reference: references/sentence-structure.md

# Sentence Structure & Clause Mechanics

> **Reference Module for `english-writing`**  
> *Conceptual synthesis informed by English Grammar in Use (Raymond Murphy, 5th Ed., Units 92–97, 109–110, 113–120).*

---

## 1. Clauses vs. Sentences

### Independent Clause
* **CONCEPT**: A clause containing a subject and a finite verb that expresses a complete thought and can stand alone as a grammatical sentence.
* **STRUCTURE**: `[Subject] + [Verb] (+ Object / Complement)`
* **EXAMPLE**: *"The service authenticated the token."*

### Dependent (Subordinate) Clause
* **CONCEPT**: A clause containing a subject and verb that begins with a subordinating conjunction or relative pronoun. It cannot stand alone.
* **STRUCTURE**: `[Subordinating Conjunction] + [Subject] + [Verb]`
* **EXAMPLE**: *"...because the database connection timed out."*

---

## 2. Sentence Types & Clause Coordination

### 2.1 Simple Sentence
* **CONCEPT**: A single independent clause expressing one complete idea.
* **EXAMPLE**: *"The deployment completed successfully at midnight."*

### 2.2 Compound Sentence (Coordination)
* **CONCEPT**: Two or more independent clauses joined by a coordinating conjunction (*for, and, nor, but, or, yet, so*) or a semicolon.
* **STRUCTURE**: `[Independent Clause], + [Coordinating Conjunction] + [Independent Clause]`
* **COMMON ERROR**: Comma splice (joining two independent clauses with only a comma).
  * *Incorrect*: *"The cache invalidated, the query latency spiked immediately."*
  * *Correction*: *"The cache invalidated, and the query latency spiked immediately."* Or use a semicolon: *"The cache invalidated; the query latency spiked immediately."*

### 2.3 Complex Sentence (Subordination)
* **CONCEPT**: One independent clause combined with one or more dependent clauses introduced by subordinators (*although, because, since, while, after, before, unless, provided*).
* **PUNCTUATION RULE**: When the dependent clause precedes the independent clause, place a comma after it. When it follows, a comma is usually unnecessary.
  * *Leading Dependent*: *"Although the cluster experienced heavy traffic, response times remained stable."*
  * *Trailing Dependent*: *"Response times remained stable although the cluster experienced heavy traffic."*

---

## 3. Structural Faults to Eliminate

### 3.1 Sentence Fragments
* **CONCEPT**: An incomplete sentence masquerading as a complete one, missing either a subject, a finite verb, or standing as an unattached subordinate clause.
* **COMMON ERROR**: *"Which reduced processing time by 15%."*
* **CORRECTION**: Attach the fragment to the preceding independent clause:
  * *"The algorithm cached intermediate results, which reduced processing time by 15%."*

### 3.2 Run-on Sentences & Comma Splices
* **COMMON ERROR**: *"The team pushed the hotfix the build failed on CI."*
* **CORRECTION**: Split into two sentences or join with a coordinator:
  * *"The team pushed the hotfix, but the build failed on CI."*

---

## 4. Word Order: Verbs, Objects, and Adverbs

*(Informed by Murphy Units 109–110)*

### 4.1 Verb and Object Adjacency
* **RULE**: In English, the direct object normally follows immediately after the verb. Do not insert adverbs or prepositional phrases between a transitive verb and its direct object.
  * *Incorrect*: *"The engineer explained clearly the architectural pattern."*
  * *Correct*: *"The engineer explained the architectural pattern clearly."*
  * *Incorrect*: *"We discussed yesterday the migration timeline."*
  * *Correct*: *"We discussed the migration timeline yesterday."*

### 4.2 Adverb Placement with Auxiliaries
* **RULE**: Adverbs of frequency and certainty (*always, often, already, probably, never, also*) go **between** the auxiliary and the main verb, or after the simple verb *be*.
  * *Incorrect*: *"The server will restart probably tonight."*
  * *Correct*: *"The server will probably restart tonight."*
  * *Incorrect*: *"They have finished already the testing phase."*
  * *Correct*: *"They have already finished the testing phase."*

---

## 5. Parallel Structure

### CONCEPT
Items in a series, list, or compound predicate must share the identical grammatical form.

### PATTERNS
1. **Series of Gerunds**:
   * *Incorrect*: *"Her duties include writing unit tests, to deploy microservices, and maintenance of documentation."*
   * *Correct*: *"Her duties include writing unit tests, deploying microservices, and maintaining documentation."*
2. **Series of Infinitives**:
   * *Correct*: *"The objective is to refactor legacy modules, reduce technical debt, and improve test coverage."* (The marker *to* may apply to all items or be repeated before each).
3. **Series of Predicate Verbs**:
   * *Incorrect*: *"The script parses the raw logs, validated the payload, and sends alerts."*
   * *Correct*: *"The script parses the raw logs, validates the payload, and sends alerts."*

## Reference: references/verb-system.md

# Verb System & Auxiliary Mechanics

> **Reference Module for `english-writing`**  
> *Conceptual synthesis informed by English Grammar in Use (Raymond Murphy, 5th Ed., Units 1–16, 26–36, 42–46, 49–52).*

---

## 1. Main Verbs vs. Auxiliary Verbs

A verb phrase consists of a **main verb** expressing the core action or state, optionally preceded by one or more **auxiliary (helping) verbs** that indicate tense, aspect, voice, negation, or modality.

---

## 2. The Three Primary Auxiliaries: *DO*, *BE*, *HAVE*

### 2.1 Auxiliary *DO / DOES / DID*
*(Informed by Murphy Units 2, 5, 49, 51)*

* **CONCEPT**: Used to form questions, negative statements, and emphatic assertions in the Present Simple and Past Simple when no other auxiliary verb is present.
* **STRUCTURE**:
  * Negative: `[Subject] + do/does/did + not + [Base Verb]`
  * Question: `[Question Word] + do/does/did + [Subject] + [Base Verb]?`
* **COMMON ERRORS**:
  * *Missing auxiliary in questions*: *"Why the service crashed yesterday?"*  
    $\rightarrow$ **Correction**: *"Why did the service crash yesterday?"*
  * *Incorrect word order without auxiliary*: *"What means this status code?"*  
    $\rightarrow$ **Correction**: *"What does this status code mean?"*
  * *Double-inflected past tense*: *"The system didn't failed."*  
    $\rightarrow$ **Correction**: *"The system didn't fail."* (Auxiliary *did* carries the past tense; main verb remains base infinitive).
* **RULE ON SUBJECT QUESTIONS**:
  * If the question word (*who / what*) is the **subject** of the sentence, do **not** use *do/does/did*:
    * *"What caused the outage?"* (Correct: *what* is the subject).
    * *"What did the team discover?"* (Correct: *the team* is the subject; *what* is the object).

---

### 2.2 Auxiliary *BE (am, is, are, was, were, been, being)*
*(Informed by Murphy Units 1, 6, 42–44)*

* **Continuous Aspect**: `[be] + [verb-ing]`
  * Expresses an ongoing, incomplete activity at a reference point in time.
  * *Present*: *"The application is processing the queue."*
  * *Past*: *"The service was synchronizing data when the connection dropped."*
* **Passive Voice**: `[be] + [past participle]`
  * Focuses on the receiver or outcome of the action rather than the agent.
  * *Present*: *"Data is encrypted in transit."*
  * *Past*: *"The patch was deployed at midnight."*
* **COMMON ERROR**: Confusing active continuous with passive participle.
  * *Incorrect*: *"The report was generating by the system."*
  * *Correction (Active)*: *"The system was generating the report."*
  * *Correction (Passive)*: *"The report was being generated by the system."*

---

### 2.3 Auxiliary *HAVE (have, has, had)*
*(Informed by Murphy Units 7–16)*

* **Present Perfect**: `have/has + [past participle]`
  * Connects a past action to the present moment, indicating recent occurrence, ongoing relevance, or life experience up to now.
  * *Correct*: *"We have resolved the incident."* (The incident is resolved now).
  * *Correct*: *"The platform has operated without downtime since April."*
  * *Contrast with Past Simple*: Use simple past when specifying a finished time period (*yesterday*, *in 2023*, *last week*):
    * *Incorrect*: *"We have completed the migration last week."*
    * *Correct*: *"We completed the migration last week."*
* **Past Perfect**: `had + [past participle]`
  * Indicates an action completed *before* another past event.
  * *Correct*: *"By the time the alert fired, the service had already restarted."*

---

## 3. Modal Auxiliary Verbs

*(Informed by Murphy Units 26–36)*

Modal verbs (*can, could, may, might, must, should, would*) modify the mood, likelihood, necessity, or capability of the main verb:

| Modal | Communicative Role | Professional Example |
| :--- | :--- | :--- |
| **can / be able to** | Current capability or possibility | *"The parser can process 5,000 records per second."* |
| **could** | Past capability or tentative suggestion | *"We could decouple the authentication layer."* |
| **may / might** | Possibility (unconfirmed fact) | *"The latency spike might stem from disk I/O contention."* |
| **must / have to** | Deduction or mandatory requirement | *"The payload must conform to the JSON schema."* |
| **should / had better** | Recommendation or expected outcome | *"The pipeline should finish within five minutes."* |
| **would** | Hypothetical consequence | *"Refactoring would reduce maintenance overhead."* |

* **RULE**: Modals are followed directly by the bare infinitive (without *to*):
  * *Incorrect*: *"The team must to update the certificate."*
  * *Correct*: *"The team must update the certificate."*

---

## 4. Tense Consistency Across Clauses

* Maintain a logical temporal timeline across related clauses in compound and complex sentences.
* **COMMON ERROR (Tense Drift)**:
  * *Incorrect*: *"Last quarter we migrated the database to PostgreSQL and it improves performance, but we are monitoring index health now."*
  * *Diagnostic*: The first clause (*migrated*) and second clause (*improves*) describe the completed past event; the third clause describes the current state.
  * *Correct*: *"Last quarter we migrated the database to PostgreSQL and it improved performance, but we are monitoring index health now."*

---

## 5. Active Voice vs. Nuanced Passive Voice

*(Informed by Murphy Units 42–44)*

* **Passive voice is NOT a grammatical error.**
* Use **Active Voice** when the agent (who performed the action) is known, important, and leads to direct, vigorous prose:
  * *"The security team identified three critical vulnerabilities."*
* Use **Passive Voice** when:
  1. The actor is unknown or irrelevant:
     * *"Over 10,000 transactions were processed during the blackout."*
  2. The subject being acted upon is the proper topic of discussion:
     * *"The legacy monolith was successfully decommissioned."*
  3. Stating objective security or system policies:
     * *"All API tokens are hashed before storage."*
* **Directive**: Prefer active voice for clarity and brevity, but do not dogmatically convert valid, purposeful passive constructions.

---

# ============================================================
# LOCAL CONFIGURATION OVERRIDES (overrides.md)
# ============================================================

# English Writing — Overrides & Configuration

This file provides project-level and user-specific configuration overrides for the `english-writing` skill. Modify these settings to tune default operating modes, tone guidelines, and vocabulary rules.

---

## 1. Operating Mode Override

* **Default**: `Mode B` (Clarity Improvement)
* **Options**:
  * `Mode A` (Grammar Correction only - minimal changes)
  * `Mode B` (Clarity Improvement - moderate targeted edits)
  * `Mode C` (Professional Rewrite - controlled restructuring)
  * `Mode D` (Review & Critique - diagnostic output)
  * `Mode E` (Composition & Content Generation - original composition)

```yaml
default_mode: Mode B
```

---

## 2. Style & Tone Preferences

```yaml
style_preferences:
  dialect: US_English        # Options: US_English, UK_English
  oxford_comma: true         # Enforce Oxford comma
  active_voice_bias: true    # Prefer active voice over passive voice
  formality_level: high      # Options: casual, standard, high
```

---

## 3. Domain Terminology & Protected Terms

List terms that must never be modified, rewritten, or simplified:

* Specific product names, brand names, and trademarked terms
* Code-level symbols, API methods, and variable names
* Technical acronyms (e.g., ADR, BLUF, JTBD, RICE, SLA)
