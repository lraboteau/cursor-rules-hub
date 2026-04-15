# Agent instructions (cursor-rules-hub)

This repository builds **Cursor rule templates** from `modules/` and `manifests/`. Treat those paths as the **single source of truth**; `templates/*.cursorrules` are **generated** outputs.

## Before you finish a change

1. If you touched `modules/`, `manifests/`, or `core/`: run `python scripts/compose.py --all`.
2. Always run `python scripts/compose.py --check` and `python -m pytest -q` before a PR or hand-off.

## Where to read

- [docs/architecture.md](docs/architecture.md) — data flow, manifest schema, merge policy.
- [docs/contributing.md](docs/contributing.md) — how to add modules and manifests.
- [docs/cursor-ide-practices.md](docs/cursor-ide-practices.md) — Cursor rules (`.mdc`) vs generated `.cursorrules` for consumers.

## Scope

Keep edits minimal and aligned with existing patterns. Do not hand-edit files under `templates/`.
