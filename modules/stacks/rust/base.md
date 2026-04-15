# Rust conventions

- Prefer stable Rust and the existing edition/toolchain configured by the repository before introducing newer language features.
- Model ownership and lifetimes clearly; prefer borrowing over cloning on hot paths unless clarity or safety requires otherwise.
- Keep `Result`-based error propagation explicit (`thiserror`/`anyhow` only when consistent with the project) and avoid `unwrap()` in production code.
- Organize crates/modules around clear domain boundaries and keep public APIs small and well-documented.
