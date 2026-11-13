# English Writing — Overrides & Configuration

This file provides project-level and user-specific configuration overrides for the `english-writing` skill. Modify these settings to tune default operating modes, tone guidelines, and vocabulary rules.

---

## 1. Operating Mode Override

* **Default**: `Mode B` (Clarity Improvement)
* **Options**:
  * `Mode A` (Grammar Correction only - minimal changes)
  * `Mode B` (Clarity Improvement - moderate targeted edits)
  * `Mode C` (Professional Rewrite - controlled restructuring)
  * `Mode D` (Review & Critique - diagnostic output)
  * `Mode E` (Composition & Content Generation - original composition)

```yaml
default_mode: Mode B
```

---

## 2. Style & Tone Preferences

```yaml
style_preferences:
  dialect: US_English        # Options: US_English, UK_English
  oxford_comma: true         # Enforce Oxford comma
  active_voice_bias: true    # Prefer active voice over passive voice
  formality_level: high      # Options: casual, standard, high
```

---

## 3. Domain Terminology & Protected Terms

List terms that must never be modified, rewritten, or simplified:

* Specific product names, brand names, and trademarked terms
* Code-level symbols, API methods, and variable names
* Technical acronyms (e.g., ADR, BLUF, JTBD, RICE, SLA)
