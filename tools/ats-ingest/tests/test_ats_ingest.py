"""Offline unit tests for ats_ingest (no network)."""
import json
from pathlib import Path

import pytest

from ats_ingest.boards import load_boards
from ats_ingest.filters import filter_by_family, title_matches
from ats_ingest.normalize import Posting, content_hash, strip_html
from ats_ingest.fetchers import cached_fetch


def make_posting(title="Financial Analyst", text="Build models in Excel.") -> Posting:
    return Posting(
        source="greenhouse", external_id="1", company="Acme", board_slug="acme",
        title=title, location="NYC", url="https://x/1", posted_at=None, raw_text=text,
    )


def test_strip_html_blocks_and_entities():
    html = "<div><p>Own the &amp; process</p><ul><li>Model in Excel</li><li>Report</li></ul></div>"
    text = strip_html(html)
    assert "Own the & process" in text
    assert "Model in Excel" in text
    assert "<" not in text
    # block tags become line breaks, not run-on words
    assert "process" in text.splitlines()[0] and "Model in Excel" not in text.splitlines()[0]


def test_content_hash_stable_and_sensitive():
    a = content_hash("t", "body")
    assert a == content_hash("t", "body")
    assert a != content_hash("t", "body2")


def test_title_rules_filter_not_force():
    cfg = {"title_rules": ["financial analyst", "fp&a"]}
    keep = make_posting("Senior Financial Analyst")
    drop = make_posting("Software Engineer, Payments")
    fpa = make_posting("FP&A Manager")
    out = filter_by_family([keep, drop, fpa], cfg)
    assert keep in out and fpa in out and drop not in out


def test_title_matches_whitespace_normalized():
    assert title_matches("  Financial   Analyst II ", ["financial analyst"])


def test_boards_seed_shape():
    data = load_boards()
    fams = data["families"]
    for fam in ("financial_analyst", "data_analyst", "security_analyst"):
        cfg = fams[fam]
        assert cfg["title_rules"], fam
        assert cfg["onet_soc"], fam
        assert cfg["greenhouse"] or cfg["lever"] or cfg["ashby"], fam


def test_posting_serialization_roundtrip():
    p = make_posting()
    d = json.loads(p.to_json())
    assert d["source"] == "greenhouse"
    assert d["content_hash"] == p.hash


def test_cached_fetch_hits_cache(tmp_path: Path):
    calls = {"n": 0}

    def fetch():
        calls["n"] += 1
        return {"jobs": [1, 2]}

    a = cached_fetch(tmp_path, "greenhouse", "acme", fetch)
    b = cached_fetch(tmp_path, "greenhouse", "acme", fetch)
    assert a == b == {"jobs": [1, 2]}
    assert calls["n"] == 1  # second call served from cache
    c = cached_fetch(tmp_path, "greenhouse", "acme", fetch, refresh=True)
    assert calls["n"] == 2 and c == a


def test_keyed_sources_noop_without_env(monkeypatch):
    from ats_ingest.fetchers import adzuna, usajobs
    for var in ("USAJOBS_API_KEY", "USAJOBS_EMAIL", "ADZUNA_APP_ID", "ADZUNA_APP_KEY"):
        monkeypatch.delenv(var, raising=False)
    assert usajobs.fetch_keyword(None, "financial analyst") == []
    assert adzuna.fetch_query(None, "financial analyst") == []
