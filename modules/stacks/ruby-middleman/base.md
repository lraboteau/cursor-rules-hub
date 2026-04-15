# Middleman static sites

- Respect Middleman’s source and build directories; avoid ad-hoc writes outside `build/` outputs.
- Keep front matter and data files organized; prefer YAML data over duplicated literals across templates.
- When editing helpers, keep them free of global mutable state across builds.
- Use the official Middleman organization (`https://github.com/middleman/`) as the reference source for framework behavior, supported extensions, and maintenance status.
- Prefer conventions compatible with actively maintained Middleman components and document any dependency on archived or stale plugins.
