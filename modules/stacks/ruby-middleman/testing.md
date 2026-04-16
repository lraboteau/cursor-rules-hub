# Ruby Middleman Testing Discipline

- Add or update tests for CLI behavior, project generation, and build output correctness.
- Keep regression tests focused on reproducible failures and cross-platform behavior.
- Run `bundle exec rake test` and relevant integration checks before merge.
- Treat build pipeline breakage and template rendering regressions as release blockers.
