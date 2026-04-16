# GitHub Actions Baseline

- Keep workflows deterministic, minimal, and scoped to clear CI/CD responsibilities.
- Pin core actions to trusted major versions and review third-party actions before adoption.
- Use matrix builds only when they provide meaningful coverage relative to runtime cost.
- Cache dependencies explicitly and invalidate caches predictably when lockfiles change.
- Keep secrets and environment protections aligned with least-privilege deployment needs.
