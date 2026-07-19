"""Ashby public posting API — keyless.

GET https://api.ashbyhq.com/posting-api/job-board/{board}?includeCompensation=true
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import httpx

from ..normalize import Posting, strip_html
from . import cached_fetch, http_get_json

SOURCE = "ashby"
API = "https://api.ashbyhq.com/posting-api/job-board/{board}"


def fetch_board(
    client: httpx.Client,
    board: str,
    *,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> list[Posting]:
    data = cached_fetch(
        cache_dir, SOURCE, board,
        lambda: http_get_json(client, API.format(board=board)),
        refresh=refresh,
    )
    postings: list[Posting] = []
    for job in (data or {}).get("jobs", []):
        postings.append(Posting(
            source=SOURCE,
            external_id=str(job.get("id")),
            company=board,
            board_slug=board,
            title=(job.get("title") or "").strip(),
            location=(job.get("location") or "").strip(),
            url=job.get("jobUrl") or job.get("applyUrl") or "",
            posted_at=job.get("publishedAt"),
            raw_text=strip_html(job.get("descriptionHtml") or "") or (job.get("descriptionPlain") or ""),
            raw_meta={"department": job.get("department"), "team": job.get("team"),
                      "remote": job.get("isRemote")},
        ))
    return postings
