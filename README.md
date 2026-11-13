# Anchor Skills (`skill-shelf`)

> **A provider-independent library of modular AI skills, workflows, and procedural knowledge.**
> Operates as the **Functional Brain** in a decoupled **Dual-Brain architecture**, plugging into any agent runtime like a USB-C drive.

---

## 1. The Dual-Brain "USB-C" Model

Modern AI agents perform best when **declarative memory** (what is true about you or your company) is cleanly separated from **procedural memory** (how work should be executed).

Anchor Skills (`skill-shelf`) implements the **USB-C Model**: a universal, read-only procedural drive that attaches to any agent environment without custom servers or vendor lock-in:

```text
               ┌────────────────────────────────────────────────────────┐
               │              NOTION STORAGE BRAIN                      │
               │             (Declarative Memory)                       │
               │  - Personal & organization profile                     │
               │  - Career history, accomplishments, and goals          │
               │  - Active project status & live facts                  │
               │  URL: https://mcp.notion.com/mcp                       │
               └──────────────────────────┬─────────────────────────────┘
                                          │
                        Query on demand   │   (OAuth / Remote MCP)
                                          ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AI AGENT RUNTIME                                     │
│          Google Antigravity  │  Claude Code  │  Codex  │  Hermes Agent           │
│                                                                                  │
│   Discovers intent via INDEX.md -> Ingests SKILL.md (<120 lines) -> Executes     │
└─────────────────────────────────────────▲────────────────────────────────────────┘
                                          │
                                    "Plug-in" (Local FS / Copilot MCP)
                                          │
               ┌──────────────────────────┴─────────────────────────────┐
               │             GITHUB FUNCTIONAL BRAIN                    │
               │             (`skill-shelf` Repository)                 │
               │  - Modular cognitive & engineering workflows           │
               │  - Strict agentskills.io format & <120 line limits     │
               │  - Evaluation rubrics, mental models, & ADR templates  │
               │  URL: https://api.githubcopilot.com/mcp/readonly       │
               └────────────────────────────────────────────────────────┘
```

### Key Principles of the Dual-Brain Architecture
1. **Passive & Zero-Server**: Neither brain requires a proprietary hosting daemon, Python backend, or custom vector database. They are standard markdown files exposed via native tools or standardized remote HTTP MCP endpoints.
2. **Zero Personal Data in GitHub**: `skill-shelf` contains zero personal biographies, credentials, or private notes. It is 100% portable, reusable, and team-sharable. Personal context lives exclusively in Notion.
3. **Provider Agnostic**: The exact same skills run identically in Google Antigravity, Claude Code, OpenAI Codex/OpenCode, and Hermes Agent.

---

## 2. Skill Catalog & Intent Routing

`skill-shelf` provides 6 core foundation skills across Cognitive, Engineering, and Communication domains. Every skill is cataloged in [`INDEX.md`](INDEX.md):

