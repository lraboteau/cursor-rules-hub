# Hono Best Practices

- Keep route handlers thin: parse and validate input, call domain logic, and return typed responses.
- Use explicit route grouping/versioning (for example `/api/v1/...`) and consistent naming conventions.
- Validate all external input (params, query, headers, JSON body) before business logic.
- Return consistent error payloads and status codes; avoid leaking stack traces or internal details.
- Centralize error handling with middleware (`app.onError`) and map known error classes to stable responses.
- Use middleware intentionally: auth first, validation/context next, business handlers last.
- Prefer request-scoped context values over mutable globals; keep handlers stateless where possible.
