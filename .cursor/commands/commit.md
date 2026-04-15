Create one safe local commit from current repository changes. Do not push.

## Goal

Produce a clean, reviewable local commit that reflects the actual staged changes and follows repository commit conventions.

## Required workflow

1. Inspect repository state first:
   - `git status --short`
   - `git diff`
   - `git diff --cached`
   - `git log --oneline -10`
2. If there are no tracked or untracked changes to commit, stop and report it.
3. Exclude sensitive or irrelevant files from the commit:
   - do not commit secrets (`.env`, credentials, tokens, private keys);
   - do not include unrelated generated/local artifacts.
4. Stage intended files (`git add -A` only if all current changes are intended).
5. Re-check staged content with `git diff --cached`.
6. Generate a commit message from staged changes:
   - imperative mood;
   - concise and specific;
   - first line <= 72 characters;
   - avoid vague wording ("update files", "fix stuff");
   - align with recent style from `git log`.
7. Commit using the generated message.
8. Show commit output and run `git status` to confirm a clean or expected state.

## Guardrails

- Never run `git push`.
- Never run destructive git commands (`reset --hard`, force push, etc.).
- Never use `git commit --amend` unless explicitly requested.
- Never use `--no-verify` or other hook-skipping flags unless explicitly requested.
- Never create an empty commit when there are no changes.
- If hooks fail, fix issues and create a new commit (do not bypass hooks).