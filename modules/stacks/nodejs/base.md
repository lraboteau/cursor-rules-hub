# Node.js conventions

- Target active LTS Node.js unless the repository explicitly pins another runtime.
- Prefer ESM or CommonJS consistently with the existing codebase; avoid mixing module systems without clear boundaries.
- Keep async flows explicit with `async`/`await`, handle promise rejections centrally, and avoid unhandled background work.
- Align dependency and script workflows with the project package manager (`npm`, `pnpm`, or `yarn`) and lockfile conventions.
