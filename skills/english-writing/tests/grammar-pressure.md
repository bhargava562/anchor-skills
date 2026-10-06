# Grammar & Structural Pressure Tests

These pressure tests validate that the English Writing skill identifies and corrects structural and grammatical flaws—specifically auxiliary verb usage, question inversion, and cross-clause tense consistency—without over-rewriting.

---

## TEST-P02: Auxiliary Verb Omission & Word Order in Questions

### Input Sentences
> "Why the application failed during deployment yesterday? What means this error code?"

### Mode Requested
`Mode A: Grammar Correction`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: AI rewrites the entire question stylistically (e.g., *"Could you explain the cause of yesterday's deployment failure and the significance of this error code?"*) instead of executing targeted grammatical correction of the auxiliary verbs.

### Diagnostic Requirement (Murphy Units 49, 51)
* Question 1 lacks past auxiliary *did* and needs base verb: *"Why did the application fail during deployment yesterday?"*
* Question 2 uses incorrect verb-subject inversion without auxiliary *does*: *"What does this error code mean?"* (not *"What means this error code?"*).

### Assertion Criteria (With Skill)
* **PASS** if the output applies minimal necessary edits to correct auxiliary structure:
  > *"Why did the application fail during deployment yesterday? What does this error code mean?"*
* **FAIL** if the questions are transformed into indirect polite inquiries or stylistically overwritten.

---

## TEST-P03: Tense Inconsistency Across Clauses

### Input Sentence
> "Last year our team migrated the infrastructure to AWS and it improves deployment speed, but we are facing network bottlenecks now."

### Mode Requested
`Mode A: Grammar Correction`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: The AI frequently changes the final clause into the past tense (*"faced network bottlenecks"*), failing to recognize that *"now"* indicates a valid current situation, or switches everything into passive voice.

### Diagnostic Requirement (Murphy Units 5, 14, 19)
* Clause 1 (*migrated*) is completed past $\rightarrow$ simple past.
* Clause 2 (*improves*) relates directly to the past migration $\rightarrow$ must be past tense (*improved*).
* Clause 3 (*now*) represents an ongoing present reality $\rightarrow$ present continuous (*are facing*) is correct and must be preserved.

### Assertion Criteria (With Skill)
* **PASS** if the output resolves the past clause while preserving the present continuous:
  > *"Last year our team migrated the infrastructure to AWS and it improved deployment speed, but we are facing network bottlenecks now."*
* Or a direct coordination variant maintaining the temporal distinction cleanly.
