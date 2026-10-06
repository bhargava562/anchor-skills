# Benchmark Examples: Before and After

> **Reference Examples for `english-writing`**  
> *Demonstrating Mode A (Grammar Correction), Mode B (Clarity Improvement), Mode C (Professional Rewrite), and Mode D (Review & Critique).*

---

## Example 1: Mode A (Grammar Correction — Minimum Edits)

### Input
> *"The development team have deployed the new release yesterday, but several tests is failing."*

### Desired Transformation
Fix subject-verb agreement and past tense without changing vocabulary or sentence structure.

### Corrected Output
> *"The development team deployed the new release yesterday, but several tests are failing."*

### Key Invariants & Annotations
* Fixed *have deployed ... yesterday* $\rightarrow$ *deployed* (Murphy Unit 14: finished time requires past simple).
* Fixed *several tests is* $\rightarrow$ *several tests are* (plural agreement).
* Zero stylistic tampering; sentence structure preserved exactly.

---

## Example 2: Mode B (Clarity & Flow — Awkward Construction)

### Input
> *"In spite of the fact that we tried hard for to resolve the memory leak, it was not able to be fixed by us before the launch date."*

### Desired Transformation
Trim wordy padding (*in spite of the fact that*), fix awkward double-preposition (*for to*), and resolve clumsy passive construction.

### Corrected Output
> *"Although we tried hard to resolve the memory leak, we could not fix it before the launch date."*

### Key Invariants & Annotations
* Trimmed *in spite of the fact that* $\rightarrow$ *although*.
* Corrected *tried hard for to resolve* $\rightarrow$ *tried hard to resolve*.
* Restructured clumsy passive (*it was not able to be fixed by us*) into natural active voice (*we could not fix it*).
* Facts and timeline (*launch date*, *memory leak*) 100% preserved.

---

## Example 3: Mode C (Professional Rewrite — Fluff Removal & Active Polish)

### Input
> *"I was personally responsible for dynamically spearheading the migration of our monolithic system over to Kubernetes microservices, which resulted in a massive 45% increase in deployment velocity."*

### Desired Transformation
Eliminate empty corporate adjectives (*personally responsible for*, *dynamically spearheading*, *massive*), preserve all tools (*monolithic system*, *Kubernetes microservices*), preserve exact metric (*45%*), and maintain truthful claim scope.

### Corrected Output
> *"Led the migration of the monolithic system to Kubernetes microservices, increasing deployment velocity by 45%."*

### Key Invariants & Annotations
* Removed filler: *personally responsible for*, *dynamically spearheading*, *massive*.
* Preserved exact technical nouns: *Kubernetes microservices*, *monolithic system*.
* Preserved exact quantitative metric: *45%*.
* Strengthened verb to clear, dignified active voice.

---

## Example 4: Mode D (Review & Critique — Diagnostic Output)

### Input
> *"Why the server crashed during the benchmark? We didn't received any alerts."*

### Desired Transformation
Diagnose the grammatical root causes, explain the rules, and provide the clean version.

### Output
> ### Diagnostic Critique
> 1. **Missing Auxiliary Verb in Question**: The sentence *"Why the server crashed...?"* forms a past question without the auxiliary verb *did*. In English, questions with a question word and explicit subject require `[Question Word] + did + [Subject] + [Base Verb]` (Murphy Units 49, 51).
> 2. **Double Past Inflection**: In *"We didn't received..."*, the negative auxiliary *didn't* already carries the past tense. The main verb must remain in its base form (*receive*), not past participle (Murphy Unit 5C).
>
> ### Corrected Version
> *"Why did the server crash during the benchmark? We didn't receive any alerts."*
