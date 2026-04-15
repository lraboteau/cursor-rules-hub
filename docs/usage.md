# Usage

## Prerequisites

- Python 3.9+ (CI uses 3.12)
- Install dependencies: `python -m pip install -r requirements.txt` (from repo root)

## Compose locally

Regenerate all public templates from `manifests/`:

```bash
python scripts/compose.py --all
```

Compose a single manifest:

```bash
python scripts/compose.py --manifest manifests/hono-workers.yml
```

Verify that `templates/` matches sources (CI uses this):

```bash
python scripts/compose.py --check
```

## Sync into a project

List available templates:

```bash
python scripts/sync.py --list
```

Copy a template to `./.cursorrules` (prompts unless `--yes`):

```bash
python scripts/sync.py . templates/hono-workers.cursorrules
# or short name matching a file in templates/
python scripts/sync.py . hono-workers
```

Non-interactive overwrite with backup:

```bash
python scripts/sync.py --yes --backup . hono-workers
```

Regenerate templates before syncing:

```bash
python scripts/sync.py --compose-first --yes . hono-workers
```

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Validation / CLI usage error |
| 2 | File operation error |

## CI

- `compose-check.yml` runs `compose.py --check`.
- `sync-smoke.yml` exercises `sync.py` in a temporary directory.
