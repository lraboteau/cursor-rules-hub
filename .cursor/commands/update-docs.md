# update-docs

Synchronize project documentation after implementation changes.

## Objective

Keep planning, rules, skills, changelog entries, and user-facing documentation consistent with the latest implementation work.

## Constraints

- Write all new or updated text in English.
- Ensure every documentation file under `.cursor/` is in English (no mixed-language sections).
- Prefer small, targeted edits.
- Do not modify unrelated files.
- Keep terminology consistent across plans, rules, skills, `CHANGELOG.md`, `AGENTS.md`, and `README.md`.

## Inputs

- Current task context and implementation outcome.
- Existing docs in `.cursor/plans/`, `.cursor/rules/`, `.cursor/skills/`, `.cursor/commands/`, `CHANGELOG.md`, `AGENTS.md`, and `README.md`.

## Workflow

### 1) Understand what changed

- Identify changed behavior, not only changed files.
- Build a concise change summary:
  - what was implemented;
  - why it was implemented;
  - what operational expectations changed.
- List impacted documentation targets before editing.

### 2) Decide whether a plan update is needed

- Update or add a plan only when the task meaningfully changes scope, sequence, or ownership.
- If a plan is needed, store it in `.cursor/plans/` with a stable name format:
  - `YYYY-MM-DD-<short-topic>.plan.md`
- Keep plan updates scoped to the current change.

### 3) Update documentation targets that are actually impacted

- `.cursor/rules/`: update only where behavior or standards changed; keep frontmatter valid.
- `.cursor/skills/`: update only where triggers/workflows changed; preserve valid `name`/`description`.
- `.cursor/commands/`: update operational steps and guardrails when workflows changed.
- `CHANGELOG.md`: add or update entries when implementation changes impact behavior, workflows, templates, or operational expectations.
- `AGENTS.md`: update only if agent operating expectations changed.
- `README.md`: update only if user/developer-facing workflow changed.

### 4) Keep quality and terminology consistent

- Keep edits small and focused.
- Keep terminology consistent across plans, rules, skills, commands, `CHANGELOG.md`, `AGENTS.md`, and `README.md`.
- Ensure instructions are actionable and non-duplicative.

### 5) Verify consistency

- Check for contradictions across updated files.
- Normalize key terms so the same concept uses the same wording everywhere.
- Confirm all cross-references point to existing files.
- Confirm `CHANGELOG.md` entries are grouped under `Unreleased` and reflect implemented behavior changes.
- Confirm `.cursor/` documentation content is fully English:
  - plans, rules, skills, and commands;
  - titles, bullet text, checklists, and examples;
  - no mixed-language leftovers after updates.

## Final Checklist

- Updated only impacted documentation targets.
- Rules, skills, and commands are aligned where needed.
- `CHANGELOG.md`, `AGENTS.md`, and `README.md` are updated only when required by behavioral changes.
- All `.cursor/` documentation files are fully in English.
- No outdated or conflicting guidance remains.
- Documentation changes stay scoped to impacted areas only.