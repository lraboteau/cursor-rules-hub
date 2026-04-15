# Tailwind Best Practices

- Keep utility classes readable and predictable by using a consistent class ordering strategy.
- Avoid long, duplicated class strings; extract reusable class groups into shared components or helpers.
- Prefer semantic component boundaries over repeating the same utility blocks across files.
- Keep conditional classes explicit and composable (for example with `clsx`/`cva` patterns) instead of inline string sprawl.
- Use design tokens and Tailwind theme scales (`spacing`, `colors`, `fontSize`) before arbitrary values.
- Use arbitrary values only when necessary and document why when intent is not obvious.
- Define interactive and accessibility states intentionally (`hover`, `focus-visible`, `disabled`, `aria-*` where relevant).
- Keep responsive behavior explicit (`sm`/`md`/`lg`...) and avoid conflicting breakpoint overrides.
- Prefer stable layout primitives (`flex`, `grid`, `gap`) over brittle spacing hacks.
- Ensure dark mode and contrast expectations are handled consistently where the UI supports theme switching.
- Keep class decisions in the component layer; avoid mixing style concerns into unrelated business logic.
- Add or update UI tests/snapshots when class composition changes impact rendering or interaction behavior.
