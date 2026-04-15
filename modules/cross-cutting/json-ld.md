# JSON-LD Best Practices

- Use valid JSON-LD with `@context` and a Schema.org `@type` appropriate for the page intent.
- Keep structured data aligned with visible page content; never add misleading or unsupported claims.
- Prefer specific Schema.org types and required/recommended properties over generic fallback shapes.
- Keep identifiers stable (`@id`, canonical URLs) to avoid duplicate or conflicting entities.
- Use absolute URLs for links and media references where Schema.org consumers expect resolvable URLs.
- Ensure date/time fields use valid ISO-8601 formats and consistent timezone handling.
- Keep organization, author, and publisher entities consistent across pages and reusable where possible.
- Validate nested objects and array structures to avoid invalid property placements.
- Avoid null, empty, placeholder, or deprecated properties in production payloads.
- Serialize JSON-LD safely in templates/scripts and prevent malformed output from string concatenation.
- Escape user-generated data before injecting it into JSON-LD payloads.
- Validate generated JSON-LD against Schema.org/Google tooling in CI or release checks when feasible.
- Add or update tests for critical JSON-LD generators to catch contract regressions.
