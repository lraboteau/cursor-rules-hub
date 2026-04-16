# CPython Testing Discipline

- Add or update tests for parser, runtime, stdlib, and platform-specific behavior touched by each change.
- Keep regressions reproducible and tied to concrete failing scenarios.
- Run `make test` and targeted test subsets for impacted areas before merge.
- Treat crashes, security regressions, and behavioral incompatibilities as release blockers.
