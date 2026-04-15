# SQL and D1 Conventions

- Use explicit `snake_case` names for tables, columns, constraints, and indexes.
- Define integrity constraints intentionally: `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, and `NOT NULL` where appropriate.
- Prefer `CREATE TABLE IF NOT EXISTS` for bootstrap scripts and idempotent setup.
- Require explicit `ON DELETE` / `ON UPDATE` behavior for foreign keys when relationship behavior matters.
- For dynamic user input, require parameterized queries/prepared statements in application code; never rely on SQL string interpolation.
- Manage schema changes through forward-only, versioned migrations; document high-risk or destructive steps.
- Avoid destructive operations (`DROP`, large deletes, type rewrites) without an explicit migration and rollback/recovery plan.
- Create indexes for frequent filters/joins and key FK columns used by application queries.
- Before high-risk data/schema operations, take a D1 backup checkpoint.
- Keep SQL types, enum/check values, and application-level expectations aligned across schema and code.
- Define application-side retry policy for transient D1 failures: bounded retries, backoff with jitter, idempotent-safe operations only.
- If schema conventions or migration workflow guidance changes, sync related docs via `/update-docs`.
