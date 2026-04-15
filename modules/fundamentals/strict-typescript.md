# TypeScript discipline

- Enable `strict` in `tsconfig.json` and fix errors instead of loosening compiler options.
- Prefer explicit types on public APIs; avoid `any` unless isolated and justified in a short comment.
- Use `unknown` for untrusted input and narrow before use.
