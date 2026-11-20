#!/usr/bin/env python3
"""Validate SkillSimm template packages.

Usage:
    python scripts/validate_package.py [templates/<slug> ...]

With no arguments, validates every package folder under templates/ and
examples/. Exits non-zero when any package has errors — this is the required
PR check.

Two formats are accepted, picked per folder:
  * app format  — template.json + stages/*.json (the starters in examples/),
                  checked by folder_template.py (stdlib only);
  * lite format — template.yaml + steps.yaml (AI/MCP submissions), checked by
                  the vendored template_package module (needs pydantic, pyyaml).

The `template_package` module next to this script is vendored from
Simulation_TaskFlow/backend/app/template_package (canonical source); keep the
two in sync when the schema evolves.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from folder_template import validate_folder  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent
SEARCH_DIRS = ("templates", "examples")


def _discover() -> list[Path]:
    found = set()
    for d in SEARCH_DIRS:
        root = REPO_ROOT / d
        for marker in ("template.json", "template.yaml"):
            found.update(p.parent for p in root.rglob(marker))
    return sorted(found)


def _validate(folder: Path):
    if (folder / "template.json").exists():
        return validate_folder(folder)
    from template_package import validate_package  # lite format; needs pydantic + pyyaml
    return validate_package(folder)


def main(argv: list[str]) -> int:
    if argv:
        folders = [Path(a) for a in argv]
    else:
        folders = _discover()
    if not folders:
        print("No template packages found under templates/ or examples/")
        return 0

    failed = 0
    for folder in folders:
        issues = _validate(folder)
        errors = [i for i in issues if i.severity == "error"]
        warnings = [i for i in issues if i.severity == "warning"]
        status = "FAIL" if errors else "PASS"
        print(f"\n{status}  {folder}")
        for i in errors + warnings:
            print(f"  {i}")
        if errors:
            failed += 1

    print(f"\n{len(folders)} package(s) checked, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
