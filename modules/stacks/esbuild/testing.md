# Esbuild Testing Discipline

- Add or update tests for bundling correctness, module format handling (ESM/CommonJS), and source map behavior.
- Keep regression tests deterministic across platforms and runtime targets.
- Run `npm test` and benchmark-sensitive checks before merge.
- Treat performance regressions and output compatibility breaks as release blockers.
