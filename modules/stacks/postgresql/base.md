# PostgreSQL Baseline

- Design schemas with explicit constraints, sensible defaults, and clear ownership of migrations.
- Prefer parameterized queries and prepared statements to avoid SQL injection and improve plan stability.
- Create and maintain indexes based on query patterns, not assumptions.
- Keep transactions explicit and scoped to preserve consistency under concurrent load.
- Run representative integration tests against PostgreSQL before merge.
