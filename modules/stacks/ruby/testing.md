# Ruby Testing Discipline

- Add or update tests for every behavior change in parser, VM, stdlib, or tooling.
- Keep regression tests small, reproducible, and tied to reported issues.
- Run `make test` and focused suites for impacted components before merge.
- Treat nondeterministic or platform-specific failures as blockers to release readiness.
