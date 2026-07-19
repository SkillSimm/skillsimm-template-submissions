"""USAJobs search API — free key, env-gated. No-ops with a log line when
USAJOBS_API_KEY / USAJOBS_EMAIL are unset (ATS sources alone reach 5-20k).

https://developer.usajobs.gov/  GET https://data.usajobs.gov/api/search
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
SOURCE = "usajobs"
API = "https://data.usajobs.gov/api/search"


def fetch_keyword(
    client: httpx.Client,
    keyword: str,
    *,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    limit: int = 500,
) -> list[Posting]:
    key = os.environ.get("USAJOBS_API_KEY")
    email = os.environ.get("USAJOBS_EMAIL")
    if not key or not email:
        log.info("usajobs: USAJOBS_API_KEY/USAJOBS_EMAIL unset — skipping (no-op)")
        return []
    slug = keyword.lower().replace(" ", "-")

    def _fetch():
        return http_get_json(
            client, API,
            params={"Keyword": keyword, "ResultsPerPage": min(limit, 500)},
            headers={"Authorization-Key": key, "User-Agent": email},
        )

    data = cached_fetch(cache_dir, SOURCE, slug, _fetch, refresh=refresh)
    postings: list[Posting] = []
    for item in ((data or {}).get("SearchResult") or {}).get("SearchResultItems", []):
        d = item.get("MatchedObjectDescriptor") or {}
        locs = d.get("PositionLocation") or []
        desc = (d.get("UserArea") or {}).get("Details") or {}
        body = "\n".join(filter(None, [
            strip_html(desc.get("MajorDuties") if isinstance(desc.get("MajorDuties"), str)
                       else "\n".join(desc.get("MajorDuties") or [])),
            strip_html(d.get("QualificationSummary") or ""),
        ]))
        postings.append(Posting(
            source=SOURCE,
            external_id=str(d.get("PositionID") or item.get("MatchedObjectId")),
            company=(d.get("OrganizationName") or "US Government").strip(),
            board_slug=slug,
            title=(d.get("PositionTitle") or "").strip(),
            location=(locs[0].get("LocationName") if locs else "").strip(),
            url=d.get("PositionURI") or "",
            posted_at=d.get("PublicationStartDate"),
            raw_text=body,
            raw_meta={"department": d.get("DepartmentName")},
        ))
    return postings
