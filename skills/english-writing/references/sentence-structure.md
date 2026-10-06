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
