# Global Configuration

Loaded in every project. Defines delegation rules, git discipline, and code standards.

## Skill-Based Documentation

Core guidelines have been extracted into focused, auto-loading skills:

| Skill | Triggers | Content |
|-------|----------|---------|
| **task-workflow** | Creating/managing tasks, checking merge readiness | Task lifecycle, file structure, acceptance criteria, deployment checklist |
| **git-conventions** | Committing code, creating branches, git operations | Conventional Commits, branch naming, one-change discipline, worktrees |
| **code-standards** | Writing code, linting, PR reviews | Import rules, testing boundaries, style guides, semantic versioning, agent discipline |

Skills auto-load when detected in your work. **Claude should proactively load them:**
- `/task-workflow` when: creating `.claude/tasks/*.md`, promoting tasks, checking merge readiness, or working on task-related operations
- `/git-conventions` when: committing code, creating branches, discussing git workflow, or doing git operations
- `/code-standards` when: writing/reviewing code, running linters, discussing architecture/testing, or pre-merge validation

You can also load them manually:
```
/task-workflow    # see task management rules
/git-conventions  # see git & branch rules
/code-standards   # see code quality & style rules
```

## Quick Reference

**Task workflow:** Create `<type>_<short-description>.md` in `.claude/tasks/` with Status/Goal/Acceptance Criteria/Plan before any code.

**Commits:** `<type>(<scope>): <imperative>` using types `feat`, `fix`, `chore`, `docs`. Branches: `<type>/<short-kebab>`.

**Code:** Module-level imports only. Strict test/impl separation. Google style guides. Semantic versioning in `package.json` / `pyproject.toml`.

**Agent rule:** No code without an active task file. No branch without a matching task. Surface blockers; don't guess.
