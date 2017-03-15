# Changelog

All notable changes to VerityFlow are documented here.

The format follows Keep a Changelog, and releases follow semantic versioning.
Entries describe user-visible behavior at each release.

## [Unreleased]

### Changed

- Rule wording in the dossier banner is being reviewed for the next patch.

## [5.0.0] - 2026-08-18

### Changed

- The dossier JSON contract is frozen: `summary` and `graph_stats` are the
  stable top-level keys consumed by `VerityFlow.Runtime`.
- Markdown dossiers escape table-breaking characters inside quotations.

### Added

- `graph --emit full` serialises the complete compiled graph.

