# Testing Tailwind Features

- Prefer component-level tests that verify key class composition for variants, states, and responsive behavior.
- Add snapshot or visual regression coverage when utility changes can affect layout or interaction affordances.
- Cover interactive and accessibility states (`hover`, `focus-visible`, `disabled`, `aria-*`) to prevent styling regressions.
- Keep tests resilient by asserting meaningful class groups/behavior rather than brittle full-string matches when possible.
