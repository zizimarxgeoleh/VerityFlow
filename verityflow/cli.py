"""VerityFlow command-line interface.

Subcommands
-----------
* ``graph``   — compile research notes and print structural stats (or export
  the adjacency / edge-list skeleton).
* ``score``   — compute citation coverage, source diversity and support
  strength; emit a JSON score report.
* ``dossier`` — assemble an evidence dossier and render it as Markdown or JSON.
* ``validate``— check note bundles for structural anomalies before ingestion.

All commands read newline-delimited-free JSON (a single array of notes) from a
file or stdin, and write to a file or stdout. The tool is dependency-free.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, List

from .graph import build_graph, compute_stats, to_adjacency, to_edge_list
from .model import load_notes
from .scoring import score_graph
from .dossier import build_dossier, render_json, render_markdown
