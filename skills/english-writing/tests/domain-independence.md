# Domain Independence & Architecture Regression Tests

These tests validate that the English Writing skill remains a pure, domain-neutral language capability that functions seamlessly across emails, LinkedIn posts, and technical notes without leaking resume-specific assumptions.

---

## TEST-P07: Domain Independence Test

### Test Case A: Professional Email
* **Input Prompt**:
  > *"Please check this email for grammar: 'Hi team, can you sent me the revised deployment checklist by tomorrow afternoon? Thanks, Alex' (Mode: Mode A)"*
* **Assertion Criteria**:
  * **PASS** if the verb form error (*"sent"* $\rightarrow$ *"send"*) is corrected cleanly:
    > *"Hi team, can you send me the revised deployment checklist by tomorrow afternoon? Thanks, Alex"*
  * **PASS** if email greetings, sign-offs, and tone are intact.
  * **FAIL** if the AI attempts to turn the email into action-verb bullet points or resume-style phrasing.

### Test Case B: LinkedIn Post
* **Input Prompt**:
  > *"Please polish this LinkedIn update for clarity: 'Happy to share that our team have completed the cloud migration project after six months hard work.' (Mode: Mode B)"*
* **Assertion Criteria**:
  * **PASS** if subject-verb agreement (*"our team has"* or *"our team have"* depending on dialect) and punctuation (*"six months of hard work"*) are corrected while preserving the authentic, celebratory LinkedIn tone.
  * **FAIL** if the text is rewritten into formal resume bullet syntax.

### Test Case C: Technical Documentation
* **Input Prompt**:
  > *"Please review this architecture note: 'The API gateway authenticate each request before routing it to the internal cluster.' (Mode: Mode A)"*
* **Assertion Criteria**:
  * **PASS** if the 3rd-person singular present inflection (*"authenticates"*) is corrected:
    > *"The API gateway authenticates each request before routing it to the internal cluster."*
  * **PASS** if technical precision is 100% maintained.

---

## TEST-P08: Architecture Regression & Decoupling Test

### Assertion Criteria
1. Scan all files in `skills/english-writing/`:
   * `SKILL.md`
   * `references/sentence-structure.md`
   * `references/verb-system.md`
   * `references/professional-writing.md`
2. **ASSERT**: Zero occurrences of `resume-generator`.
3. **ASSERT**: Zero occurrences of resume-specific constraints (e.g., *"1 page"*, *"resume sections"*, *"ATS parsing"*).
4. **PASS** if `english-writing` can be fully understood, loaded, and executed by an AI that has never heard of `resume-generator`.
