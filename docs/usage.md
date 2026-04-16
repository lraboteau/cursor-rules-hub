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
python scripts/compose.py --manifest manifests/hono.yml
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

Current public template IDs include:
`cloudflare-sql1`, `cloudflare-workers`, `esbuild`, `github-actions`, `hono`,
`json-ld`, `nodejs`, `postgresql`, `python`, `ruby`, `ruby-middleman`,
`ruby-rails`, `rust`, `semantic-web`, `seo`, `tailwind`, `typescript`, and `vite`.

Copy a template to `./.cursorrules` (prompts unless `--yes`):

```bash
python scripts/sync.py . templates/hono.cursorrules
# or short name matching a file in templates/
python scripts/sync.py . hono
```

Non-interactive overwrite with backup:

```bash
python scripts/sync.py --yes --backup . hono
```

Regenerate templates before syncing:

```bash
python scripts/sync.py --compose-first --yes . hono
```

## Install without clone (GitHub)

Directly download a generated template into a target project:

```bash
curl -fsSL \
  https://raw.githubusercontent.com/laurent/cursor-rules-hub/main/templates/hono.cursorrules \
  -o /path/to/new-project/.cursorrules
```

Use the bootstrap installer script:

```bash
curl -fsSL \
  https://raw.githubusercontent.com/laurent/cursor-rules-hub/main/scripts/install-cursorrules.sh \
  | bash -s -- --template hono --target /path/to/new-project --yes
```

Keep a backup when overwriting:

```bash
curl -fsSL \
  https://raw.githubusercontent.com/laurent/cursor-rules-hub/main/scripts/install-cursorrules.sh \
  | bash -s -- --template hono --target /path/to/new-project --backup --yes
```

For stable/reproducible installs, pin `main` to a tag or commit SHA in URLs.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Validation / CLI usage error |
| 2 | File operation error |

## CI

- `compose-check.yml` runs `compose.py --check`.
- `sync-smoke.yml` exercises `sync.py` in a temporary directory.
