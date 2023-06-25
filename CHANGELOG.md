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

### Fixed

- Unknown relations are rejected at parse time with a message naming the closed
  vocabulary, instead of failing later during scoring.

## [1.0.0] - 2025-12-02

### Added

- Stable command-line contract: `graph`, `score`, `dossier` and `validate`,
  each reading from `-i`/stdin and writing to `-o`/stdout.
- The `.NET` summariser `VerityFlow.Runtime` consumes the JSON dossier and
  prints a provenance health score with a letter grade.

## [0.8.0] - 2024-05-21

### Added

- Confidence-weighted support strength: each relation carries a signed weight
  (`supports` +1.0, `qualifies` +0.5, `context` +0.25, `refutes` -1.0) scaled by
  the annotator confidence and squashed through a logistic curve.

## [0.7.0] - 2023-06-27

### Added

- `validate` reports dangling links and orphan quotations and exits `2` when
  either is found.
- Markdown dossiers render verdict badges and a per-quotation evidence table.

## [0.6.0] - 2022-07-12

### Added

- Evidence dossiers in Markdown and JSON, with a per-claim verdict
  (`well-supported` through `refuted`).

## [0.5.0] - 2021-06-29

### Added

- Citation coverage: the fraction of claims carrying at least one supporting
  evidence link.

## [0.4.0] - 2020-07-07

### Added

- Source diversity: normalised Shannon entropy over the provenance domains
  behind a claim, with `www.` stripped from host names.

## [0.3.0] - 2019-06-18

### Added

- Graph compilation with de-duplication by deterministic id, structural
  statistics, and adjacency and edge-list exports for external tools.

## [0.2.0] - 2018-05-22

### Added

- `graph` subcommand with `stats`, `adjacency` and `edges` output modes.

## [0.1.0] - 2017-06-14

### Added

- First public release: the data model for claims, sources, quotations and
  evidence links; deterministic content-hash ids; JSON research-note ingestion
  keyed by `source_title` and `quotation_text`.

<!-- draft note 686 -->
