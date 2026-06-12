#!/usr/bin/env python3
"""Validate SkillSimm template packages.

Usage:
    python scripts/validate_package.py [templates/<slug> ...]

With no arguments, validates every package folder under templates/.
Exits non-zero when any package has errors — this is the required PR check.

The `template_package` module next to this script is vendored from
Simulation_TaskFlow/backend/app/template_package (canonical source); keep the
two in sync when the schema evolves.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from template_package import validate_package  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent


def main(argv: list[str]) -> int:
    if argv:
        folders = [Path(a) for a in argv]
    else:
        folders = sorted(
            p.parent for p in (REPO_ROOT / "templates").rglob("template.yaml")
        )
    if not folders:
        print("No template packages found under templates/")
        return 0

    failed = 0
    for folder in folders:
        issues = validate_package(folder)
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
