---
name: code-review
description: Review Python code changes on the current branch with Google Python Style, idiomatic design, typing, test adequacy, KISS, SOLID, and separation of concerns. Use constructive language and actionable suggestions.
tools: [git]
---

# Python Code Review Skill

## What this skill does
Performs a structured review of Python code modified on the current Git branch, focusing on:

- Correctness and edge cases
- Readability and maintainability
- Idiomatic Python usage
- Google Python Style Guide alignment
- Type hints and typing quality
- Test coverage for business logic and complex behavior
- KISS (keep it simple)
- SOLID principles (when compatible with idiomatic Python)
- Separation of concerns and decomposition of complex code

This skill uses constructive, collaborative phrasing (for example: _“Have you considered…?”_) and includes practical suggestions.

## When to use
Use this skill when:

- Reviewing a pull request or branch before merge
- Auditing recent Python changes for quality
- Improving test strategy for new functionality
- Checking maintainability and design quality

## Keywords
python, code review, git diff, pull request, google style guide, pyguide, typing, type hints, tests, business logic, complexity, maintainability, SOLID, separation of concerns, idiomatic python, refactor, suggestions

## Inputs expected
- Repository with Git history
- Current branch checked out
- Optional: target base branch (default: `main` or merge-base)

## Workflow

### 1) Collect changed Python files
Identify files changed on the current branch.

Typical commands:
- `git merge-base HEAD main`
- `git diff --name-only <merge-base>...HEAD -- '*.py'`

If no Python files changed, report that and stop.

### 2) Review each changed file
For each changed file, evaluate:

1. **Correctness**
   - Potential bugs, missed edge cases, failure modes
   - Error handling and input validation

2. **Style and idioms**
   - Google Python Style Guide alignment
   - Naming, docstrings, readability, clear control flow
   - Idiomatic constructs (avoid overengineering)

3. **Typing**
   - Public APIs and core business logic are typed
   - Type hints are precise enough to be useful
   - Avoid unnecessary `Any` where stronger typing is feasible

4. **Tests**
   - Business logic and complex behavior are tested
   - Critical paths, edge cases, and regressions covered
   - Do **not** require exhaustive tests for trivial wrappers

5. **Design quality**
   - KISS: flag unnecessary complexity
   - SOLID (pragmatic): cohesion, dependency direction, interface clarity
   - Separation of concerns: split overly complex functions/classes

### 3) Prioritize findings
Classify findings as:

- **High**: likely bug, missing critical test, unsafe behavior
- **Medium**: maintainability risk, weak typing, design concern
- **Low**: style/readability polish, optional improvement

### 4) Use constructive review language
Prefer:
- “Have you considered handling …?”
- “Would it simplify this if …?”
- “Could this be split into … for clearer separation of concerns?”

Avoid blunt fault language such as “This is wrong.”

### 5) Provide actionable suggestions
Every significant finding should include:
- Why it matters
- Concrete improvement
- Optional code sketch if helpful

## Output format
Return:

1. **Summary**
   - Scope reviewed (files)
   - Overall quality impression

2. **Findings by priority**
   - High / Medium / Low
   - File + location
   - Observation + suggestion (constructive tone)

3. **Testing assessment**
   - What is adequately tested
   - What critical behavior is not yet covered

4. **Refactor opportunities**
   - Simplifications (KISS)
   - Separation of concerns improvements
   - Idiomatic Python upgrades

## Quality checks before finishing
- Reviewed only changed branch files (or clearly stated scope deviation)
- Included typing and testing assessment
- Called out complexity with simplification options
- Used constructive, collaborative wording
- Gave actionable suggestions, not only critique

## Example prompts
- “Review my current branch Python changes with this skill.”
- “Focus on typing and test adequacy in modified files.”
- “Find unnecessary complexity and suggest simpler designs.”
- “Check whether business logic has sufficient tests.”