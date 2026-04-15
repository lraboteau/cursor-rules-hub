# cursor-rules-hub

Opinionated, **manifest-driven** Cursor rule templates built from reusable Markdown modules. Generate deterministic `.cursorrules` files, check them in CI, and sync them into any repository.

## Quickstart

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Generate templates from manifests
python scripts/compose.py --all

# List available templates
python scripts/sync.py --list

# Apply a template to a new project
python scripts/sync.py --yes /path/to/new-project hono-cloudflare-workers

# Optional: regenerate templates before syncing
python scripts/sync.py --compose-first --yes /path/to/new-project hono-cloudflare-workers
```

## Public Templates

Current public stacks include:

- `cloudflare-workers`
- `hono`
- `hono-cloudflare-workers`
- `nodejs`
- `postgresql`
- `python`
- `ruby`
- `ruby-middleman`
- `rust`
- `cloudflare-sql1`
- `tailwind`

## Install Without Clone (GitHub)

```bash
# Direct raw template URL
curl -fsSL \
  https://raw.githubusercontent.com/laurent/cursor-rules-hub/main/templates/hono-cloudflare-workers.cursorrules \
  -o /path/to/new-project/.cursorrules

# Bootstrap installer script (template + target)
curl -fsSL \
  https://raw.githubusercontent.com/laurent/cursor-rules-hub/main/scripts/install-cursorrules.sh \
  | bash -s -- --template hono-cloudflare-workers --target /path/to/new-project --yes
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
