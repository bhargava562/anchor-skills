# Architecture Decision Record (ADR) Template

# ADR-[NUMBER]: [SHORT TITLE OF DECISION]

* **Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]
* **Date**: [YYYY-MM-DD]
* **Deciders**: [List of decision makers and stakeholders]
* **Technical Domain**: [e.g., Storage, Authentication, Caching, Messaging]

---

## 1. Context & Problem Statement
Describe the architectural context, problem, and operational reality driving this decision.
* What is the current technical limitation or challenge?
* What changed in requirements, scale, or constraints?
* What are the specific non-functional requirements (latency, throughput, cost, developer velocity)?

---

## 2. Decision Drivers
List the key forces and constraints shaping the choice:
1. [Driver 1, e.g., Must support 10,000 writes/sec without distributed deadlocks]
2. [Driver 2, e.g., Must maintain sub-50ms p99 read latency]
3. [Driver 3, e.g., Must avoid vendor lock-in for data storage]
4. [Driver 4, e.g., Team familiarity and operational overhead]

---

## 3. Considered Options

### Option 1: [Option Name, e.g., PostgreSQL with Partitioning]
* **Overview**: Brief description of this approach.
* **Pros**:
  * [Advantage 1]
  * [Advantage 2]
* **Cons**:
  * [Disadvantage 1]
  * [Disadvantage 2]

### Option 2: [Option Name, e.g., DynamoDB / NoSQL Document Store]
* **Overview**: Brief description of this approach.
* **Pros**:
  * [Advantage 1]
  * [Advantage 2]
* **Cons**:
  * [Disadvantage 1]
  * [Disadvantage 2]

---

## 4. Decision Outcome
* **Chosen Option**: [Option Name]
* **Justification**:
  [Explain why this option best addresses the decision drivers above. Acknowledge trade-offs explicitly.]

---

## 5. Consequences & Trade-offs

### Positive Consequences
* [Benefit 1: e.g., Simplified local development and testing environment]
* [Benefit 2: e.g., ACID transactions guaranteed across account balances]

### Negative Consequences & Risks
* [Trade-off 1: e.g., Requires manual sharding strategy once table exceeds 2TB]
* [Mitigation 1: e.g., Partition by tenant_id from inception]

---

## 6. Compliance & Verification
How will we verify that code adheres to this decision over time?
* [e.g., Linter rule forbidding direct database queries outside the repository package]
* [e.g., Automated integration test verifying query latency under simulated load]
