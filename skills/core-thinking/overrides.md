# Core Thinking — Overrides & Configuration

This file provides project-level and user-specific configuration overrides for the `core-thinking` skill. Modify these settings to tune decision thresholds, rigor levels, and communication formats.

---

## 1. Decision Rigor Level

* **Default**: `Balanced`
* **Options**:
  * `Iterative` (Bias for action; minimal pre-mortem; fast prototypes; Type 2 focus)
  * `Balanced` (Standard first-principles analysis; 3 failure modes; trade-off matrix)
  * `Defensive` (Exhaustive pre-mortem; formal ADR requirements; Type 1 irreversible scrutiny)

```yaml
rigor_level: Balanced
```

---

## 2. Priority Dimension Weighting

Define which dimension takes precedence when evaluating trade-offs in this project:

```yaml
tradeoff_priorities:
  simplicity_over_optimization: true
  developer_velocity_over_raw_throughput: true
  open_standards_over_proprietary_features: true
  operational_resilience_over_feature_breadth: true
```

---

## 3. Communication Constraints

```yaml
communication:
  bluf_enforced: true
  max_recommendation_bullets: 4
  show_visible_tradeoffs: true
  suppress_conversational_filler: true
```

---

## 4. Domain Invariants & Hard Constraints

List absolute system invariants that all proposed solutions must respect (e.g., zero data loss, specific cloud providers, cost caps):

* Invariant 1: Any solution must support standard headless execution.
* Invariant 2: No introduction of external proprietary daemons or unapproved SaaS dependencies.
* Invariant 3: P99 latency SLA must remain under 200ms.
