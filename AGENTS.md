# Global Configuration

Loaded in every project. Defines delegation rules, git discipline, and code standards.

## Skill-Based Documentation

Core guidelines have been extracted into focused, auto-loading skills:

| Skill | Triggers | Content |
|-------|----------|---------|
| **task-workflow** | Creating/managing tasks, checking merge readiness | Task lifecycle, file structure, acceptance criteria, deployment checklist |
| **backlog-management** | Adding backlog items, updating status, marking tasks done | Backlog file structure, status lifecycle, sync with task-workflow on completion |
| **git-conventions** | Committing code, creating branches, git operations | Conventional Commits, branch naming, one-change discipline, worktrees |
| **code-standards** | Writing code, linting, PR reviews | Import rules, testing boundaries, style guides, semantic versioning, agent discipline |
| **typescript-coding-guidelines** | Writing/reviewing TS or JS files | Type system, error handling, naming, imports, testing, general TS/JS rules |

Skills auto-load when detected in your work. Load the relevant skill proactively:
- **backlog-management** when: adding backlog items, checking backlog status, marking tasks done, or updating `.agent/backlog.md`
- **task-workflow** when: creating `.agent/tasks/*.md`, promoting tasks, checking merge readiness, or working on task-related operations
- **git-conventions** when: committing code, creating branches, discussing git workflow, or doing git operations
- **code-standards** when: writing/reviewing code, running linters, discussing architecture/testing, or pre-merge validation
- **typescript-coding-guidelines** when: writing or reviewing `.ts`, `.tsx`, `.js`, or `.jsx` files, running ESLint/Biome, or doing TS/JS pre-merge validation

## Quick Reference

**Task workflow:** Create `<type>_<short-description>.md` in `.agent/tasks/` with Status/Goal/Acceptance Criteria/Plan before any code.

**Commits:** `<type>(<scope>): <imperative>` using types `feat`, `fix`, `chore`, `docs`. Branches: `<type>/<short-kebab>`.

**Code:** Consult the `code-standards` skill for language specific instructions.

**Backlog:** All work items tracked in `.agent/backlog.md`. Status: `backlog → active → done`. Update on task completion before removing task file.

**Agent rule:** No code without an active task file. No branch without a matching task. Surface blockers; don't guess.
