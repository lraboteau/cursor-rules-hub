---
name: hub-sync
description: Syncs a generated template from this repository to a consumer .cursorrules file via scripts/sync.py. Use when listing templates, selecting one, and copying it with safety options and optional compose-first execution.
---

# Hub Sync

## When to use this skill

- The user wants to copy a template into another project.
- You need to list available templates.
- You need to run sync with backup or compose-first options.

## Default workflow

1. List templates:
   - `python scripts/sync.py --list`
2. Determine the destination:
   - Consumer project directory (writes `<target>/.cursorrules`)
   - Or an explicit file path
3. Run sync:
   - Standard: `python scripts/sync.py <target> <template>`
   - No prompt: add `-y`
   - With backup: add `--backup`
   - With compose-first: add `--compose-first`
4. Verify that target `.cursorrules` was updated.

## Error handling

- `sync: error: ...` indicates a validation error (bad args/missing template).
- `sync: file error: ...` indicates an I/O error (permissions/invalid path).
- If `--compose-first` fails, fix compose issues first.

## Useful commands

```bash
# List available templates
python scripts/sync.py --list

# Copy the ruby template to a target repo
python scripts/sync.py ../my-ruby-app ruby

# Sync with forced overwrite and backup
python scripts/sync.py ../my-ruby-app ruby -y --backup

# Recompose before sync
python scripts/sync.py ../my-ruby-app ruby --compose-first -y
```
