# Cloudflare Workers Baseline

- Keep `compatibility_date` current and enable `nodejs_compat` when Node.js APIs are required.
- Use Cloudflare bindings directly (KV, R2, D1, Queues, Durable Objects) instead of external REST hops when possible.
- Avoid global mutable state because Worker isolates are reused across requests.
- Prefer streaming request/response bodies to reduce memory pressure and improve latency.
- Always `await` promises or use `ctx.waitUntil(...)` for background work.
