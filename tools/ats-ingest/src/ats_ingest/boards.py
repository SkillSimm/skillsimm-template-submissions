"""Load the committed board seed list (data/job_boards.json).

The seed list is the community contribution surface: adding a company's
Greenhouse/Lever/Ashby slug to your family is a one-line PR.
"""
from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path
from typing import Optional


def load_boards(path: Optional[Path] = None) -> dict:
    """Return {family: {greenhouse: [...], lever: [...], ashby: [...],
    title_rules: [...], onet_soc, adzuna_query, usajobs_keyword}}."""
    if path is not None:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return json.loads(files("ats_ingest.data").joinpath("job_boards.json").read_text(encoding="utf-8"))
