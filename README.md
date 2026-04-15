# cursor-rules-hub

Opinionated, **manifest-driven** Cursor rule templates built from reusable Markdown modules. Generate deterministic `.cursorrules` files, check them in CI, and sync them into any repository.

## Quickstart

```bash
python -m pip install -r requirements.txt
python scripts/compose.py --all
python scripts/sync.py --list
python scripts/sync.py --yes . hono-workers
```

- Architecture: [docs/architecture.md](docs/architecture.md)
- Day-to-day usage: [docs/usage.md](docs/usage.md)
- Contributing: [docs/contributing.md](docs/contributing.md)
- Cursor IDE practices: [docs/cursor-ide-practices.md](docs/cursor-ide-practices.md)

## Layout

- `core/identity.md` — shared baseline prepended with lowest merge priority
- `modules/` — `fundamentals/`, `stacks/`, `cross-cutting/`
- `manifests/` — one YAML file per public template
- `templates/` — **generated**; edit sources instead
- `scripts/compose.py`, `scripts/sync.py` — compose and cross-platform sync

## Principles

- No legacy wrapper scripts; `modules/` + `manifests/` are the source of truth.
- CI blocks drift between generated templates and sources.

## License

MIT — see [LICENSE](LICENSE).
