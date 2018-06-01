"""Evidence dossier assembly and rendering.

A *dossier* is the human-facing deliverable: for each claim it lays out the
support verdict, the diversity of provenance, and the full chain of quotations
and sources that underpin (or contest) the claim. Dossiers render to Markdown
for review and to JSON for downstream tooling.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from .graph import compute_stats
from .model import ProvenanceGraph
from .scoring import ClaimScore, ScoreReport, score_graph


def _verdict(score: ClaimScore) -> str:
