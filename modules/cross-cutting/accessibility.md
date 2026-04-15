# Accessibility best practices

- Prefer semantic HTML elements before ARIA workarounds (`button`, `nav`, `main`, `label`, `fieldset`, etc.).
- Ensure every interactive element is keyboard accessible and usable without a mouse.
- Keep visible and logical focus behavior (`:focus-visible`, focus order, no keyboard traps).
- Use accessible names for controls (`label`, `aria-label`, `aria-labelledby`) and avoid unlabeled inputs/buttons.
- Keep heading hierarchy meaningful and sequential for screen-reader navigation.
- Ensure sufficient color contrast and do not rely on color alone to convey meaning.
- Provide text alternatives for non-text content (`alt`, captions/transcripts where relevant).
- Announce dynamic UI changes appropriately (live regions and state updates when necessary).
- Keep form validation accessible: clear error messages, field association, and error summary behavior.
- Use ARIA only when native semantics are insufficient; avoid redundant or conflicting ARIA attributes.
- Respect reduced motion and avoid animation that harms readability or usability.
- Include accessibility checks in delivery workflow (linting, automated scans, and targeted manual keyboard/screen-reader checks).
- Add or update tests when interaction or UI structure changes can impact accessibility behavior.
