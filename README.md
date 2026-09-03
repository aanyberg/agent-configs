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

## Validation

Every change is gated by a structural validation suite that parses the same files
Claude Code parses at load time, so a failure means the plugin would load wrong.

```bash
uv run --frozen pytest tests
```

It runs in well under a second and needs no API access. `.github/workflows/validate.yml`
runs it on every pull request and on pushes to `main`.

What it checks:

| Area | Checks |
| --- | --- |
| Manifests | `marketplace.json` and `plugin.json` parse, agree on descriptions, use semver, and every declared `source` resolves to a real plugin |
| Skills | frontmatter has `name` and `description`, `name` matches the directory, names are unique, descriptions fit the loader budget, and no unrecognised (silently ignored) keys |
| Agents | `name` matches the filename and is kebab-case; `tools`, `model`, `effort`, `maxTurns`, and `permissionMode` are present and valid; `plan`-mode agents declare no write tools |
| References | relative markdown links resolve, shipped scripts are executable with a shebang, and every skill or agent named in prose exists |
| Policy | `policy.example.yml` parses, has exactly one copy, keeps the `backend: auto` line `generate-policy.sh` substitutes, and contains every key the skills read |

Adding a skill or agent needs no test changes — the suite discovers files by glob and
parametrises per file, so each one fails independently with its own path in the failure.
