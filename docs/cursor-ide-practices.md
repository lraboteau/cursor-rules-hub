# Cursor IDE practices (reference)

This page summarizes **practical conventions** for working well with Cursor in general, and how they map to **this repository**.

## Project rules: `.cursor/rules/*.mdc`

- Rules use **YAML front matter** (`description`, optional `globs`, `alwaysApply`).
- Prefer **short, focused rules** (roughly one concern per file) and **concrete examples** when it helps.
- Use **`globs`** so rules apply when relevant files are in context; use **`alwaysApply: true`** only for small, universal project facts.

Product features (MCP servers, model settings, indexing) change often—prefer the [Cursor documentation](https://docs.cursor.com) for product-specific setup.

## Monolithic `.cursorrules` vs modular rules

- **`.cursor/rules/`**: good for **large or multi-stack repos** where different globs load different guidance.
- **Single `.cursorrules` file**: fine for **one artifact** to copy into consumer projects.

This hub generates **`.cursorrules`** under `templates/` for consumers. Maintenance here stays in `modules/` + `manifests/`; use `scripts/sync.py` to copy a template into another repo.

## Authoring in *this* repo

| Location | Front matter | Purpose |
|----------|--------------|---------|
| `modules/**/*.md` | No (compose v1) | Slices merged by `compose.py`; top-level sections use `# Title` only. |
| `.cursor/rules/*.mdc` | Yes | Maintainer-facing Cursor rules; **not** processed by compose. |
| `core/identity.md` | No | Shared baseline merged into every template unless `core: false`. |

Do not add YAML front matter to `modules/` files: it would break or complicate the compose parser.

## Writing effective guidance

- Be **actionable** (what to do / avoid) rather than vague principles alone.
- Prefer **one rule file per topic** over a single huge rule.
- When suggesting fixes, align with **existing** stack and tooling in the target repo.
