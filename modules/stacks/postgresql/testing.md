# Testing PostgreSQL Features

- Add migration tests that verify final schema shape, constraints, and index presence after applying forward migrations.
- Cover error paths, not only success paths: constraint violations, FK behavior, conflict handling, and transaction rollback behavior.
- Use deterministic fixtures/seed data and isolate test datasets per case to avoid coupling and flaky outcomes.
- Validate performance-sensitive queries with realistic filter/join patterns to catch missing indexes before release.
- Test retry behavior for transient failures with bounded attempts, backoff, and idempotent-safe operations only.
