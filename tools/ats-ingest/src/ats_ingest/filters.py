"""Title-rule filtering: keep postings whose title matches a family's rules.

Filter, don't force — a posting that matches no family is dropped from family
feeds rather than being assigned to the closest one.
"""
from __future__ import annotations

from typing import Iterable

from .normalize import Posting


def title_matches(title: str, rules: Iterable[str]) -> bool:
    t = " ".join(title.lower().split())
    return any(rule.lower() in t for rule in rules)


def matches_family(posting: Posting, family_cfg: dict) -> bool:
    return title_matches(posting.title, family_cfg.get("title_rules", []))


def filter_by_family(postings: Iterable[Posting], family_cfg: dict) -> list[Posting]:
    return [p for p in postings if matches_family(p, family_cfg)]
