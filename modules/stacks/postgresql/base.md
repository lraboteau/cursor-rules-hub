# PostgreSQL Conventions

- Use explicit `snake_case` names for tables, columns, constraints, indexes, and migration identifiers.
- Define integrity constraints intentionally (`PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `NOT NULL`) and specify `ON DELETE`/`ON UPDATE` behavior for relationships.
- Manage schema evolution through forward-only, versioned migrations; document high-risk or destructive steps with rollback/recovery guidance.
- Require parameterized queries/prepared statements for dynamic values in application code; never rely on string interpolation for SQL.
- Keep transaction boundaries explicit for multi-step writes and enforce idempotent-safe behavior where retries are expected.
- Avoid destructive operations (`DROP`, mass deletes, type rewrites) outside explicit, reviewed migrations.
- Create indexes based on observed query patterns (filters/joins/order), and validate impact with `EXPLAIN`/`EXPLAIN ANALYZE`.
- Keep schema types, defaults, enum/check values, and application-level contracts aligned across migrations and code.
