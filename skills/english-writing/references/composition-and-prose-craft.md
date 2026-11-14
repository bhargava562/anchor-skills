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
