# Cursor workflow

- Prefer **project rules** (e.g. `.cursor/rules/*.mdc`) scoped with `globs` when the repo has many areas; use a **single `.cursorrules`** when you want one file to share or sync across machines.
- Keep rules **short and specific**; split large topics into multiple rule files instead of one huge document.
- Ground suggestions in **this repository’s** stack, configs, and existing patterns—avoid generic advice that conflicts with the codebase.

# Context and edits

- When changing behavior, update **tests and docs** the same way you would for non-agent workflows.
- Do not paste secrets into rules, prompts, or committed samples; use env vars and secret stores as documented for your stack.
