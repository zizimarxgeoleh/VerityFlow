# VerityFlow — Claim Provenance Graph Builder

VerityFlow turns a pile of research notes into a rigorous, inspectable **provenance graph**. Every assertion you make becomes a *claim* node; every document you lean on becomes a *source*; every verbatim span you pull becomes a *quotation*; and every judgement you form — "this backs the claim", "this contradicts it", "this only qualifies it" — becomes a typed *evidence link*. From that graph VerityFlow computes **citation coverage**, **source diversity** and **claim support strength**, then assembles a publication-ready **evidence dossier** in Markdown or JSON. A companion .NET runtime reads the dossier and stamps it with an executive **provenance health grade**.

If you have ever finished a report and wondered *which of my claims are actually cited, and how well*, VerityFlow answers that question mechanically and reproducibly.

![Provenance graph](docs/assets/provenance-graph.svg)

VerityFlow is deliberately small and dependency-free. The core is a Python 3.11 package (`verityflow`) built entirely on the standard library; the summariser is a single-file .NET 9 console app that uses only the base class library. There is no database, no service to run, no network call anywhere in the pipeline. You point it at a JSON bundle of notes and you get back structured verdicts.

---

## Table of contents

- [Why provenance graphs](#why-provenance-graphs)
- [The mental model](#the-mental-model)
- [Architecture](#architecture)
- [Install and run](#install-and-run)
- [The data schema](#the-data-schema)
- [Command reference](#command-reference)
- [Scoring algorithms in depth](#scoring-algorithms-in-depth)
- [The dossier format](#the-dossier-format)
- [The .NET summariser](#the-net-summariser)
- [CLI recipes](#cli-recipes)
- [Operations and exit codes](#operations-and-exit-codes)
- [Extension seams](#extension-seams)
- [Design principles](#design-principles)
- [Glossary](#glossary)

---

## Why provenance graphs

Most citation tooling treats references as a flat bibliography: a list at the end of a document with no machine-readable relationship to the sentences that depend on them. That flatness hides three failure modes that VerityFlow is built to expose:

1. **Uncited claims.** A confident sentence with no attached evidence reads exactly like a well-supported one. A flat reference list cannot tell them apart. A provenance graph can: an uncited claim is simply a node with no inbound supporting edge.

2. **Monoculture citations.** Five citations that all trace back to the same author, publisher or domain give the *appearance* of thorough sourcing while providing almost none of its substance. VerityFlow measures the **diversity** of the provenance domains behind each claim, so a single-source claim cannot masquerade as broadly supported.

3. **Buried contradictions.** When a source you cite actually *undercuts* your claim, that tension should be surfaced, not smoothed over. VerityFlow models `refutes` and `qualifies` relations as first-class edges and folds them into a signed support index, so a contested claim is flagged rather than quietly averaged away.

By representing the whole apparatus as a directed graph, VerityFlow makes these properties *computable*. Coverage becomes a ratio. Diversity becomes an entropy. Support becomes a bounded index. And the dossier turns those numbers back into prose a human reviewer can act on.

---

## The mental model

VerityFlow has exactly four node kinds and one edge kind. Keeping the vocabulary this small is intentional — it is what lets the whole tool stay dependency-free and auditable.
