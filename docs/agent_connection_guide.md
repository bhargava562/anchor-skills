# Skill Shelf — Agent Connection Guide

This guide provides **exact, production-ready copy-paste configurations** to connect any AI agent to the **Skill Shelf Dual-Brain Architecture**:
* **Declarative Memory (Storage Brain)**: Notion Remote MCP (`https://mcp.notion.com/mcp`)
* **Procedural Memory (Functional Brain)**: GitHub Copilot Read-Only MCP (`https://api.githubcopilot.com/mcp/readonly`)

---

## Quick Reference: Environment Variables

Before configuring your agents, export your API keys in your terminal or shell profile (`.bashrc`, `.zshrc`, or Windows Environment Variables):

```bash
# Notion Integration Token (with database read permissions)
export NOTION_API_KEY="ntn_..."

# GitHub Personal Access Token (classic or fine-grained with read:contents)
export GITHUB_TOKEN="ghp_..."
```

On Windows PowerShell:
```powershell
$env:NOTION_API_KEY="ntn_..."
$env:GITHUB_TOKEN="ghp_..."
```

---

## 1. Google Antigravity (Antigravity IDE & CLI)

Google Antigravity natively supports remote HTTP MCP servers and workspace/global rule routing.

### 1.1 MCP Configuration
Add the remote HTTP MCP definitions to your project's `.gemini/mcp_config.json` (or globally at `~/.gemini/antigravity/mcp_config.json`):

```json
{
  "mcpServers": {
    "notion": {
      "url": "https://mcp.notion.com/mcp",
      "headers": {
        "Authorization": "Bearer ${NOTION_API_KEY}"
      }
    },
    "github-copilot-readonly": {
      "url": "https://api.githubcopilot.com/mcp/readonly",
      "headers": {
        "Authorization": "Bearer ${GITHUB_TOKEN}"
      },
      "enabledTools": [
        "get_file_contents",
        "search_code"
      ]
    }
  }
}
```

### 1.2 Global Agent Rules
Create `.gemini/rules/skill-shelf.md` (or globally at `~/.gemini/antigravity/rules/skill-shelf.md`):

```markdown
# Antigravity Skill Shelf Execution Rules

You are integrated with the Skill Shelf Dual-Brain architecture.

## 1. Memory Access
- **Procedural Brain (GitHub)**: Query `github-copilot-readonly` using `search_code` and `get_file_contents`. Do not attempt write operations on the skill shelf.
- **Declarative Brain (Notion)**: Query `notion` for user profile, career evidence, or project records only when scoped context is required.

## 2. Progressive Disclosure Workflow
1. When a user asks for a cognitive or engineering task, check `INDEX.md` at the repository root to determine the correct skill directory.
2. Read `skills/<skill-name>/SKILL.md` (<120 lines). This defines your execution sequence.
3. Read `skills/<skill-name>/overrides.md` to incorporate personal or workspace constraints.
4. Execute the workflow step-by-step.
5. Fetch files in `skills/<skill-name>/references/` on-demand only when a step explicitly requires that reference. Do NOT load references prematurely.
6. Verify your deliverable against the skill's quality rubric before presenting it to the user.
```

---

## 2. Claude Code (Anthropic CLI & Desktop)

Claude Code connects directly to remote HTTP MCP endpoints via `.mcp.json` and respects repo-level instructions in `CLAUDE.md`.

### 2.1 MCP Configuration (`.mcp.json`)
Place this file in your project root or at `~/.claude.json`:

```json
{
  "mcpServers": {
    "notion": {
      "url": "https://mcp.notion.com/mcp",
      "headers": {
        "Authorization": "Bearer ${NOTION_API_KEY}"
      }
    },
    "github-copilot-readonly": {
      "url": "https://api.githubcopilot.com/mcp/readonly",
      "headers": {
        "Authorization": "Bearer ${GITHUB_TOKEN}"
      },
      "enabledTools": [
        "get_file_contents",
        "search_code"
      ]
    }
  }
}
```

### 2.2 System Instructions (`CLAUDE.md`)
Place this file in your project root (`CLAUDE.md`) or at `~/.claude/CLAUDE.md`:

