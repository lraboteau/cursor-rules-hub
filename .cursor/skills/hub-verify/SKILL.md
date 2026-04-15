---
name: hub-verify
description: Runs the standard repository verification before hand-off or PR using compose --check and pytest, then interprets failures to guide minimal fixes.
---

# Hub Verify

## When to use this skill

- Before finalizing changes.
- Before opening a PR or requesting review.
- After changing template sources or scripts/tests.

## Required validation sequence

1. Verify template consistency:
   - `python scripts/compose.py --check`
2. Run test suite:
   - `python -m pytest -q`
3. If a check fails:
   - fix the root cause in source files;
   - rerun the failing command until it passes;
   - rerun both commands for final validation.

## Quick interpretation

- `compose` error:
  - template drift -> regenerate with `python scripts/compose.py --all`;
  - invalid manifest/module -> fix the relevant source file.
- test error:
  - fix behavior or test according to intended project behavior.

## Useful commands

```bash
# Check drift only
python scripts/compose.py --check

# Test suite
python -m pytest -q

# Common drift recovery flow
python scripts/compose.py --all && python scripts/compose.py --check && python -m pytest -q
```
