# REST API Best Practices

- Design resource-oriented endpoints with consistent naming and plural nouns.
- Keep HTTP method semantics explicit (`GET` read-only, `POST` create, `PUT/PATCH` update, `DELETE` remove).
- Use stable, predictable response contracts for success and error payloads across endpoints.
- Map status codes intentionally (`200/201/204`, `400/401/403/404/409/422`, `429`, `5xx`) based on API behavior.
- Version APIs deliberately (for example `/api/v1`) and avoid breaking changes without migration strategy.
- Validate and sanitize all external input (path params, query, headers, body) before domain logic.
- Require authentication/authorization checks before protected operations.
- Never expose secrets, stack traces, tokens, or sensitive internals in responses or logs.
- Use pagination, filtering, and sorting conventions consistently for list endpoints.
- Prefer idempotent behavior where relevant (especially retries and update/delete flows).
- Apply rate limiting and abuse protection on exposed endpoints when risk is non-trivial.
- Emit structured logs and correlation identifiers to trace request lifecycle and failures.
- Define and test error handling paths, not only success paths.