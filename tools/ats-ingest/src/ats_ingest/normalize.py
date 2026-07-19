"""Normalize raw ATS payloads into a common Posting shape."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, asdict
from html.parser import HTMLParser
from typing import Any, Optional


class _TextExtractor(HTMLParser):
    _BLOCK_TAGS = {"p", "div", "li", "br", "ul", "ol", "h1", "h2", "h3", "h4", "tr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in self._BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_data(self, data: str) -> None:
        self.chunks.append(data)


def strip_html(html: str) -> str:
    """HTML → plain text using only the stdlib. Collapses blank runs."""
    if not html:
        return ""
    parser = _TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        return html  # malformed markup: better raw than empty
    text = "".join(parser.chunks)
    lines = [ln.strip() for ln in text.splitlines()]
    out: list[str] = []
    for ln in lines:
        if ln:
            out.append(ln)
        elif out and out[-1] != "":
            out.append("")
    return "\n".join(out).strip()


def content_hash(title: str, raw_text: str) -> str:
    return hashlib.sha256(f"{title}\n{raw_text}".encode("utf-8", "replace")).hexdigest()


@dataclass
class Posting:
    """The common shape every fetcher returns."""

    source: str            # greenhouse | lever | ashby | usajobs | adzuna
    external_id: str       # source-native id; (source, external_id) is the dedupe key
    company: str
    board_slug: str
    title: str
    location: str
    url: str
    posted_at: Optional[str]   # ISO 8601 when the source provides it
    raw_text: str              # HTML-stripped description
    raw_meta: dict[str, Any] = field(default_factory=dict)

    @property
    def hash(self) -> str:
        return content_hash(self.title, self.raw_text)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["content_hash"] = self.hash
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)
