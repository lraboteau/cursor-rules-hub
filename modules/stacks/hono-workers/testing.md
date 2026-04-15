# Testing Workers features

- Prefer `vitest` with `@cloudflare/vitest-pool-workers` when the project already uses that stack.
- Keep tests hermetic: mock fetches and bindings where needed; avoid live network in unit tests by default.
