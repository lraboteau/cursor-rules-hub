# Esbuild Baseline

- Prioritize build performance and keep bundling steps simple and observable.
- Use built-in esbuild capabilities (JS, TS, JSX, CSS, minification, sourcemaps) before adding extra tooling layers.
- Keep configuration explicit and avoid hidden magic across CLI, JS API, and Go API usage.
- Run `npm test` before proposing behavior changes.
