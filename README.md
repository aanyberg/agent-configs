# agent-configs

A collection of specialized agents, skills, and development guidelines for AI coding assistants.

This repository contains:

- **`plugins/conventions`** — A Claude Code plugin bundling the agents and skills below. See [docs/CONSUMER.md](docs/CONSUMER.md) for how a consumer repo loads it via the `lahnvik` marketplace, with no copying into `~/.claude`.
  - **Agents** — Specialized multi-step task runners for common development workflows (feature planning, refactoring, documentation updates, etc.)
  - **Skills** — Focused knowledge modules covering code standards, best practices, and workflows across Python, TypeScript, and general development
- **Instructions** — A single `AGENTS.md` file with project-level guidance that works across all supported tools

These components enhance AI coding assistants by providing domain knowledge, coding conventions, and structured workflows.

## Installation

### Agents & Skills (Claude Code)

Claude Code loads agents and skills via the plugin marketplace at `.claude-plugin/marketplace.json` — see [docs/CONSUMER.md](docs/CONSUMER.md) for the exact `.claude/settings.json` snippet and CLI commands. The old `agents/` and `skills/` symlink targets have moved to `plugins/conventions/agents` and `plugins/conventions/skills`; do not symlink both the plugin and the legacy paths, or skills/agents will load twice.

For tools other than Claude Code that don't support this plugin format, the `agents/` and `skills/` directories at the repo root now only contain a pointer to the new location.

### Global Instructions

`AGENTS.md` is the single source of truth for global instructions. Symlink it to each tool's expected config path:

**Claude Code**
```bash
ln -s /path/to/agent-configs/AGENTS.md ~/.claude/CLAUDE.md
```

**GitHub Copilot**
```bash
mkdir -p ~/.copilot
ln -s /path/to/agent-configs/AGENTS.md ~/.copilot/copilot-instructions.md
```

**OpenAI Codex CLI**
```bash
mkdir -p ~/.codex
ln -s /path/to/agent-configs/AGENTS.md ~/.codex/AGENTS.md
```

Replace `/path/to/agent-configs` with the absolute path to your local clone, e.g. `/home/<username>/projects/agent-configs`.
