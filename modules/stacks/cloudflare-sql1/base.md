# Cloudflare D1 SQL Baseline

- Access D1 through Worker bindings and prepared statements instead of string-concatenated SQL.
- Keep schema and query design index-aware to preserve low-latency reads and predictable throughput.
- Use D1-compatible SQLite features deliberately (JSON/FTS extensions where justified by use case).
- Batch large migrations and bulk updates/deletes to stay within Workers CPU and execution limits.
- Prefer binding names in automation and migration scripts to keep deployments portable across environments.
