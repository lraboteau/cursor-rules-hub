# Security hygiene

- Never commit secrets, tokens, or private keys; use environment variables or the platform secret store already adopted in the project.
- Validate and encode untrusted input at trust boundaries; prefer parameterized queries for SQL.
- Favor least privilege for tokens and IAM-style permissions discussed in the repo docs.
