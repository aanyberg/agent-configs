# Global Configuration

## When to Load Skills

| Trigger | Skill |
|---------|-------|
| Creating/managing tasks, checking merge readiness | `task-workflow` |
| Architectural decisions, new services/modules, tech choices | `architecture-planning` |
| Backlog updates or status changes | `backlog-management` |
| Committing, branching, git operations | `git-conventions` |
| Writing/reviewing code, linting, PR reviews | `code-standards` |

## Quick Reference

**Task:** `<type>_<short-description>.md` in `.agent/tasks/` with Status/Goal/Acceptance Criteria/Plan before any code.  
**Commits:** `<type>(<scope>): <imperative>` — types: `feat`, `fix`, `chore`, `docs`. Branches: `<type>/<short-kebab>`.  
**Architecture:** Record decisions as ADRs in `architecture.md`. Structural choices are blockers — surface and confirm before coding.  
**Backlog:** `.agent/backlog.md` — status: `backlog → active → done`. Update on task completion before removing task file.  
**Agent rule:** No code without a task file. No branch without a matching task. Surface blockers; don't guess.
