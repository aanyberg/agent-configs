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
- **Use Git worktrees for parallel work.** Multiple agents can work in parallel without branch conflicts. **Removing the worktree is mandatory before declaring a task done.**

## Worktree Workflow

For parallel agent work **worktree isolation is a must**. Each agent should operate in its own worktree to avoid conflicts and maintain clean branch states.

### Lifecycle

```bash
# 1. Create — give the worktree a path that mirrors the branch name
git worktree add ../repo-feat-my-feature feat/my-feature

# 2. Work — all commits happen inside the worktree directory
cd ../repo-feat-my-feature
# ... make changes, commit ...

# 3. Push
git push -u origin feat/my-feature

# 4. Cleanup — do this before declaring the task done
git worktree remove ../repo-feat-my-feature
```

### Rules

- **Always remove the worktree when done.** Do not leave worktrees behind after a task is complete or abandoned.
- If the worktree has uncommitted changes that must be discarded, use `--force`:
  ```bash
  git worktree remove --force ../repo-feat-my-feature
  ```
- After removing, prune any stale metadata Git may have kept:
  ```bash
  git worktree prune
  ```
- Audit open worktrees at any time with:
  ```bash
  git worktree list
  ```

Each worktree has its own isolated working tree and index — no cross-contamination between agents.
