---
name: hub-compose
description: Generates and validates .cursorrules templates for this repository from modules/manifests/core via scripts/compose.py. Use when composing templates, checking drift, or diagnosing compose failures.
---

# Hub Compose

## When to use this skill

- The user asks to regenerate templates in `templates/`.
- Changes touch `modules/`, `manifests/`, or `core/identity.md`.
- You need to verify there is no drift between sources and templates.

## Default workflow

1. Determine the need:
   - Generate all: `python scripts/compose.py --all`
   - Check only: `python scripts/compose.py --check`
   - Target one manifest: `python scripts/compose.py --manifest manifests/<stack>.yml`
2. Run the appropriate command.
3. If there is an error:
   - Read the `compose: error: ...` message.
   - Fix source files (`modules/`, `manifests/`, `core/`) instead of `templates/`.
4. If sources changed, rerun `--all` and then `--check`.

## Important project rules

- `templates/*.cursorrules` are generated: do not edit them manually.
- Markdown modules must start with a level-1 heading (`# Title`).
- Manifests must stay on `version: 1` with a valid structure.

## Useful commands

```bash
# Regenerate all templates
python scripts/compose.py --all

# Check there is no drift
python scripts/compose.py --check

# Compose one manifest
python scripts/compose.py --manifest manifests/hono-workers.yml
```
