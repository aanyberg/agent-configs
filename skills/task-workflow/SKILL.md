---
name: task-workflow
description: Use when creating, managing, promoting tasks, or checking merge readiness. Covers task file structure, lifecycle, acceptance criteria, and deployment validation.
---

# Task Workflow

Enforces disciplined task management across the codebase.

## Task Lifecycle

Tasks have two states, each with a directory:

| State | Location | Created via |
|---|---|---|
| `planned` | `<root>/.claude/planning/<category>/` | Definition only, no code, no branch |
| `active` | `<root>/.claude/tasks/` | Move from planning OR create directly |

**Filename:** `<type>_<short-description>.md` (e.g. `feat_user-authentication.md`)

**Promoting planned → active:** move file, set `Status: active`, add `Started` datetime and `Branch` field — before any code.

## Task File Structure

```markdown
# <Title>

**Status:** planned | active
**Created:** <datetime>
**Started:** <datetime>      # active only
**Finished:** <datetime>     # on completion

## Branch                    # active only
`<type>/<short-description>`

## Goal
One paragraph: what and why.

## Acceptance Criteria
- [ ] Criterion one
- [ ] Criterion two

## Plan
Ordered steps. Written before any code. Update + log if it changes.

## Log                       # active only
- `HH:MM` — What was done (past tense, not intent)

## Blockers
Open questions needing human input. In planned tasks these are pre-start blockers and must be resolved before promotion.

## Summary                   # appended before marking done
What was built; deviations from Plan.
```

## Merge Readiness Checklist

Branch is not merge-ready until **ALL** are satisfied:

- [ ] All Acceptance Criteria checked
- [ ] Tests cover new code
- [ ] No lint or type errors
- [ ] Pre-commit passes
- [ ] `CHANGELOG.md` updated (if public behaviour changed)
- [ ] Version bumped in `pyproject.toml` / `package.json` (if applicable)
- [ ] Summary section appended to task file

## Agent Discipline

- **No code without task file.** No branch without a matching task file.
- **Plan before code.** Scope freezes once Plan is written — changes require Plan update, logged reason, and human confirmation if significant.
- **Stay scoped.** Do not modify files outside task scope without logging why.
- **Surface blockers.** Architecture, public API, or schema decisions → stop, add to Blockers.
