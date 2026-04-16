# Cloudflare D1 SQL Testing Discipline

- Add tests for prepared statement correctness, parameter binding, and expected query results.
- Verify index usage and query plans for performance-critical paths before release.
- Test migrations in incremental batches and validate rollback/recovery strategy for failed steps.
- Validate Workers integration limits (CPU, memory, concurrent D1 connections) under realistic load.
