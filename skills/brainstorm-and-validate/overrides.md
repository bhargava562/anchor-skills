# Brainstorm & Validate — Overrides & Configuration

This file provides project-level and user-specific configuration overrides for the `brainstorm-and-validate` skill. Modify these settings to tune validation rigor, ROI thresholds, and interview protocols.

---

## 1. Validation Rigor & Hurdle Rates

```yaml
validation_rigor:
  min_roi_score_to_proceed: 15     # Minimum score (1–25) to greenlight implementation
  pivot_threshold: 10              # Below this score, feature is killed outright
  require_competitor_audit: true    # Enforce status-quo and alternative evaluation
  require_fatal_flaw_check: true   # Enforce platform risk and unit economics review
```

---

## 2. Interactive Interview Cadence

```yaml
interview_preferences:
  strict_single_question_loop: true  # Ask exactly one question per turn
  max_playback_words: 200            # Word limit for playback summaries
  propose_defaults_automatically: true # Offer opinionated defaults when user is undecided
  explore_anti_goals_upfront: true   # Explicitly uncover failure conditions early
```

---

## 3. Target Domain & Beachhead Defaults

Configure the primary customer and environment context for faster discovery:

```yaml
domain_context:
  default_icp: "Senior Software Engineers & AI Systems Architects"
  deployment_target: "Local Agent Runtime / Remote MCP"
  acceptable_time_to_value_minutes: 5
```

---

## 4. Protected Product Principles

List inviolable product tenets that cannot be compromised during brainstorming or feature additions:

* Tenet 1: Zero vendor lock-in for critical application state.
* Tenet 2: Low-friction adoption must precede complex multi-step configuration.
* Tenet 3: Deliver immediate local utility before requiring network synchronization.
