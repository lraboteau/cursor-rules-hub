# Testing SQL and D1 Features

- Add migration tests that verify schema shape, constraints, and index presence after applying forward migrations.
- Cover failure paths for invalid writes (constraint violations, FK behavior, and type/check mismatches), not only success cases.
- Use deterministic seed fixtures and isolate test data per case to avoid cross-test coupling.
- Validate query behavior on realistic list/filter/sort access patterns to catch missing indexes and regressions early.
- Test retry behavior for transient D1 failures with bounded attempts, backoff, and idempotent-safe operations.
