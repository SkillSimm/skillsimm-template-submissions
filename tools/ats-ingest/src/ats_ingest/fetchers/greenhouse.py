"""Greenhouse public board API — keyless, full descriptions.

GET https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true
"""
from __future__ import annotations

import html as html_mod
from pathlib import Path
from typing import Optional

import httpx

from ..normalize import Posting, strip_html
from . import cached_fetch, http_get_json

SOURCE = "greenhouse"
API = "https://boards-api.greenhouse.io/v1/boards/{board}/jobs"


def fetch_board(
    client: httpx.Client,
    board: str,
    *,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> list[Posting]:
    data = cached_fetch(
        cache_dir, SOURCE, board,
        lambda: http_get_json(client, API.format(board=board), params={"content": "true"}),
        refresh=refresh,
    )
    postings: list[Posting] = []
    for job in data.get("jobs", []):
        company = (job.get("company_name") or board).strip()
        postings.append(Posting(
            source=SOURCE,
            external_id=str(job["id"]),
            company=company,
            board_slug=board,
            title=(job.get("title") or "").strip(),
            location=((job.get("location") or {}).get("name") or "").strip(),
            url=job.get("absolute_url") or "",
            posted_at=job.get("first_published") or job.get("updated_at"),
            # Greenhouse serves `content` HTML-escaped (&lt;p&gt;…) — unescape
            # to real markup before stripping.
            raw_text=strip_html(html_mod.unescape(job.get("content") or "")),
            raw_meta={"departments": [d.get("name") for d in job.get("departments") or []]},
        ))
    return postings
