# Meaning & Claim Preservation Pressure Tests

These pressure tests validate that the English Writing skill strictly preserves factual truth, quantitative metrics, technical terminology, claim scopes, and relationships without inflation or hallucination.

---

## TEST-P01: Claim Scope & Technical Metric Preservation Under Rewrite

### Input Sentence
> "Built an internal service using Spring Boot and PostgreSQL, decreasing query latency by 32% for 10,000 daily active users."

### Mode Requested
`Mode C: Professional Rewrite`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: Inflation of claim scope and rounding of metrics.
* *Example Uncontrolled Output*: *"Architected an enterprise-grade backend infrastructure utilizing Spring Boot and PostgreSQL, slashing query latency by nearly a third for tens of thousands of users."*
* *Flaws*:
  1. Changed relationship/scope: *"Built an internal service"* $\rightarrow$ *"Architected enterprise-grade backend infrastructure"*.
  2. Altered exact metric: *"32%"* $\rightarrow$ *"nearly a third"*.
  3. Altered user scale: *"10,000 daily active users"* $\rightarrow$ *"tens of thousands of users"*.

### Assertion Criteria (With Skill)
* **PASS** if the output:
  1. Preserves exact technical tools: `Spring Boot`, `PostgreSQL`.
  2. Preserves exact metrics: `32%`, `10,000 daily active users`.
  3. Preserves scope of responsibility: Does not inflate *built* to *architected*, *spearheaded*, or *directed*.
  4. Delivers clear, grammatically polished professional prose.

---

## TEST-P05: Do Not Overcorrect Already-Correct Text

### Input Sentence
> "The server restarted automatically after the update was installed."

### Mode Requested
`Mode A: Grammar Correction`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: Compulsive rewriting and unwarranted style changes on correct text.
* *Example Uncontrolled Output*: *"Following the installation of the update, the server underwent an automatic reboot."*
* *Flaw*: The source was 100% grammatically correct. Unnecessary rewriting introduces noise and alters author voice.

### Assertion Criteria (With Skill)
* **PASS** if the output is returned **exactly unchanged**:
  > *"The server restarted automatically after the update was installed."*

---

## TEST-P06: Combined Pressure Test (Grammar + Metrics + Technical Terminology)

### Input Sentence
> "Last month our team was tasked to optimize the pipeline, and we build a Redis cache which was decreasing memory usage by 40%, but there is some edge cases that still need fixing."

### Mode Requested
`Mode C: Professional Rewrite`

### Baseline AI Failure (Without Skill)
* **Observed Failure Mode**: When multiple issues compete (passive task assignment, mixed tenses, subject-verb disagreement, exact metric, remaining defect qualification), the AI either drops the qualification (*"edge cases"*), alters the metric, or converts the entire sentence into generic marketing fluff.

### Assertion Criteria (With Skill)
* **PASS** if the output:
  1. Resolves tense inconsistency: past simple *built* instead of present *build*.
  2. Resolves subject-verb agreement: *there are some edge cases* instead of *there is some edge cases*.
  3. Retains exact tool: `Redis`.
  4. Retains exact metric: `40%`.
  5. Retains the qualification: Does not hide that edge cases still require fixing.
  6. Preserves the meaning without claim inflation.
