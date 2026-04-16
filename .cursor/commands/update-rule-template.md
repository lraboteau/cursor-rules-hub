# update-rule-template

Update an existing rule template from a GitHub repository and refresh `modules/`, `manifests/`, and `templates/` without creating new template targets.

## Goal

Update one existing rule stack deterministically from repository signals, while preserving the source-of-truth model (`modules/` + `manifests/`) and compose-based generation.

## Inputs (required)

- Repository URL: `https://github.com/<owner>/<repo>`
- Existing template id (slug): e.g. `acme-nodejs`
- Existing template title (expected current title or new desired title)
- Primary command to enforce in updated rules: e.g. `npm test`

## Preconditions (strict)

- `manifests/<template-id>.yml` must already exist.
- The manifest must be schema v1 and contain `template.id == <template-id>`.
- `templates/<template-id>.cursorrules` should already exist; if missing, stop and ask for confirmation before proceeding.
- If no module currently referenced by the target manifest exists, stop and report a broken baseline instead of creating a new stack silently.

## Workflow

1. Validate inputs before writing files:
   - repo is a valid GitHub URL;
   - template id is a lowercase slug (`[a-z0-9-]+`);
   - command is non-empty.
2. Resolve update target:
   - load `manifests/<template-id>.yml`;
   - verify target manifest matches the provided template id;
   - enumerate modules currently referenced in the manifest priority blocks.
3. Analyze the target repository (read-only):
   - detect dominant stack using sentinel files (`package.json`, `pyproject.toml`, `Cargo.toml`, `Gemfile`, `wrangler.toml`, etc.);
   - detect signals for testing/security/performance/docs.
   - detect whether the target project is a REST API (routing layer + HTTP endpoints + request/response contracts).
4. Update source-of-truth modules under `modules/`:
   - update only modules referenced by the target manifest, unless explicit user approval is given to add/remove module refs;
   - stack baseline in `modules/stacks/<stack>/base.md`;
   - optional stack testing in `modules/stacks/<stack>/testing.md`;
   - optional cross-cutting files in `modules/cross-cutting/` (`docs.md`, `security.md`, `performance.md`).
   - when the target is a REST API, include and maintain `modules/fundamentals/rest-api.md` in the manifest module refs.
5. Ensure every updated module remains compose-compatible:
   - first non-empty line must be a level-1 heading `# ...`;
   - content is actionable, concise, and deterministic.
6. Update the existing manifest (in place only):
   - keep `version: 1`;
   - keep `template.id` unchanged;
   - update `template.title` only if explicitly requested;
   - keep priority block order: `stack-base`, `stack-extension`, `cross-cutting`;
   - add `fundamentals/rest-api` to the target manifest when REST API detection is positive, and remove it when it no longer applies;
   - never create a second manifest file for the same template id.
7. Regenerate template output through compose only:
   - run `python3 scripts/compose.py --manifest manifests/<template-id>.yml`;
   - never hand-edit files in `templates/`.
8. Run validation checks:
   - `python3 scripts/compose.py --check`
   - `python3 -m pytest -q`
9. Report exactly what changed:
   - modules modified;
   - manifest fields and module refs changed;
   - regenerated template path;
   - assumptions made during stack/signal detection.

## Guardrails

- Source of truth is `modules/` + `manifests/`; treat `templates/` as generated output only.
- Update only the targeted template id; do not edit unrelated manifests/modules/templates.
- Never create a new template or manifest implicitly in this command.
- Require explicit overwrite confirmation before replacing existing module content.
- Do not use destructive git commands.
- If stack detection is ambiguous, stop and ask for clarification rather than guessing.
