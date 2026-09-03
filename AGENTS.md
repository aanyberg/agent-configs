# Global Configuration

## When to Load Skills

| Trigger | Skill |
|---------|-------|
| Listing, creating, claiming, releasing, de-duplicating work items; checking what is in flight; any "add to backlog" or "update status" | `backlog-management` |
| Creating/managing tasks, checking merge readiness, running autonomously as an agent or subagent | `task-workflow` |
| Architectural decisions, new services/modules, tech choices | `architecture-planning` |
| Committing, branching, PRs, worktrees, git operations | `git-conventions` |
| Reviewing a PR or branch, acting as independent reviewer | `code-review` |
| Writing/reviewing code, linting | `code-standards` + the language guideline skill |
| Writing/updating docs, READMEs, changelogs, role/layer docs | `docs-standards` |
| Auditing code health, prioritising refactors | `tech-debt` |

## Quick Reference

**Policy:** `<root>/.planning/policy.yml` is read before any action that creates items, branches, or PRs. It defines backend, ID scheme, statuses, commit types, branch format, versioning, and autonomous limits. Missing file means single-agent work with skill defaults.
**Backlog:** only via `backlog-management`. Backend (`github-issues` or `BACKLOG.md`) resolved from policy, never assumed. Status `backlog → ready → active → in-review → done`, side states `blocked`, `cancelled`. Agents select `ready` + `agent-safe` only; only triage or a human sets those.
**Task:** `<type>_<short-description>.md` in `.planning/tasks/` with Backlog ID, Status, Goal, Acceptance Criteria, Plan before any code.
**Commits:** `<type>(<scope>): <imperative>`, types from policy (default `feat`, `fix`, `chore`, `docs`, `refactor`, `test`). Branches `<type>/<id>-<short-kebab>`.
**Architecture:** record decisions as ADRs in `.planning/architecture.md`. Structural choices are blockers: surface and confirm, or set `blocked` when autonomous.
**Agent rule:** no branch without a claimed item, no item without evidence, no code without a task file. Surface blockers, do not guess. Never force push, edit branch protection, add a dependency, or delete a test without a human.
**Migration:** if a project still has `.agents/tasks/`, `.agents/planning/`, `.agents/architecture.md`, or `.agents/backlog.md`, migrate to `.planning/` and root `BACKLOG.md` automatically before proceeding (see `task-workflow` and `backlog-management`).
