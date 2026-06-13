---
name: git-conventions
description: Use when committing, creating branches, or managing git workflow. Covers Conventional Commits format, branch naming, one-change-per-branch discipline, and worktree coordination.
---

# Git Conventions

Enforces Conventional Commits and disciplined branching across all projects.

## Commit Format

### Conventional Commits

All commits follow the format:

```
<type>(<scope>): <imperative verb>

Optional longer description explaining why, not what.
```

**Types:** `feat`, `fix`, `chore`, `docs`

**Examples:**
- `feat(auth): add JWT refresh rotation`
- `fix(search): resolve partial index corruption`
- `chore(deps): bump typescript to 5.1`
- `docs(api): clarify retry backoff behavior`

**Rules:**
- Imperative mood only: "add", not "added" or "adds"
- Lowercase after colon
- No period at end
- Scope is optional but preferred for clarity
- Breaking changes get `!` before colon: `feat!: remove legacy API`

## Branch Naming

```
<type>/<short-kebab-description>
```

**Examples:**
- `feat/user-authentication`
- `fix/cache-invalidation-race`
- `docs/api-endpoint-reference`

Match the commit type to the branch type for consistency.

## Discipline

- **One logical change per branch.** No "WIP" or "misc" commits on shared branches — squash or amend first.
- **Delete branches once merged.** Keep the repo clean.
- **Use Git worktrees for parallel work.** Multiple agents can work in parallel without branch conflicts. Clean up worktrees after.

## Worktree Workflow

For parallel agent work:

```bash
git worktree add /path/to/worktree feat/parallel-feature
# Agent works in /path/to/worktree
git worktree remove /path/to/worktree
```

Each worktree has its own detached state; no cross-contamination.
