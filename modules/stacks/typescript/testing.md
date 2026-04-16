# TypeScript Testing Discipline

- Add or update tests for parser, checker, emitter, and language-service behaviors affected by each change.
- Keep regression tests reproducible and scoped to observable compiler outcomes.
- Run `npm test` and targeted suites for impacted compiler/language-service paths.
- Treat crashes, serious regressions, and security issues as release blockers.
