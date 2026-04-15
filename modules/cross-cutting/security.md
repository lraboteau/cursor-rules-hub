# Security Best Practices

- Treat all external input as untrusted; validate and sanitize params, query, headers, and body before use.
- Enforce authentication and authorization explicitly for protected resources and state-changing actions.
- Apply least-privilege access for services, bindings, and data operations.
- Never hardcode secrets, tokens, or credentials; use secure secret/binding workflows.
- Never log secrets or sensitive personal data; sanitize logs and error payloads.
- Keep error responses generic for clients and avoid exposing internals, stack traces, or infrastructure details.
- Use parameterized queries/prepared statements for dynamic data access to prevent injection risks.
- Validate file uploads/content types and enforce safe size/type limits for untrusted payloads.
- Set and maintain secure HTTP behavior (CORS, security headers, cookie/session flags) intentionally.
- Protect critical endpoints with abuse controls (rate limiting, throttling, and anomaly monitoring where applicable).
- Prefer secure-by-default dependency and package practices; avoid unmaintained or high-risk libraries.
- Keep threat-sensitive logic covered by tests (authz boundaries, validation failures, and privilege escalation paths).
- Include security review checkpoints in release workflow for high-risk changes.
