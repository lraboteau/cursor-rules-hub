# Testing Rust features

- Prefer `cargo test` unit tests close to implementation and integration tests under `tests/` for public behavior.
- Keep tests deterministic: avoid timing-sensitive assertions and isolate filesystem/network side effects with temp resources and mocks.
- Add compile-time checks (`clippy`, `fmt`, feature-matrix tests) when stack changes impact API surface or conditional builds.
