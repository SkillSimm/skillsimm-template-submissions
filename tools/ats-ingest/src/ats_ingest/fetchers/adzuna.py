"""Adzuna search API — free key, env-gated. No-ops with a log line when
ADZUNA_APP_ID / ADZUNA_APP_KEY are unset.

https://developer.adzuna.com/  GET https://api.adzuna.com/v1/api/jobs/us/search/1
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Optional

import httpx

from ..normalize import Posting, strip_html
from . import cached_fetch, http_get_json

log = logging.getLogger("ats_ingest")
SOURCE = "adzuna"
API = "https://api.adzuna.com/v1/api/jobs/us/search/1"


def fetch_query(
    client: httpx.Client,
    query: str,
    *,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    limit: int = 50,
) -> list[Posting]:
    app_id = os.environ.get("ADZUNA_APP_ID")
    app_key = os.environ.get("ADZUNA_APP_KEY")
    if not app_id or not app_key:
        log.info("adzuna: ADZUNA_APP_ID/ADZUNA_APP_KEY unset — skipping (no-op)")
        return []
    slug = query.lower().replace(" ", "-")

    def _fetch():
        return http_get_json(client, API, params={
            "app_id": app_id, "app_key": app_key,
            "what": query, "results_per_page": min(limit, 50),
            "content-type": "application/json",
        })

    data = cached_fetch(cache_dir, SOURCE, slug, _fetch, refresh=refresh)
    postings: list[Posting] = []
    for job in (data or {}).get("results", []):
        postings.append(Posting(
            source=SOURCE,
            external_id=str(job.get("id")),
            company=((job.get("company") or {}).get("display_name") or "").strip(),
            board_slug=slug,
            title=(job.get("title") or "").strip(),
            location=((job.get("location") or {}).get("display_name") or "").strip(),
            url=job.get("redirect_url") or "",
            posted_at=job.get("created"),
            raw_text=strip_html(job.get("description") or ""),
            raw_meta={"category": (job.get("category") or {}).get("label")},
        ))
    return postings