| Category | Skill Name | Primary Capability | Entry Point |
| :--- | :--- | :--- | :--- |
| **Cognitive** | [`core-thinking`](skills/core-thinking/SKILL.md) | First-principles decomposition, weighted trade-off matrices, preemptive failure-mode analysis, and high-density reasoning. | `skills/core-thinking/SKILL.md` |
| **Cognitive / Product** | [`brainstorm-and-validate`](skills/brainstorm-and-validate/SKILL.md) | 4-step wedge discovery, competitor & ROI gating, interactive scope refinement via one-question-at-a-time loop. | `skills/brainstorm-and-validate/SKILL.md` |
| **Engineering** | [`planning-and-architecture`](skills/planning-and-architecture/SKILL.md) | System design, SOLID & Clean Code boundaries, thin controllers, ADR creation, and phased bite-sized task plans. | `skills/planning-and-architecture/SKILL.md` |
| **Engineering** | [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | 4-phase causal root-cause tracing before code changes, minimal reproduction tests, surgical fixes, and regression suites. | `skills/systematic-debugging/SKILL.md` |
| **Engineering** | [`code-review`](skills/code-review/SKILL.md) | Multi-file diff inspection, subagent verification, severity grading (Critical, Important, Minor), and red-flag audits. | `skills/code-review/SKILL.md` |
| **Communication** | [`english-writing`](skills/english-writing/SKILL.md) | Grammar, sentence rhythm, professional tone calibration, and prose economy while strictly freezing factual claims. | `skills/english-writing/SKILL.md` |

For automated routing rules and conversational prompt mappings, consult [`INDEX.md`](INDEX.md).

---

## 3. Engineering Rigor: OOP, SOLID, and Progressive Disclosure

Instructions are organized with the same discipline as high-reliability software architectures:

| Principle | Implementation in `skill-shelf` |
| :--- | :--- |
| **Single Responsibility (SRP)** | Primary `SKILL.md` acts purely as an orchestration manifest. Reference heuristics belong in `references/`, templates in `assets/`, and examples in `examples/`. |
| **Strict Token Budgeting** | All new `SKILL.md` files are strictly constrained to **<120 lines**. Deep checklists are loaded on demand, never upfront. |
| **Open / Closed (Base + Overrides)** | Canonical skills remain unmodified. Personal, organizational, or repository preferences are injected via [`overrides.md`](AGENTS.md#4-the-base--overrides-pattern-overridesmd) using `ADD`, `REPLACE`, `RESTRICT`, and `PRIORITISE` directives. |
| **Interface Segregation** | Skills declare minimal resource needs. Agents use strict read-only tool allowlists (`get_file_contents`, `search_code`, `read_resource`). |
| **Dependency Inversion** | Skills depend on abstract capabilities (e.g., "requires test runner", "optional web search"), never hardcoded proprietary vendor APIs. |

---

## 4. Repository Structure

```text
skill-shelf/
├── README.md                           # Architecture, quickstart, & USB-C model
├── INDEX.md                            # Master intent-to-skill routing table
├── AGENTS.md                           # Repository governance & skill standards
├── docs/                               # System architecture & connection guides
│   ├── architecture.md                 # Dual-Brain & remote HTTP MCP deep dive
│   ├── design_principles.md            # Progressive disclosure & context hygiene
│   ├── agent_connection_guide.md       # Copy-paste configs for all major runtimes
│   └── roadmap.md                      # Evolution phases & milestones
├── scripts/                            # Validation, bundling, and synchronization tooling
│   ├── validate_skills.py              # Schema, line-count, and link integrity checker
│   ├── bundle_skills.py                # Single-file chat bundler (dist/*.md)
│   ├── sync.ps1                        # Native Windows PowerShell sync script
│   └── sync.sh                         # POSIX bash sync script
├── dist/                               # Bundled standalone skills for chat/mobile
└── skills/                             # Domain skill packages
    ├── core-thinking/
    │   ├── SKILL.md                    # Primary workflow (<120 lines)
    │   ├── overrides.md                # Local override directives
    │   └── references/mental-models.md
    ├── brainstorm-and-validate/
    │   ├── SKILL.md
    │   ├── overrides.md
    │   └── references/
    ├── planning-and-architecture/
    │   ├── SKILL.md
    │   ├── overrides.md
    │   ├── assets/adr-template.md
    │   └── references/
    ├── systematic-debugging/
    │   ├── SKILL.md
    │   ├── overrides.md
    │   └── references/
    ├── code-review/
    │   ├── SKILL.md
    │   ├── overrides.md
    │   └── references/
    └── english-writing/
        ├── SKILL.md
        ├── overrides.md
        ├── examples/
        ├── references/
        └── tests/
```

---

## 5. Quickstart

### 5.1 Local Agent Synchronization (Symlink / Copy)
To make all skills immediately accessible to your local agent CLIs and IDEs, run the sync script:

**Windows PowerShell:**
```powershell
./scripts/sync.ps1
```

**Linux / macOS Bash:**
```bash
chmod +x ./scripts/sync.sh
./scripts/sync.sh
```
This links or copies skills to standard discovery directories:
- `~/.gemini/skills/` (Google Antigravity)
- `~/.claude/skills/` (Claude Code)
- `~/.codex/skills/` (OpenAI Codex / OpenCode)
- `~/.hermes/skills/` (Hermes Agent)

### 5.2 Validate Skill Compliance
Ensure all skills meet `agentskills.io` frontmatter specifications, link validity, line count constraints (<120 lines), and `overrides.md` presence:

```bash
python scripts/validate_skills.py
```

### 5.3 Bundle Skills for Chat & Mobile Pasting
If using a web or mobile LLM interface without MCP filesystem access, generate standalone bundled markdown documents:

```bash
python scripts/bundle_skills.py
```
Output files are generated in `dist/<skill-name>-bundled.md`.

---

## 6. MCP Connection Overview

`skill-shelf` connects to modern agent runtimes via **Model Context Protocol (MCP)**:

### 6.1 Remote HTTP MCP Setup (Zero Local Servers)
Connect agents to the Dual-Brain using native cloud MCP endpoints:

* **GitHub Functional Brain**:
  - URL: `https://api.githubcopilot.com/mcp/readonly`
  - Read-Only Tools: `get_file_contents`, `search_code`
* **Notion Declarative Brain**:
  - URL: `https://mcp.notion.com/mcp`
  - Auth: Standard OAuth 2.0

### 6.2 Local Filesystem Configuration
When running locally, expose `skill-shelf` via filesystem MCP or native workspace mounting:

#### Google Antigravity (`mcp_config.json`):
```json
{
  "mcpServers": {
    "skill-shelf": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:\\skill-shelf"]
    }
  }
}
```

#### Claude Code (`.mcp.json`):
```json
{
  "mcpServers": {
    "skill-shelf": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/skill-shelf"]
    }
  }
}
```

Detailed step-by-step setup guides for all runtimes (including Antigravity, Claude Code, Codex, and Hermes) are provided in [`docs/agent_connection_guide.md`](docs/agent_connection_guide.md).

---

## 7. Governance & Contribution Rules

All contributors and AI agents must follow the governance rules documented in [`AGENTS.md`](AGENTS.md):
- **Name Invariant**: Skill folder name must match frontmatter `name` (lowercase-hyphenated).
- **Line Limit**: `<120 lines` for new `SKILL.md` files (legacy exemption for `english-writing`).
- **Base + Overrides**: Never modify canonical workflows for local quirks; use `overrides.md`.
- **Zero Bio & Zero Secrets**: Never commit personal PII, credentials, or proprietary API keys.
- **Verification**: All PRs must pass `python scripts/validate_skills.py`.
