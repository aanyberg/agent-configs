---
name: code-standards
description: Use when writing code, running linters, or reviewing pull requests. Covers imports, testing boundaries, style guides, semantic versioning, and agent discipline.
---

# Code Standards

Enforces consistent code quality and architectural boundaries.

## General Rules

### Imports
- **Module level only.** Never inside functions, conditionals, or class bodies. Any language.
- Violating this causes bloat, circular dependencies, and hidden performance issues.

### Testing Boundaries
- **Strict separation:** no implementation in test files, no test code in implementation files.
- Test files are for validation; implementation files are for logic.
- Shared test utilities go in a dedicated `test-utils` or `testing` module.

### Style Guides
- **Python:** Google Python Style Guide (non-negotiable)
- **TypeScript/JavaScript:** Google TypeScript Style Guide (non-negotiable)
- Enforce via linters (pylint, eslint) and pre-commit hooks.

### Semantic Versioning
- **Source of truth:** `pyproject.toml` (Python) or `package.json` (Node.js/TypeScript)
- Format: `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)
- Bump version when cutting a release alongside a commit that updates CHANGELOG.md

### Conciseness
- Answers are short, no loss of information.
- "Fix this: X" > "We need to fix this: X"
- Comments explain *why*, not *what*; code is self-documenting.

## Agent Discipline

### Pre-Code Checklist
- [ ] Active task file exists in `.claude/tasks/`
- [ ] Task has Goal, Plan, and Acceptance Criteria
- [ ] Branch name matches task type and description
- [ ] Plan is written before code (scope freeze point)

### During Implementation
- [ ] Update task file's Log section as work progresses
- [ ] Do not modify files outside task scope; log if necessary
- [ ] Commit frequently with Conventional Commits
- [ ] Surface blockers immediately — don't guess

### Pre-Merge Checklist
- [ ] All Acceptance Criteria satisfied
- [ ] Tests cover new code paths
- [ ] No lint or type errors
- [ ] Pre-commit hooks pass
- [ ] CHANGELOG.md updated (if behavior changed)
- [ ] Version bumped in metadata files
- [ ] Task Summary section filled in
