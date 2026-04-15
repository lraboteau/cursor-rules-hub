# Testing Hono Features

- Add route-level tests for success paths, validation failures, auth failures, and error mapping behavior.
- Keep tests hermetic by mocking external I/O and integration boundaries when unit behavior is the target.
- Verify middleware ordering and request context behavior in tests when auth/validation chains change.
