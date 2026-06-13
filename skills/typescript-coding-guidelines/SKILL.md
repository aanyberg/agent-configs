---
name: typescript-coding-guidelines
description: Rules for TypeScript and JavaScript code — idioms, type system usage, error handling, naming, imports, and eliminating unnecessary complexity. Use when reading or writing .ts, .tsx, .js, or .jsx files.
---

# TypeScript & JavaScript Coding Guidelines

Applies to all `.ts`, `.tsx`, `.js`, and `.jsx` files. TypeScript-only rules are marked **[TS]**.

## Code Style

- Keep commits focused on their stated purpose — exclude unrelated changes even if conceptually related — Simplifies review, prevents unintended side effects, and makes rollbacks cleaner when each PR has a single clear objective
- Wrap code identifiers in backticks in user-facing messages (errors, warnings, logs) — Improves readability and clearly distinguishes code elements from prose
- Centralize validation at one layer — removes redundancy and establishes a single source of truth — Prevents validation drift when requirements change
- Extract duplicated logic into shared helpers after 2+ occurrences — refactor existing code rather than creating parallel implementations — Prevents bugs from inconsistent implementations
- Remove commented-out code, unused definitions, and superseded implementations — Version control preserves history; dead code creates confusion about intent and active control flow
- Consolidate duplicate logic across conditional branches using combined conditions, extracted variables, or hoisted shared code — Reduces duplication and clarifies intentionally shared behavior
- Inline single-use helpers that only wrap property access or delegation — reduces nesting and cognitive load without sacrificing clarity
- Scope helpers and constants to their single usage site — define inline or within the module/function that uses them — Reduces namespace pollution and prevents accidental reuse of implementation details
- Compile static `RegExp` patterns as module-level `const` — avoids recompilation overhead on repeated calls
- Extract repeated logic into helper functions when patterns recur across handlers, serializers, or adapters — Prevents duplication bugs and makes changes easier to apply consistently

## Type System [TS]

- Use `instanceof` for class-based type narrowing; use discriminated unions with a `kind` or `type` literal field for sum-type narrowing — Enables proper type narrowing for static analysis and prevents fragile duck-typing
- Use `unknown` instead of `any` — forces explicit narrowing before use, catching errors at compile time rather than runtime
- Avoid `as` type assertions except when runtime logic guarantees safety and static analysis cannot narrow (e.g., after a literal check or known invariant) — use type guards or discriminated unions instead; document the safety reasoning when `as` is genuinely necessary
- Use `satisfies` to validate an expression against a type without widening the inferred type — preserves literal types while catching structural mismatches at the point of definition
- Use `as const` assertions for readonly literal tuples and objects — prevents widening to mutable primitive types
- Use `Literal` union types for fixed string/number value sets in parameters, fields, and return types — Makes valid values explicit in signatures and enables static catch of invalid values
- Create type aliases for complex types (3+ union branches, object types used 2+ times) — reduces duplication and improves readability; skip aliases for simple one-off internal types
- Use `interface` for extensible object shapes (declaration merging, class `implements`); use `type` for unions, intersections, mapped types, and aliases — matches the intended extension model of each construct
- Use `readonly` on arrays (`readonly T[]`) and object properties that must not be mutated — makes immutability intent explicit and catches accidental writes at compile time
- Use `never` to enforce exhaustive checks in `switch`/`if`-else chains over discriminated unions — a compile-time guarantee that all cases are handled
- Remove `| undefined` from fields when values are guaranteed to be initialized — prevents false optionality and unnecessary non-null checks
- Avoid `@ts-ignore`; use `@ts-expect-error` only when unavoidable, always with a comment explaining why the suppression is safe and what error it hides
- Fix type errors properly — use type annotations, narrowing, or `as` with explanatory comments — prevents masking real type errors that indicate structural problems
- **`strict: true` is non-negotiable** — it enables `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, and related checks; never disable it project-wide

## Error Handling

- Use domain-specific error classes extending `Error` — set `this.name` in the constructor for clear stack traces and `instanceof` checks
- Never use `console.assert` as error handling — throw descriptive errors with the relevant identifiers included
- Use the `cause` option when re-throwing: `throw new AppError("message", { cause: err })` — preserves the original stack trace and error chain
- Fail fast: validate input parameters before expensive operations — prevents unnecessary resource consumption and provides faster feedback
- Catch specific error types instead of bare `catch (e: unknown)` when failure modes are known — prevents catching unexpected errors that should propagate
- Avoid swallowing errors in `.catch(() => {})` — at minimum log them with enough context to diagnose the issue later
- Use `!r`-equivalent quoting in error messages — wrap identifiers with backticks or quotes so values are clearly delimited: `` `Unknown tool \`${name}\`` `` — handles edge cases like empty strings or special characters

