"""Shared HTTP plumbing for all fetchers: polite UA, 0.5s/host rate limit,
429/5xx backoff, and a cache-before-fetch layer keyed {source}/{slug}.json."""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlparse

import httpx

log = logging.getLogger("ats_ingest")

USER_AGENT = "skillsimm-ats-ingest/0.1 (https://github.com/SkillSimm/skillsimm-template-submissions)"
HOST_INTERVAL_S = 0.5
_last_hit: dict[str, float] = {}


def _throttle(url: str) -> None:
    host = urlparse(url).netloc
    wait = _last_hit.get(host, 0.0) + HOST_INTERVAL_S - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_hit[host] = time.monotonic()


def http_get_json(
    client: httpx.Client,
    url: str,
    *,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    retries: int = 3,
) -> Any:
    """GET → parsed JSON with throttling and exponential backoff on 429/5xx."""
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    delay = 2.0
    for attempt in range(retries + 1):
        _throttle(url)
        resp = client.get(url, params=params, headers=merged)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (429, 500, 502, 503, 504) and attempt < retries:
            retry_after = resp.headers.get("Retry-After")
            sleep_s = float(retry_after) if retry_after and retry_after.isdigit() else delay
            log.warning("%s → %s; backing off %.1fs", url, resp.status_code, sleep_s)
            time.sleep(sleep_s)
            delay *= 2
            continue
        resp.raise_for_status()
    raise RuntimeError(f"unreachable: {url}")


def cached_fetch(
    cache_dir: Optional[Path],
    source: str,
    slug: str,
    fetch: Callable[[], Any],
    *,
    refresh: bool = False,
) -> Any:
    """Cache-hit-before-fetch (mirrors quarter_pack_build's edgar_cache).
    --refresh bypasses the cache; a fresh fetch always rewrites it."""
    if cache_dir is None:
        return fetch()
    path = Path(cache_dir) / source / f"{slug}.json"
    if path.exists() and not refresh:
        log.info("cache hit: %s/%s", source, slug)
        return json.loads(path.read_text(encoding="utf-8"))
    data = fetch()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    log.info("fetched + cached: %s/%s", source, slug)
    return data


def make_client() -> httpx.Client:
    return httpx.Client(follow_redirects=True, timeout=30.0)
