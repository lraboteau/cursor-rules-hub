# Performance awareness

- Measure before optimizing; note what was measured and the baseline in PR descriptions when performance is the goal.
- Avoid accidental O(n²) patterns on large collections and unbounded in-memory buffering on hot paths.
- Prefer lazy work and caching only when correctness and invalidation are clear.
