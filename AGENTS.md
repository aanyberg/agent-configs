# Global Configuration

## When to Load Skills

| Trigger | Skill |
|---------|-------|
| Creating/managing tasks, checking merge readiness | `task-workflow` |
| Architectural decisions, new services/modules, tech choices | `architecture-planning` |
| Backlog updates or status changes | `backlog-management` |
| Committing, branching, git operations | `git-conventions` |
| Writing/reviewing code, linting, PR reviews | `code-standards` |
| Writing/updating docs, READMEs, changelogs, role/layer docs | `docs-standards` |

## Quick Reference

**Task:** `<type>_<short-description>.md` in `.planning/tasks/` with Status/Goal/Acceptance Criteria/Plan before any code.  
**Commits:** `<type>(<scope>): <imperative>` — types: `feat`, `fix`, `chore`, `docs`. Branches: `<type>/<short-kebab>`.  
**Architecture:** Record decisions as ADRs in `architecture.md`. Structural choices are blockers — surface and confirm before coding.  
**Backlog:** `BACKLOG.md` (project root) — status: `backlog → active → done`. Update on task completion before removing task file.  
**Agent rule:** No code without a task file. No branch without a matching task. Surface blockers; don't guess.
**Migration:** If a project still has `.agents/tasks/`, `.agents/planning/`, `.agents/architecture.md`, or `.agents/backlog.md`, migrate them to `.planning/` and root `BACKLOG.md` automatically before proceeding (see **task-workflow** and **backlog-management**).
