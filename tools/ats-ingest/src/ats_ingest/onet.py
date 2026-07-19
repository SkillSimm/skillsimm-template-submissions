"""One-shot O*NET anchor import.

Reads the free O*NET database text files (unzipped from
https://www.onetcenter.org/database.html — tab-separated) and emits
data/onet_anchors.json: per SOC code, the authoritative task/tool/technology
vocabulary used as canonical anchors downstream.

Usage:
    python -m ats_ingest.onet --onet-dir ~/Downloads/db_30_0_text \
        --socs 13-2051.00,15-2051.01,15-1212.00 \
        --out src/ats_ingest/data/onet_anchors.json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

FILES = {
    "technology": "Technology Skills.txt",
    "tools": "Tools Used.txt",
    "tasks": "Task Statements.txt",
}


def _rows(path: Path):
    with path.open(encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        yield from reader


def _col(row: dict, *names: str) -> str:
    for n in names:
        if n in row and row[n]:
            return row[n].strip()
    return ""


def build_anchors(onet_dir: Path, socs: list[str]) -> dict:
    anchors: dict[str, dict] = {
        soc: {"technology": [], "tools": [], "tasks": []} for soc in socs
    }
    socset = set(socs)

    path = onet_dir / FILES["technology"]
    if path.exists():
        for row in _rows(path):
            soc = _col(row, "O*NET-SOC Code")
            if soc in socset:
                name = _col(row, "Example", "Commodity Title")
                if name and name not in anchors[soc]["technology"]:
                    anchors[soc]["technology"].append(name)

    path = onet_dir / FILES["tools"]
    if path.exists():
        for row in _rows(path):
            soc = _col(row, "O*NET-SOC Code")
            if soc in socset:
                name = _col(row, "Example", "Commodity Title")
                if name and name not in anchors[soc]["tools"]:
                    anchors[soc]["tools"].append(name)

    path = onet_dir / FILES["tasks"]
    if path.exists():
        for row in _rows(path):
            soc = _col(row, "O*NET-SOC Code")
            if soc in socset:
                task = _col(row, "Task")
                if task and task not in anchors[soc]["tasks"]:
                    anchors[soc]["tasks"].append(task)

    return anchors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--onet-dir", required=True, type=Path,
                    help="directory of unzipped O*NET database text files")
    ap.add_argument("--socs", required=True,
                    help="comma-separated O*NET-SOC codes, e.g. 13-2051.00,15-1212.00")
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).parent / "data" / "onet_anchors.json")
    args = ap.parse_args(argv)

    socs = [s.strip() for s in args.socs.split(",") if s.strip()]
    anchors = build_anchors(args.onet_dir, socs)
    for soc in socs:
        n = sum(len(v) for v in anchors[soc].values())
        print(f"{soc}: {len(anchors[soc]['technology'])} technology, "
              f"{len(anchors[soc]['tools'])} tools, {len(anchors[soc]['tasks'])} tasks "
              f"({n} total)")
        if n == 0:
            print(f"  WARNING: no anchors found for {soc} — check --onet-dir files", file=sys.stderr)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(anchors, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
