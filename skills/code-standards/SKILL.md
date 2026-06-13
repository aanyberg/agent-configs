---
name: code-standards
description: Use when writing code, running linters, or reviewing pull requests. Covers imports, testing boundaries, style guides, semantic versioning, and agent discipline.
---

# Code Standards

Enforces consistent code quality and architectural boundaries.

## General Rules

### Testing Boundaries
- **Strict separation:** no implementation in test files, no test code in implementation files.
- Test files are for validation; implementation files are for logic.
- Shared test utilities go in a dedicated `test-utils` or `testing` module.

### Style Guides
- `/python-best-practices` when: writing Python code, running linters, discussing architecture/testing, or pre-merge validation for Python code.
- `/typescript-coding-guidelines` when: writing TypeScript or JavaScript code, running ESLint/Biome, discussing TS architecture/testing, or pre-merge validation for TS/JS code.

### Semantic Versioning
- **Source of truth:** `pyproject.toml` (Python) or `package.json` (Node.js/TypeScript)
- Format: `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)
- Bump version when cutting a release alongside a commit that updates CHANGELOG.md

### Conciseness
- Answers are short, no loss of information.
- "Fix this: X" > "We need to fix this: X"
- Comments explain *why*, not *what*; code is self-documenting.
