# Testing expectations

- Add or update automated tests when behavior changes; skip only with an explicit reason noted in the task.
- Prefer fast, deterministic tests; isolate flaky IO behind interfaces that can be stubbed.
- Keep fixtures small and local to the suite that uses them.