```markdown
# Claude Code — Skill Shelf Operating Instructions

You are operating with access to the Skill Shelf Dual-Brain system:
- **Procedural Memory**: GitHub Copilot Read-Only MCP (`skills/*`)
- **Declarative Memory**: Notion MCP

### Execution Protocol
1. **Route Intent**: When tasked with system design, debugging, code review, brainstorming, or writing, read `INDEX.md` using `get_file_contents` to locate the target skill.
2. **Tier 1 Load**: Read `skills/<name>/SKILL.md` (<120 lines) and `skills/<name>/overrides.md`.
3. **Execute in Phases**: Follow the declared phases in `SKILL.md`.
4. **Tier 2 Just-In-Time Loading**: Load references from `skills/<name>/references/` strictly when entering the step that cites them.
5. **Context Hygiene**: Do not dump entire reference files into conversational responses. Emit only verified deliverables.
```

---

## 3. Codex & OpenCode

For OpenCode, OpenAI Codex, or compatible open agent runners.

### 3.1 MCP Configuration (`opencode.json`)
Place this file in your configuration directory or workspace root:

```json
{
  "$schema": "https://opencode.ai/schema/v1.json",
  "mcp": {
    "servers": [
      {
        "name": "notion",
        "type": "remote",
        "url": "https://mcp.notion.com/mcp",
        "headers": {
          "Authorization": "Bearer ${NOTION_API_KEY}"
        }
      },
      {
        "name": "github-copilot-readonly",
        "type": "remote",
        "url": "https://api.githubcopilot.com/mcp/readonly",
        "headers": {
          "Authorization": "Bearer ${GITHUB_TOKEN}"
        },
        "enabledTools": [
          "get_file_contents",
          "search_code"
        ]
      }
    ]
  }
}
```

### 3.2 Agent Instructions (`AGENTS.md`)
Include this block in your agent system prompt or project `AGENTS.md`:

```markdown
## Skill Shelf Execution Directive
- Prioritize procedural skills in `skills/` over ungrounded reasoning.
- Discover matching skills using `INDEX.md`.
- Read Tier 1 `SKILL.md` (<120 lines) first, merge `overrides.md`, and load `references/*.md` strictly on demand.
- Keep GitHub MCP access strictly read-only (`get_file_contents`, `search_code`).
```

---

## 4. Hermes Agent (Nous Research)

Hermes Agent uses a YAML configuration file (`config.yaml`) paired with a character/persona file (`SOUL.md`).

### 4.1 MCP Configuration (`config.yaml`)
Add the following block to your Hermes `config.yaml`:

```yaml
mcp_servers:
  notion:
    transport: sse
    url: "https://mcp.notion.com/mcp"
    headers:
      Authorization: "Bearer ${NOTION_API_KEY}"

  github_copilot_readonly:
    transport: sse
    url: "https://api.githubcopilot.com/mcp/readonly"
    headers:
      Authorization: "Bearer ${GITHUB_TOKEN}"
    enabled_tools:
      - get_file_contents
      - search_code
```

### 4.2 Soul & Execution Persona (`SOUL.md`)
Place this in your Hermes character/persona directory:

```markdown
# Soul of Hermes — Dual-Brain Operator

You are Hermes, a sharp, disciplined autonomous agent powered by the Skill Shelf Dual-Brain architecture.

## Operating Principles
- **Declarative Memory**: Query Notion MCP to recall user context, active projects, and past architectural decisions.
- **Procedural Memory**: Consult GitHub Copilot Read-Only MCP to retrieve validated execution workflows from `skills/`.
- **Progressive Disclosure**:
  1. Check `INDEX.md` to identify the required skill.
  2. Load `skills/<skill>/SKILL.md` to establish the contract and phase pipeline.
  3. Load `skills/<skill>/overrides.md` to apply user-specific constraints.
  4. Fetch Tier 2 references from `skills/<skill>/references/` on-demand when executing complex evaluation steps.
- **Tone**: Direct, concise, technical, and objective. Eliminate conversational filler.
```

---

## 5. Grok & Meta Muse (Chat-Only / Web / Mobile Interface)

When operating in web or mobile chat interfaces (e.g., Grok 2, ChatGPT Web, Meta AI, or mobile apps) where direct MCP tool calling is unavailable, use **Skill Shelf Bundled Skills**.

### 5.1 Generating Bundled Skills
Run the repo bundling script:
```bash
python scripts/bundle_skills.py
```
This generates single-file, self-contained markdown bundles in `dist/`:
* `dist/core-thinking-bundled.md`
* `dist/brainstorm-and-validate-bundled.md`
* `dist/planning-and-architecture-bundled.md`
* `dist/systematic-debugging-bundled.md`
* `dist/code-review-bundled.md`
* `dist/english-writing-bundled.md`

### 5.2 System Prompt Preamble (Copy-Paste)
Paste this preamble into the Custom Instructions, System Prompt, or initial message of your chat session:

```markdown
You are executing with the Skill Shelf procedural framework.
Below is the bundled skill instructions for this session:

[PASTE CONTENT OF dist/<name>-bundled.md HERE]

### Rules of Engagement:
1. Follow the phases declared in the skill workflow sequentially.
2. Enforce the constraints and validation criteria specified in the bundled rubric.
3. Apply the overrides specified in the bundled overrides section.
4. Output only high-signal deliverables; omit conversational fluff.
```

---

## 6. Verification Checklist

After configuring your agent, verify connectivity with this two-step test:

1. **Verify Procedural Brain (GitHub Read-Only)**:
   Ask your agent:
   > *"Read `INDEX.md` from the GitHub MCP and tell me which skill handles root-cause bug analysis."*
   - Expected Result: The agent calls `get_file_contents("INDEX.md")` and identifies `skills/systematic-debugging/`.
2. **Verify Declarative Brain (Notion)**:
   Ask your agent:
   > *"Query my Notion workspace for recent architecture notes."*
   - Expected Result: The agent calls Notion MCP tools and returns scoped page titles or properties.
