# Anchor Core — Phased Implementation Roadmap

Anchor Core is developed incrementally in disciplined, testable milestones. We do not attempt to build the entire system at once. Each phase proves a critical architectural concept before expanding scope.

---

## 1. Overview of Phases

```mermaid
graph LR
    P1[Phase 1: Resume Generator] --> P2[Phase 2: External Skill + Overlay]
    P2 --> P3[Phase 3: Provider Adapters]
    P3 --> P4[Phase 4: Notion Memory]
    P4 --> P5[Phase 5: Capability Engine]
    P5 --> P6[Phase 6: Multi-Tier Validation]
    P6 --> P7[Phase 7: Cache & Memoisation]
    P7 --> P8[Phase 8: Emergency Medpack]
    P8 --> P9[Phase 9: Additional Skills]
    P9 --> P10[Phase 10: Automation & Cloud]
```

---

## 2. Phase-by-Phase Deliverables

### Phase 1: Resume Generator (Current Active Milestone)
* **Goal**: Build one high-quality, provider-neutral Resume Generator Skill while proving the foundational architecture.
* **Key Deliverables**:
  * Input schema validation (JD, Candidate Memory, Old Resume, Layout overrides).
  * Decoupled Content Engine vs. Layout Engine.
  * Central design tokens in `config/resume.yaml` (typography, margins, column ratios).
  * Swappable `PDFRenderer` interface with ReportLab implementation.
  * One-Analysis / One-Fix pipeline with consolidated Issue Manifest.
  * Guaranteed 1-page output (2-column default, 1-column override).
  * ATS extractability validation and zero-fabrication evidence mapping.
* **Scope Discipline**: No cloud runtime, no complex database, no automated multi-provider compiler.

### Phase 2: External Skill + Personal Overlay
* **Goal**: Prove that mature external skills (such as `obra/superpowers`) can be consumed directly as upstream dependencies without cloning or modifying their repositories.
* **Key Deliverables**:
  * Overlay syntax and parser (`ADD`, `REPLACE`, `RESTRICT`, `PRIORITISE`).
  * Deterministic conflict resolution hierarchy (Safety > Hard Constraints > Provider Limits > Defaults).
  * Personal engineering overlays (e.g., systematic debugging overlay that enforces root-cause explanation before code edits).
* **Scope Discipline**: Deterministic rule composition only; no heuristic AI conflict engine.

### Phase 3: Provider Adapter & Portability
* **Goal**: Prove that the universal skill contract can be executed across distinct AI environments without altering the core skill definition.
* **Key Deliverables**:
  * Provider research dossiers (Claude, Gemini, OpenAI).
  * Adapters for Claude Code / Desktop (`.claude/skills`).
  * Adapters for Gemini Antigravity (`.gemini/skills`).
  * Verification that skill definitions execute identically across both targets.

### Phase 4: Optional Memory Integration (Anchor-Brain)
* **Goal**: Connect the personal memory layer (Notion) to skills via a clean, abstract `MemoryProvider` interface.
* **Key Deliverables**:
  * `MemoryProvider` interface and `NotionMemoryAdapter`.
  * Scoped query engine (`identity.*`, `experience.backend`, `projects.relevant`).
  * Enforcement of visibility boundaries (L0–L4) at retrieval time.
  * Principle of least privilege: zero ambient context leakage.

### Phase 5: Dependency & Capability Resolution
* **Goal**: Formalize automated capability checking and dependency verification before task execution.
* **Key Deliverables**:
  * Automated capability validator (`memory: optional/required`, `web: optional`, `codebase: optional`).
  * Environment prerequisite checks (Python, ReportLab, CLI tools).
  * Graceful degradation paths when optional capabilities are offline.

### Phase 6: Multi-Tier Validation System
* **Goal**: Formalize mechanical, semantic, and security validation into an extensible test harness.
* **Key Deliverables**:
  * Deterministic structural validators (page count, margin overflow, PDF corruption).
  * Semantic linting (grammar, tense consistency, action verb impact).
  * Evidence provenance validator (every resume bullet maps to a verified Notion record).
  * Redaction audit tool (ensuring L2/L3 data never enters public outputs).

### Phase 7: Artifact Cache & Memoisation
* **Goal**: Prevent redundant, expensive LLM calls by introducing input-aware caching.
* **Key Deliverables**:
  * Artifact metadata schema (`input_hash`, `memory_version`, `skill_version`, `template_version`).
  * Local filesystem artifact store with metadata indexing.
  * Re-generation short-circuiting when inputs and dependencies are unchanged.

### Phase 8: Emergency Medpack (Degraded Fallback)
* **Goal**: Provide a lightweight, portable fallback workflow when operating in restricted environments (e.g., mobile devices, offline, missing dependencies).
* **Key Deliverables**:
  * Zero-dependency text/markdown resume and workflow generator.
  * Explicit assumption and missing-evidence logging.
  * Post-recovery reconciliation guide to sync changes back to desktop/Notion.

### Phase 9: Additional Personal Skills
* **Goal**: Expand the Anchor Skills library across professional and technical domains.
* **Candidate Skills**:
  * Cover Letter Generator (paired with Resume Skill).
  * LinkedIn Content & Profile Sync.
  * Hackathon Opportunity & Feasibility Evaluator.
  * Technical Deep-Dive & Research Digest.
  * Code Review & Architecture Critique (with personal overlay).

### Phase 10: Automation, Cloud & Future Management
* **Goal**: Optional scheduled workflows, notifications, and application tracking.
* **Candidate Capabilities**:
  * n8n integration for scheduled job alerts.
  * Application status tracking and follow-up reminders.
  * Automated periodic sync between Notion brain and local cache.
