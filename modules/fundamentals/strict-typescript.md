# TypeScript Best Practices

- Prefer explicit domain types and interfaces over loose structural typing in core flows.
- Avoid `any`; use `unknown` with narrowing when type certainty is not available.
- Keep strict null handling explicit and guard nullable values before use.
- Model enums and controlled value sets with string unions or `as const` objects intentionally.
- Use discriminated unions for stateful or variant-heavy logic instead of fragile flag combinations.
- Keep function signatures precise: typed inputs, typed outputs, and no hidden side effects.
- Prefer small reusable utility types over deeply nested ad-hoc generic complexity.
- Validate external or untrusted data at boundaries before casting to internal types.
- Keep runtime schema expectations aligned with TypeScript types to avoid false safety.
- Avoid unsafe non-null assertions (`!`) unless invariants are explicit and documented by logic.
- Type async boundaries clearly and handle error states explicitly.
- Use typed environment/binding objects for platform resources rather than string-based access.
- Add or update tests when type-level refactors could alter runtime behavior.
