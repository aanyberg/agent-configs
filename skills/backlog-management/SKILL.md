---
name: backlog-management
description: Use when managing the project backlog, adding new backlog items, updating item status, or marking tasks as done. Covers backlog file structure, status lifecycle, and sync with task-workflow on task completion.
---

# Backlog Management

Maintains a single source of truth for all work items across every state — from idea to done.

## Backlog File Location

Each project root keeps its backlog at:

```
<root>/BACKLOG.md
```

This is a project-root file (like `README.md`), never a global tool directory — so it's visible and discoverable alongside the rest of the project.

If the file does not exist, create it with the header and empty table before adding the first item.

## Legacy Layout Migration

Older projects may still have a backlog at `<root>/.agents/backlog.md`. Before reading or writing the backlog, check once per project:

1. If `<root>/.agents/backlog.md` exists and `<root>/BACKLOG.md` does not, move it to `<root>/BACKLOG.md`.
2. Update any `Task File` values still pointing at `.agents/tasks/...` or `.agents/planning/...` to their `.planning/tasks/...` or `.planning/planned/...` equivalents (see **task-workflow**'s migration step).
3. Do this silently and automatically — it is additive and safe. Do not ask for confirmation.

## Backlog File Structure

`BACKLOG.md` holds two tables: the **live table** (`backlog`/`active` rows you check daily)
and an **Archive** (terminal `done`/`cancelled` rows). Same file, same columns — see
[Archiving Resolved Items](#archiving-resolved-items).

```markdown
# Backlog

| ID | Title | Type | Priority | Status | Task File | Depends On | Created | Acceptance Criteria Summary | Notes |
|----|-------|------|----------|--------|-----------|------------|---------|--------------------|-------|
| 001 | Short imperative description | feat | high | backlog | — | — | 2025-01-30 | Feature X should contain xyz | Optional context |

## Archive

| ID | Title | Type | Priority | Status | Task File | Depends On | Created | Acceptance Criteria Summary | Notes |
|----|-------|------|----------|--------|-----------|------------|---------|--------------------|-------|
```

### Column Definitions

| Column | Values / Format | Notes |
|--------|----------------|-------|
| **ID** | Zero-padded integer (`001`, `002`, …) | Monotonically increasing; never reused |
| **Title** | Short imperative phrase | What the work achieves |
| **Type** | `feat`, `fix`, `chore`, `docs`, `refactor` | Matches conventional-commit type |
| **Priority** | `high`, `medium`, `low` | Set by human; agent may suggest |
| **Status** | See lifecycle below | |
| **Task File** | Relative path or `—` | Link once a task file is created |
| **Depends On** | ID(s) (e.g. `009`) or `—` | This item is blocked by the referenced ID(s); structured, queryable — mirrors `todo_deps` |
| **Created** | ISO date (`YYYY-MM-DD`) | Set once, at creation; never edited. Supports staleness review |
| **Notes** | Free text | Links, scope limits, completion/cancellation reason |

## Status Lifecycle

```
backlog → active → done
              ↓
          cancelled
```

| Status | Meaning |
|--------|---------|
| `backlog` | Identified but not started; no task file yet |
| `active` | Task file exists and work is in progress |
| `done` | Task completed; task file removed |
| `cancelled` | Work will not be done; reason in Notes |

`done` and `cancelled` are terminal — rows in these states move to the Archive table (see below).

## Adding a Backlog Item

1. Open `<root>/BACKLOG.md`.
2. Assign the next sequential ID from the live table. If working in a worktree or parallel
   branch (see **git-conventions**), also check `origin/main`'s copy (`git fetch` then
   `git show origin/main:BACKLOG.md`) before assigning — this reduces, but does not
   guarantee, ID collisions when multiple agents add items concurrently. If a collision is
   only discovered at merge time, renumber the newer item and fix its cross-references.
3. Append a new row with `Status: backlog`, `Task File: —`, `Depends On: —` (or the
   blocking ID(s), if known), and `Created` set to today's date.
4. Set Priority to `medium` unless there is a clear reason to differ.

## Promoting to Active

When a task file is created (either directly or via `planned → active` promotion per task-workflow):

1. Change the row's `Status` to `active`.
2. Set `Task File` to the relative path of the task file (e.g., `.planning/tasks/feat_user-auth.md`).

## Marking an Item Done

Run this update **as part of the merge-readiness checklist** in task-workflow, before removing the task file:

1. Change `Status` to `done`.
2. Set `Task File` to `—` (task file is removed at this point).
3. Optionally append a short completion note to `Notes` (e.g., "shipped in v1.4.0").
4. Move the row from the live table to the Archive table (see [Archiving Resolved Items](#archiving-resolved-items)).

## Cancelling an Item

1. Change `Status` to `cancelled`.
2. Record the reason in `Notes` (e.g., "superseded by #012").
3. Move the row from the live table to the Archive table (see [Archiving Resolved Items](#archiving-resolved-items)).

## Archiving Resolved Items

Keeps the live table scannable as a project matures, without violating "one file per
project root" — the Archive is a second table in the same `BACKLOG.md`, not a second file.

1. Cut the row out of the live table once its `Status` becomes `done` or `cancelled`.
2. Paste it, unchanged, as a new row at the bottom of the `## Archive` table.
3. Never edit a row's `ID`, `Created`, or history once archived — Notes may still gain a
   trailing completion/cancellation note per the sections above.
4. If another live row's `Depends On` still references an archived ID, leave the reference
   as-is — the ID remains valid and lookup-able in the Archive.

## Incomplete Plan Steps / Unresolved Blockers

When a task closes with leftover work (per task-workflow's merge-readiness checklist):

- Create a **new backlog row** for each incomplete Plan step or unresolved Blocker.
- Reference the originating task ID in `Notes` (e.g., "from task #005"), and set `Depends On` if the new item is genuinely blocked by another open backlog ID.
- Set an appropriate Priority.

## Agent Discipline

- **Never skip the backlog.** Every piece of identified work — even small chores — gets a row.
- **No status jump.** Do not change `backlog → done` directly; always pass through `active`.
- **IDs are permanent.** Do not renumber or delete rows; `done`/`cancelled` rows move to the Archive table, they are never removed.
- **One file per project root.** The Archive is a second table inside the same `BACKLOG.md`, not a second file.
- **Review for staleness.** When asked to review the backlog (or when it's grown large), flag long-lived `backlog` rows with old `Created` dates for the human to re-prioritize, cancel, or promote — no fixed age threshold is prescribed.
