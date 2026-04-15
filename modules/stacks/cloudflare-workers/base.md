# Cloudflare Workers Foundations

- Primary stack: Cloudflare Workers + TypeScript; keep runtime-specific behavior aligned with Workers constraints.
- Treat `wrangler.jsonc` as source of truth; if dashboard changes are made, sync them back to config.
- Maintain backward compatibility for existing bindings and runtime configuration unless migration is intentional.
- Access platform resources through typed `env` bindings; never hardcode secrets, tokens, or credentials.
- Keep environments intentionally separated (`dev`, `staging`, `prod`) with distinct bindings and resource IDs.
- Prefer structured JSON logs for operational events and include request correlation identifiers when practical.
- For observability-sensitive changes, ensure Workers logging and tracing settings remain deliberate.
