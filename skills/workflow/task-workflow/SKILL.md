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
| `planned` | `<root>/.agents/planning/<category>/` | Definition only, no code, no branch |
| `active` | `<root>/.agents/tasks/` | Move from planning OR create directly |

**Filename:** `<type>_<short-description>.md` (e.g. `feat_user-authentication.md`)

**Promoting planned → active:** move file, set `Status: active`, add `Started` datetime and `Branch` field — before any code.

## Task File Structure

```markdown
# <Title>

**Status:** planned | active
**Created:** <datetime>
**Started:** <datetime>      # active only

## Branch                    # active only
`<type>/<short-description>`

## Goal
One paragraph: what and why.

## Acceptance Criteria
- [ ] Criterion one
- [ ] Criterion two

Acceptance criteria should be discussed through questions with the user and refined until they are clear, specific, and testable. They define the conditions for task completion and guide development and testing.

## Plan
Ordered steps. Written before any code. Update + log if it changes.

## Log                       # active only
- `HH:MM` — What was done (past tense, not intent)

## Blockers
Open questions needing human input. In planned tasks these are pre-start blockers and must be resolved before promotion.

## Summary                   # appended before marking done
What was built; deviations from Plan.
```

## Merge Readiness Verification

A branch is **not** merge-ready until every item below has been *verified in the current session*. Verification means running the stated check and observing its result — **not** ticking a box from memory or assumption. Work through the table top to bottom and record evidence as you go.

| # | Item | How to verify | Evidence to capture |
|---|------|---------------|---------------------|
| 1 | All Acceptance Criteria met | Re-read each criterion in the task file; confirm the implementation satisfies it | Each `- [ ]` flipped to `- [x]` in the task file |
| 2 | Tests cover new code | Run the test suite; confirm new/changed code has tests | Test command + pass count |
| 3 | No lint or type errors | Run the linter and type checker | Commands + clean exit |
| 4 | Pre-commit passes | Run the pre-commit hooks across the diff | Command + clean exit |
| 5 | `CHANGELOG.md` updated | Only if public behaviour changed | Diff shown, or "N/A — no public behaviour change" |
| 6 | Version bumped | Only if applicable (`pyproject.toml` / `package.json`) | Old → new version, or "N/A" with reason |
| 7 | Summary appended to task file | Confirm `## Summary` section exists and reflects what was built | Section present |
| 8 | Backlog items for leftovers | Create backlog entries for incomplete Plan steps / unresolved Blockers | Item IDs created, or "none outstanding" |
| 9 | Backlog status updated | Set this task's row to "Done" in `.agents/backlog.md` | Diff shown |
| 10 | Task file removed | After all above pass, delete the file from `.agents/tasks/` or `.agents/planning/` | File no longer present |
| 11 | Branch current with remote main | `git fetch` then confirm branch is rebased/merged on top of `origin/main` with no conflicts | Command + "up to date" |

**Gate — read before claiming "done" or "ready to merge":**

- Do **not** report a task as complete or merge-ready until items 1–11 are each verified with evidence in this session. Stop on the first failure, fix it, then re-verify.
- For every item, state the result explicitly as **pass**, **fail**, or **N/A (reason)**. Silence is not a pass — an unverified item counts as failing.
- A conditional item (5, 6) still requires an explicit decision: state why it does or does not apply.
- If any item cannot be verified (missing tooling, ambiguous criterion), treat it as a **Blocker**, surface it to the user, and do not merge.
- Order matters: item 10 (remove task file) and the "Done" backlog status (item 9) come **last**, only after 1–8 and 11 have passed.

## Agent Discipline

- **No code without task file.** No branch without a matching task file.
- **Plan before code.** Scope freezes once Plan is written — changes require Plan update, logged reason, and human confirmation if significant.
- **Stay scoped.** Do not modify files outside task scope without logging why.
- **Surface blockers.** Architecture, public API, or schema decisions → stop, add to Blockers.
