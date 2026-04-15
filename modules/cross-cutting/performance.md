# Performance Best Practices

- Optimize critical rendering paths to protect Core Web Vitals (LCP, CLS, INP/TBT proxies).
- Ship less JavaScript: avoid unnecessary client bundles, heavy dependencies, and duplicate runtime logic.
- Prefer streaming, caching, and server-side computation when it reduces client work and latency.
- Keep images/fonts optimized (correct formats, dimensions, lazy loading, and preload only when justified).
- Reduce layout shift by reserving space for dynamic media and async UI blocks.
- Avoid render-blocking assets where possible; load non-critical resources with appropriate priority.
- Keep API handlers efficient: avoid N+1 patterns, over-fetching, and unbounded payloads.
- Use pagination, filtering, and field selection for list endpoints to cap response cost.
- Apply caching intentionally (HTTP cache headers, edge/cache layers, and revalidation strategy).
- Prefer idempotent and retry-safe operations for transient failures; avoid expensive repeated side effects.
- Measure and log performance metrics with request correlation identifiers for troubleshooting.
- Profile before and after meaningful changes; verify improvements with objective metrics.
- Add/update tests or checks for performance-sensitive paths when behavior could regress.
