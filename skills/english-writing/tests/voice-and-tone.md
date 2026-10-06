# Voice, Tone & Parallelism Pressure Tests

These pressure tests validate that the English Writing skill enforces parallel grammatical structures in lists and applies nuanced voice rules (preferring active voice for clarity while retaining valid passive constructions).

---

## TEST-P04: Parallel Structure in Generic Lists

### Input Sentence
> "The role involves designing distributed systems, to lead code reviews, and maintenance of legacy databases."

### Mode Requested
`Mode B: Clarity Improvement`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: AI often leaves the mixed grammatical forms intact (gerund *designing*, infinitive *to lead*, noun phrase *maintenance of*) while adding filler words, or arbitrarily changes the whole list into bullet points.

### Diagnostic Requirement
* The coordinated series governed by *"involves"* mixes three grammatical forms:
  1. *designing* (gerund)
  2. *to lead* (infinitive)
  3. *maintenance of* (noun phrase)
* All items in a coordinated series must share the same grammatical part of speech.

### Assertion Criteria (With Skill)
* **PASS** if the output harmonizes the list into parallel grammatical forms (e.g., all gerunds):
  > *"The role involves designing distributed systems, leading code reviews, and maintaining legacy databases."*
* Or all noun phrases:
  > *"The role involves the design of distributed systems, leadership of code reviews, and maintenance of legacy databases."*

---

## TEST-P10: Valid Passive Voice Retention vs. Active Voice Preference

### Scenario A: Valid Passive Voice Should Be Retained
* **Input Sentence**:
  > *"The vulnerability was patched before customer data could be accessed."*
* **Mode Requested**: `Mode B: Clarity Improvement`
* **Assertion Criteria**:
  * **PASS** if the passive construction is retained. The actor is unspecified and the vulnerability is the proper subject.
  * **FAIL** if the AI invents an actor (e.g., *"Our team patched the vulnerability..."*).

### Scenario B: Active Voice Preferred When Actor is Explicit and Clarity Increases
* **Input Sentence**:
  > *"A 25% performance improvement was achieved by the engineering team through query indexing."*
* **Mode Requested**: `Mode C: Professional Rewrite`
* **Assertion Criteria**:
  * **PASS** if the AI converts to direct active voice:
    > *"The engineering team achieved a 25% performance improvement through query indexing."*
  * **PASS** if metrics (25%) and facts (query indexing, engineering team) are 100% preserved.
