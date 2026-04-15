# Testing Python features

- Prefer `pytest` with clear fixture scopes; avoid hidden global state between tests.
- Cover CLI and integration behavior with lightweight end-to-end tests when stack workflows depend on scripts.
- Mock external services by default and keep network/file-system integration tests explicit and isolated.
