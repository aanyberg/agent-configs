# agent-configs

A collection of specialized agents, skills, and development guidelines for AI coding assistants.

This repository contains:

- **Agents** — Specialized multi-step task runners for common development workflows (feature planning, refactoring, documentation updates, etc.)
- **Skills** — Focused knowledge modules covering code standards, best practices, and workflows across Python, TypeScript, and general development
- **Instructions** — A single `AGENTS.md` file with project-level guidance that works across all supported tools

These components enhance AI coding assistants by providing domain knowledge, coding conventions, and structured workflows.

## Installation

### Agents & Skills

Agents and skills can be symlinked into compatible tools to provide immediate access to their capabilities:

**Claude Code Example** — reads agents from `~/.claude/agents/` and skills from `~/.claude/skills/`:
```bash
ln -s /path/to/agent-configs/agents ~/.claude/agents
ln -s /path/to/agent-configs/skills ~/.claude/skills

```

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

**OpenCode**
```bash
mkdir -p ~/.opencode
ln -s /path/to/agent-configs/AGENTS.md ~/.opencode/AGENTS.md
```

Replace `/path/to/agent-configs` with the absolute path to your local clone, e.g. `/home/<username>/projects/agent-configs`.
