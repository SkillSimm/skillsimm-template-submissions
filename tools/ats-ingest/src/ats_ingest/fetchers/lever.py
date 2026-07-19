"""Lever public postings API — keyless, full descriptions.

GET https://api.lever.co/v0/postings/{company}?mode=json
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import httpx

from ..normalize import Posting, strip_html
from . import cached_fetch, http_get_json

SOURCE = "lever"
API = "https://api.lever.co/v0/postings/{company}"


def _ms_to_iso(ms) -> Optional[str]:
    try:
        return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).isoformat()
    except (TypeError, ValueError):
        return None


def fetch_board(
    client: httpx.Client,
    company: str,
    *,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> list[Posting]:
    data = cached_fetch(
        cache_dir, SOURCE, company,
        lambda: http_get_json(client, API.format(company=company), params={"mode": "json"}),
        refresh=refresh,
    )
    postings: list[Posting] = []
    for job in data or []:
        cats = job.get("categories") or {}
        text = job.get("descriptionPlain") or strip_html(job.get("description") or "")
        postings.append(Posting(
            source=SOURCE,
            external_id=str(job["id"]),
            company=company,
            board_slug=company,
            title=(job.get("text") or "").strip(),
            location=(cats.get("location") or "").strip(),
            url=job.get("hostedUrl") or "",
            posted_at=_ms_to_iso(job.get("createdAt")),
            raw_text=text,
            raw_meta={"team": cats.get("team"), "commitment": cats.get("commitment")},
        ))
    return postings
