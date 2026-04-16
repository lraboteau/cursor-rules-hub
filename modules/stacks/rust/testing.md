# Rust Testing Discipline

- Add or update tests for compiler behavior, borrow checking, diagnostics, and standard library regressions.
- Keep regression tests minimal, reproducible, and tied to concrete failing cases.
- Run `python x.py test` and focused suites for impacted areas before merge.
- Treat soundness bugs, miscompilations, and security regressions as release blockers.
