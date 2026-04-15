# Testing Workers Features

- Prefer `vitest` with `@cloudflare/vitest-pool-workers` when the project already uses that stack.
- Keep tests hermetic: mock fetches and bindings where needed; avoid live network in unit tests by default.
- Add focused integration tests for Worker bindings (`env`) and D1 interactions when behavior depends on runtime resources.
