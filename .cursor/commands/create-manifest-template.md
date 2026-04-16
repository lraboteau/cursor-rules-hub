# create-manifest-template

Create a new manifest-driven template from an explicit list of modules, and optionally compose its `.cursorrules` output.

## Goal

Make it easy to define a new stack template by passing module references as parameters, without hand-writing a manifest file.

## Inputs

When the user runs the `create-manifest-template` command in this repo, collect the following information (from the initial request or via follow-up questions):

- **Template id** (required): lower-case slug used as `template.id` and file name, e.g. `hono-cloudflare-full-stack`.
- **Template title** (required): human-readable title, e.g. `Hono + Cloudflare Full Stack`.
- **Base modules** (required): ordered list of module refs for the `stack-base` block, e.g.:
  - `stacks/nodejs/base`
  - `stacks/typescript/base`
  - `stacks/hono/base`
  - `stacks/vite/base`
  - `stacks/tailwind/base`
  - `stacks/cloudflare-workers/base`
  - `stacks/cloudflare-sql1/base`
  - `stacks/json-ld/base`
  - `stacks/semantic-web/base`
  - `fundamentals/rest-api`
  - `fundamentals/seo`
- **Extension modules** (optional): ordered list of module refs for the `stack-extension` block, e.g.:
  - `stacks/nodejs/testing`
  - `stacks/typescript/testing`
  - `stacks/hono/testing`
  - `stacks/vite/testing`
  - `stacks/tailwind/testing`
  - `stacks/cloudflare-workers/testing`
  - `stacks/cloudflare-sql1/testing`
  - `stacks/json-ld/testing`
  - `stacks/semantic-web/testing`
- **Cross-cutting modules** (optional): ordered list of module refs for the `cross-cutting` block, e.g.:
  - `cross-cutting/docs`
  - `cross-cutting/security`
  - `cross-cutting/performance`
- **Compose flag** (optional): whether to immediately generate the `.cursorrules` template from the manifest.

All module references must be relative to `modules/` and omit the `.md` suffix (for example `stacks/hono/base`, not `modules/stacks/hono/base.md`).

## Validation

Before writing any files:

1. **Validate the template id**
   - Must be a non-empty slug of the form `[a-z0-9-]+`.
   - Reject or ask for correction if it contains spaces or uppercase letters.
2. **Validate the title**
   - Must be non-empty.
   - If missing, derive a reasonable default from the id (replace `-` by spaces and capitalize words).
3. **Validate module references**
   - Ensure each module string contains at least one `/` and no `.md` suffix.
   - Optionally, check that `modules/<ref>.md` exists on disk:
     - If some references are missing, report them explicitly.
     - Ask the user whether to proceed anyway or to adjust the module list.
4. **Validate conflicts**
   - Target manifest path is `manifests/<template-id>.yml`.
   - If that file already exists, do not overwrite silently:
     - Explain that the manifest already exists and ask whether the user wants to:
       - stop, or
       - replace it (explicit confirmation required).

## Manifest generation

When inputs are valid and either no manifest exists yet or the user has confirmed overwrite:

1. Build an in-memory YAML structure that matches the v1 manifest schema described in `docs/architecture.md`:
   - `version: 1`
   - `template.id`: template id provided by the user.
   - `template.title`: template title.
   - `priority`: ordered list of blocks:
     - First block: `type: stack-base`, `modules: <base modules>`.
     - Second block (only if any extension modules were provided): `type: stack-extension`, `modules: <extension modules>`.
     - Third block (only if any cross-cutting modules were provided): `type: cross-cutting`, `modules: <cross-cutting modules>`.
2. Serialize this structure to YAML that is consistent with existing manifests (two-space indentation, same key ordering).
3. Write the result to `manifests/<template-id>.yml` in the repo root.

## Compose integration

If the user requested composition (explicitly, or through the command’s default behavior):

1. Run the existing compose script for this manifest only:
   - `python3 scripts/compose.py --manifest manifests/<template-id>.yml`
2. On failure:
   - Capture and surface the error output.
   - Do not modify or delete any existing manifests or templates.
3. On success:
   - Confirm that `templates/<template-id>.cursorrules` now exists.

## Reporting back to the user

After running the command, summarize clearly:

- The **template id** and **title**.
- The exact manifest path created or updated, e.g. `manifests/hono-cloudflare-full-stack.yml`.
- The `priority` blocks and module lists that were written.
- Whether composition was run and, if so, the resulting template path (e.g. `templates/hono-cloudflare-full-stack.cursorrules`).
- Any modules that did not exist on disk (if you allowed the user to proceed anyway).

Keep the behavior aligned with the repository’s architecture:

- Treat `modules/` and `manifests/` as the single source of truth.
- Never hand-edit `templates/`; always use `scripts/compose.py`.
- Prefer explicit confirmation over implicit overwrites.

