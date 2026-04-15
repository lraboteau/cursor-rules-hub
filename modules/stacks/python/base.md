# Python conventions

- Target Python 3.12+ unless the repository specifies another runtime baseline.
- Prefer explicit type hints on public functions and module boundaries; keep mypy/pyright clean when present.
- Use `pathlib`, context managers, and small pure functions to keep code testable and side effects explicit.
- Keep dependency and packaging workflows aligned with the existing project tooling (`pip`, `poetry`, or `uv`) instead of mixing approaches.
