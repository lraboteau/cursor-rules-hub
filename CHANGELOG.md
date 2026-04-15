# Changelog

This file tracks notable changes to templates, modules, manifests, tooling, and documentation workflows.

## Unreleased

### Added

- New public templates: `cloudflare-workers`, `hono`, `hono-cloudflare-workers`, `nodejs`, `python`, `rust`, `postgresql`, `tailwind`, and `sql1`.
- New reusable modules across fundamentals, stacks, and cross-cutting areas, including `rest-api`, `accessibility`, and `json-ld`.
- A repository-level `CHANGELOG.md` with an `Unreleased` workflow for ongoing release notes.

### Changed

- Replaced legacy `hono-workers` stack with split `hono` and `cloudflare-workers` stacks plus a combined template.
- Renamed stack module path from `stacks/sql1/*` to `stacks/cloudflare-sql1/*` and aligned the `sql1` template title.
- Expanded sync/install test coverage to run against all template IDs defined in `manifests/*.yml`.
- Updated docs, examples, and command guidance to use current template names and workflow expectations.

### Fixed

- Added a compose-level guard test to detect duplicate top-level module titles that could silently override sections.
- Removed non-web-specific `json-ld` guidance from SQL-focused manifests to reduce irrelevant template noise.

### Removed

- Removed the deprecated `hono-workers` stack modules, manifest, and generated template.

## Maintenance notes

- Update this file in the same change set when behavior, workflows, or public templates change.
- Keep entries short, user-facing, and grouped under `Unreleased`.
