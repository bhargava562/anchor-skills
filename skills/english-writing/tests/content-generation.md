# Original Content Generation & Prose Craft Tests

These tests evaluate whether the English Writing skill produces coherent, informative, and structurally varied original prose when invoked with a short, minimal prompt—without requiring lengthy formatting instructions.

---

## 1. Testing Methodology

### Step 1: Verification of Activation
Confirm that `english-writing` is properly discovered and loaded by the AI environment (via skill discovery records or session traces). High output quality alone does not prove skill activation; verification requires confirming that the model recognized and consulted the skill.

### Step 2: Invariant-Based Rubric Evaluation
Evaluate the generated output against the 8-point rubric below. Do **not** require the model to output a meta-audit or vocabulary report in normal use; evaluate the output prose directly.

---

## TEST-P09: Technical Paragraph Generation (Distributed Systems Traffic Spikes)

### Short Input Prompt
> *"Write a clear, informative paragraph explaining why distributed systems can struggle during sudden traffic spikes."*

### Target Mode
`Mode E: Composition & Content Generation`

### Baseline AI Failure (Without Skill)
* **Observed Failure Modes**:
  1. *Filler & Clichés*: Begins with throat-clearing fluff (*"In today's fast-paced digital world, distributed systems are increasingly important..."*).
  2. *Mechanical Transitions*: Stuffs formulaic adverbs at the start of every sentence (*"Furthermore... Moreover... In conclusion..."*).
  3. *Invented Statistics*: Injects fake numbers to sound authoritative (*"Over 80% of system crashes are caused by spikes..."*).
  4. *Monotonous Rhythm*: Every sentence has identical length and Subject-Verb-Object cadence.

### Evaluation Rubric

| Criterion | Target Behavior | Failure Condition |
| :--- | :--- | :--- |
| **Logical Flow** | Arranges ideas in a causal sequence: traffic surge $\rightarrow$ stateful bottlenecks $\rightarrow$ queue saturation / retries $\rightarrow$ cascading degradation. | Jumping randomly between unrelated architectural concepts. |
| **Lexical Variety** | Avoids unnecessary repetition of secondary verbs and descriptive words. | Reusing the exact same phrase multiple times (*"the system fails because... and then fails when..."*). |
| **Precision** | Preserves core technical nouns (`distributed systems`, `database`, `latency`, `cache`, `connection pools`). | Thesaurus-hunting for unnatural synonyms (*"dispersed assemblies"*, *"information vaults"*). |
| **Prose Economy** | High information density; zero throat-clearing preambles or empty padding. | Fluff openings (*"It goes without saying that in modern times..."*). |
| **Sentence Variety** | Blends short impact statements with complex analytical explanations; varies openers. | Monotonous sentence length; all sentences opening with Subject-Verb. |
| **Coherence** | Natural transitions via lexical hooks and demonstratives; no robotic transition stuffing. | Forcing *"Furthermore"*, *"Moreover"*, *"Consequently"* into every sentence. |
| **Accuracy** | Causally sound engineering reasoning; zero fabricated statistics or fake citations. | Inventing unverified metrics (*"studies show 90% of failures..."*). |
| **Grammar** | Flawless punctuation, clause syntax, and verb aspect. | Comma splices, fragments, or subject-verb disagreement. |

---

## TEST-P10: Professional Paragraph Generation (Asynchronous Team Communication)

### Short Input Prompt
> *"Write a concise, persuasive paragraph explaining why clear written communication is essential for asynchronous engineering teams."*

### Target Mode
`Mode E: Composition & Content Generation`

### Evaluation Rubric
* **Logical Progression**: Connects time-zone independence to documentation rigor to decision velocity.
* **Prose Economy**: Delivers high-density persuasion in 4–6 sentences without repetitive corporate jargon (*"synergy"*, *"dynamic alignment"*).
* **Tone**: Professional, measured, and direct.
* **Invariant Compliance**: Zero fabricated claims, no ungrounded statistics.
