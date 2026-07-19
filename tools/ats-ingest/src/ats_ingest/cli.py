"""ats-ingest CLI.

    python -m ats_ingest fetch --family financial_analyst --out postings.jsonl \
        [--sources greenhouse,lever,ashby] [--cache-dir cache] [--refresh] \
        [--limit N] [--no-filter] [--boards-file path.json]
    python -m ats_ingest boards [--family X]
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from . import boards as boards_mod
from .fetchers import make_client
from .fetchers import greenhouse, lever, ashby, usajobs, adzuna
from .filters import filter_by_family
from .normalize import Posting

log = logging.getLogger("ats_ingest")

ATS_SOURCES = ("greenhouse", "lever", "ashby")
KEYED_SOURCES = ("usajobs", "adzuna")
ALL_SOURCES = ATS_SOURCES + KEYED_SOURCES


def fetch_family(
    family: str,
    cfg: dict,
    *,
    sources: list[str],
    cache_dir: Path | None,
    refresh: bool = False,
    limit: int = 0,
    apply_filter: bool = True,
) -> list[Posting]:
    """Fetch every configured board for a family, optionally title-filtered."""
    out: list[Posting] = []
    with make_client() as client:
        for source in sources:
            if source in ATS_SOURCES:
                mod = {"greenhouse": greenhouse, "lever": lever, "ashby": ashby}[source]
                for slug in cfg.get(source, []):
                    try:
                        out.extend(mod.fetch_board(client, slug, cache_dir=cache_dir, refresh=refresh))
                    except Exception as e:  # one bad board must not sink the run
                        log.warning("%s/%s failed: %s", source, slug, e)
            elif source == "usajobs":
                out.extend(usajobs.fetch_keyword(client, cfg.get("usajobs_keyword", family),
                                                 cache_dir=cache_dir, refresh=refresh))
            elif source == "adzuna":
                out.extend(adzuna.fetch_query(client, cfg.get("adzuna_query", family),
                                              cache_dir=cache_dir, refresh=refresh))
            if limit and len(out) >= limit and not apply_filter:
                break
    if apply_filter:
        out = filter_by_family(out, cfg)
    if limit:
        out = out[:limit]
    return out


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser(prog="ats-ingest", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="fetch postings for a family")
    f.add_argument("--family", required=True)
    f.add_argument("--sources", default="greenhouse,lever,ashby",
                   help=f"comma list from {ALL_SOURCES}")
    f.add_argument("--cache-dir", type=Path, default=None)
    f.add_argument("--refresh", action="store_true", help="bypass cache")
    f.add_argument("--limit", type=int, default=0)
    f.add_argument("--no-filter", action="store_true",
                   help="skip title_rules filtering (raw board dump)")
    f.add_argument("--boards-file", type=Path, default=None,
                   help="override the packaged job_boards.json")
    f.add_argument("--out", type=Path, default=None, help="write JSONL here (default stdout)")

    b = sub.add_parser("boards", help="list configured boards")
    b.add_argument("--family", default=None)

    args = ap.parse_args(argv)
    data = boards_mod.load_boards(getattr(args, "boards_file", None))
    families = data.get("families", data)

    if args.cmd == "boards":
        names = [args.family] if args.family else sorted(families)
        for name in names:
            cfg = families.get(name)
            if not cfg:
                print(f"unknown family: {name}", file=sys.stderr)
                return 2
            counts = {s: len(cfg.get(s, [])) for s in ATS_SOURCES}
            print(f"{name}: {counts} title_rules={cfg.get('title_rules')}")
        return 0

    cfg = families.get(args.family)
    if not cfg:
        print(f"unknown family: {args.family} (have: {', '.join(sorted(families))})", file=sys.stderr)
        return 2
    sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    bad = [s for s in sources if s not in ALL_SOURCES]
    if bad:
        print(f"unknown sources: {bad}", file=sys.stderr)
        return 2

    postings = fetch_family(args.family, cfg, sources=sources, cache_dir=args.cache_dir,
                            refresh=args.refresh, limit=args.limit,
                            apply_filter=not args.no_filter)
    lines = [p.to_json() for p in postings]
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        log.info("wrote %d postings → %s", len(lines), args.out)
    else:
        for ln in lines:
            print(ln)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
