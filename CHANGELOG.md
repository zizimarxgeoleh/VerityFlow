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

## [4.0.0] - 2026-06-23

### Changed

- The `validate` exit contract is now explicit: `2` for structural anomalies,
  `1` for unreadable input. Scripts that treated any non-zero code the same are
  unaffected; CI gates can now distinguish the two cases.
- Score output rounds every float to four decimals for diff-friendly reports.

## [3.1.0] - 2026-04-28

### Added

- Per-claim `n_domains`, `n_supporting` and `n_refuting` counters in the score
  report, so consumers no longer have to re-derive them from the graph.
- Dossier entries are ordered by descending support index with the claim id as
  a deterministic tie-breaker.

## [2.6.0] - 2026-02-24

### Added

- `dossier --title` sets the report heading for Markdown and JSON output.
- The Markdown dossier opens with a "Graph at a glance" table covering node,
  link, dangling and orphan counts.

## [1.0.1] - 2026-01-13

