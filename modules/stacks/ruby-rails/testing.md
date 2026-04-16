# Ruby on Rails Testing Discipline

- Add or update tests for models, controllers, jobs, mailers, and integration flows affected by each change.
- Keep regressions reproducible with focused fixtures and deterministic setup.
- Run `bundle exec rake test` and targeted suites for impacted frameworks before merge.
- Treat security-sensitive regressions (auth, params handling, session behavior) as blockers.
