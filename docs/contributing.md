# Contributing

## Working in this repo with Cursor

- Maintainer rules live in **`.cursor/rules/*.mdc`** (with front matter). They are not run through `compose.py`.
- Agent entry point: [`AGENTS.md`](../AGENTS.md) at the repo root.
- How `.mdc` rules relate to generated `.cursorrules`: [cursor-ide-practices.md](cursor-ide-practices.md).

## Add or edit a module

1. Place or update a file under `modules/` using only `# ` for top-level section titles.
2. Keep sections focused; prefer linking to docs over huge pasted guides.
3. Run `python scripts/compose.py --all` and commit the updated `templates/`.

## Add a public template

1. Create `manifests/<name>.yml` with `version: 1`, `template.id`, `template.title`, and `priority` blocks.
2. Reference modules without the `.md` suffix (paths relative to `modules/`).
3. Run `python scripts/compose.py --all`.
4. Open a PR; CI must pass `compose.py --check`.

You can also use the `create-manifest-template` Cursor command in this repo to generate a new manifest from an explicit list of modules and optionally compose its `.cursorrules` output.

## Priority blocks

Use `stack-base` for runtime/framework baseline rules, `stack-extension` for optional slices (e.g. testing addons), and `cross-cutting` for security, performance, or doc standards that should override stack defaults when titles collide.

## Tests

```bash
pytest
```
