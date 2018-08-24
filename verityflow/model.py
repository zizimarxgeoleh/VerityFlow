"""Core data model for VerityFlow provenance graphs.

The model expresses four node kinds and the edges that bind them:

* :class:`Claim`      — an assertion made in a document.
* :class:`Source`     — a document, dataset or artefact that can be cited.
* :class:`Quotation`  — a verbatim span extracted from a source.
* :class:`EvidenceLink` — a typed edge stating how a quotation relates to a
  claim (supports, refutes, qualifies or context).

A :class:`ResearchNote` is the ingestion unit: it carries one claim plus the
quotations and sources that back (or challenge) it. A collection of research
notes is compiled into a :class:`ProvenanceGraph`.

All structures are plain dataclasses so they serialise cleanly to JSON with the
standard library only.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, Iterable, List, Optional


# Relation vocabulary used by evidence links. The weight expresses how much a
# given relation contributes to (or detracts from) claim support strength.
