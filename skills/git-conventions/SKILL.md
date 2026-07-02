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

## Worktrees (parallel work only)

Use a worktree **only when agents work concurrently** on the same repo — it gives each an isolated working tree and index. For sequential, single-agent work a plain branch is enough; skip the overhead.

```bash
git worktree add ../repo-feat-my-feature feat/my-feature   # path mirrors branch
cd ../repo-feat-my-feature                                  # commit + push from here
git push -u origin feat/my-feature
git worktree remove ../repo-feat-my-feature                 # add --force to discard changes
```

**Rules:** remove the worktree before declaring the task done; run `git worktree prune` after removal and `git worktree list` to audit stragglers.
