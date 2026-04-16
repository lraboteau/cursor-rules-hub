# create-rule-template

Create a new rule template from a GitHub repository and populate `modules/`, `manifests/`, and `templates/`.

## Goal

Bootstrap a usable rule stack from scratch using one command input, with deterministic outputs compatible with `scripts/compose.py`.

## Inputs (required)

- Repository URL: `https://github.com/<owner>/<repo>`
- Template id (slug): e.g. `acme-nodejs`
- Template title: e.g. `Acme Node.js`
- Primary command to enforce in rules: e.g. `npm test`

## Workflow

1. Validate inputs before writing files:
   - repo is a valid GitHub URL;
   - template id is a lowercase slug (`[a-z0-9-]+`);
   - command is non-empty.
2. Analyze the target repository (read-only):
   - detect dominant stack using sentinel files (`package.json`, `pyproject.toml`, `Cargo.toml`, `Gemfile`, `wrangler.toml`, etc.);
   - detect signals for testing/security/performance/docs.
3. Create or update source-of-truth modules under `modules/`:
   - stack baseline in `modules/stacks/<stack>/base.md`;
   - optional stack testing in `modules/stacks/<stack>/testing.md`;
   - optional cross-cutting files in `modules/cross-cutting/` (`docs.md`, `security.md`, `performance.md`).
4. Ensure every generated module is compose-compatible:
   - first non-empty line must be a level-1 heading `# ...`;
   - content is actionable, concise, and deterministic.
5. Create `manifests/<template-id>.yml` (schema v1):
   - `version: 1`;
   - `template.id` and `template.title`;
   - `priority` blocks in this order:
     - `stack-base`
     - `stack-extension`
     - `cross-cutting`
   - module refs must be relative to `modules/` and omit `.md`.
6. Generate template output only through compose:
   - run `python3 scripts/compose.py --manifest manifests/<template-id>.yml`
   - never hand-edit files in `templates/`.
7. Run validation checks:
   - `python3 scripts/compose.py --check`
   - `python3 -m pytest -q`
8. Report exactly what was created:
   - module files;
   - manifest path;
   - generated template path;
   - any assumptions made during stack detection.

## Guardrails

- Source of truth is `modules/` + `manifests/`; treat `templates/` as generated output only.
- Do not edit unrelated manifests/modules/templates.
- If files already exist, require explicit overwrite confirmation.
- Do not use destructive git commands.
- If stack detection is ambiguous, stop and ask for clarification rather than guessing.
