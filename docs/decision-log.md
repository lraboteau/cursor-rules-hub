# Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-15 | Compose implemented in Python alongside `sync.py` | One runtime on CI and developer machines; consistent UTF-8 and YAML handling on Windows. |
| 2026-04-15 | `templates/` committed; `compose.py --check` in CI | Prevents silent drift between modules/manifests and what users sync. |
| 2026-04-15 | Manifest-driven `priority` with three layer types | Explicit merge order: `stack-base` < `stack-extension` < `cross-cutting`. |
| 2026-04-15 | Core identity injected by default (`core: true`) | Ensures shared tone/discipline; opt out per manifest with `core: false`. |
| 2026-04-15 | Level-1 `#` sections only as merge keys | Predictable parsing; nested `##` content stays attached to its parent section. |
