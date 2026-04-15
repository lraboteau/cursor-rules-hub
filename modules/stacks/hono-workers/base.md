# Hono on Cloudflare Workers

- Target the Workers runtime and bindings documented in the repo; avoid Node-only APIs unless a compatibility layer is already configured.
- Prefer explicit `Env` typing for bindings and keep route handlers small and composable.
- Use streaming and `Response` patterns that fit Workers limits; guard against unbounded buffers.
