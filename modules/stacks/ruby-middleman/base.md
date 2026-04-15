# Middleman static sites

- Respect Middleman’s source and build directories; avoid ad-hoc writes outside `build/` outputs.
- Keep front matter and data files organized; prefer YAML data over duplicated literals across templates.
- When editing helpers, keep them free of global mutable state across builds.
