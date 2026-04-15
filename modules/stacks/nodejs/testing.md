# Testing Node.js features

- Prefer the test runner already used by the project (`vitest`, `jest`, or Node test runner) and keep configuration centralized.
- Mock external I/O (HTTP, queues, databases) by default; keep integration tests explicit, isolated, and reproducible.
- Add CLI and script-level tests when repository workflows depend on package scripts or build tooling behavior.