## Naming

- Use `camelCase` for variables, functions, and methods; `PascalCase` for classes, interfaces, types, and enums; `UPPER_CASE` for module-level constants (`const MAX_RETRIES = 3`)
- Prefix internal module constants with `_` when they are not part of the public export surface (`const _CACHE_TTL_MS = 60_000`)
- Drop redundant prefixes when context is clear — prefer `Config.description` over `Config.configDescription`, `Tool.label` over `Tool.toolLabel` — the containing class/module already provides context
- Use specific parameter/variable names that convey semantic meaning — prefer `userId`, `orderId`, `configData` over generic `id`, `name`, `data` — prevents confusion when multiple identifiers of the same shape are in scope
- Avoid redundant type suffixes (`Value`, `Type`, `Class`, `List`, `String`) when the type is clear from annotations or context
- Boolean variables and functions should read as predicates: `isLoading`, `hasError`, `canSubmit`, `isEmpty`
- Rename functions/methods when their behavior changes — names must reflect actual scope, return values, and abstraction level

## Imports

- Place all imports at the top of the file — no dynamic `require()` or `import()` inside functions unless lazy-loading is intentional and documented with a comment explaining why
- Prefer named exports over default exports — named exports improve refactoring support, IDE discoverability, and make re-exporting explicit
- Use barrel files (`index.ts`) to define the public API of a module — export only what consumers need; do not re-export internal implementation details
- Avoid circular imports — if two modules depend on each other, extract shared logic into a third module
- Remove unused imports — prevents dependency bloat and keeps the module namespace clean
- Group imports consistently: external packages first, then internal modules (`@/`, `~/`, relative), separated by a blank line; enforce with ESLint's `import/order` rule or Biome

## Testing

- Remove tests when redundant, obsolete, or duplicative — each test should verify distinct, valuable behavior that currently exists
- Test behavior, not implementation — avoid asserting on internal state or private members directly; test through the public interface
- Use descriptive test names that read as full sentences: `it("returns null when the user is not found")`, `it("throws when the token is expired")`
- Prefer `vi.fn()` / `jest.fn()` stubs over full module mocks when testing units in isolation — avoids over-specification and keeps tests resilient to refactoring
- Avoid `// istanbul ignore` / `/* c8 ignore */` — write tests instead; only suppress coverage for code paths that genuinely cannot execute in test environments (platform-specific branches, unreachable defensive guards)

## General

- Use `pnpm` by default unless `package.json` scripts or project docs specify `npm` or `yarn`
- Run `eslint` and `prettier` (or `biome`) before committing — enforce via pre-commit hooks or CI; never disable rules project-wide without a documented reason
- Prefer `const` over `let`; never use `var` — `const` communicates immutability of the binding and prevents accidental reassignment
- Use optional chaining (`?.`) and nullish coalescing (`??`) instead of manual null guards — more concise and avoids incorrectly coalescing on `0`, `""`, or `false`
- Use `structuredClone()` for deep cloning plain objects instead of `JSON.parse(JSON.stringify(...))` — handles more types correctly and is faster in modern runtimes
