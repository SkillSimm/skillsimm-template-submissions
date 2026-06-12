"""Package loader + validator (TemplateMCP spec §4 + §6).

`validate_package(folder)` returns a list of Issues; an empty list (or
warnings only) means the package may be submitted. The same function runs in
three places: the MCP server's `validate_template` tool, the backend's
submission endpoint, and the submissions repo's GitHub Actions check.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml
from pydantic import ValidationError

from .schema import GradingRule, StepSpec, TemplatePackage

REQUIRED_FILES = ("template.yaml", "steps.yaml", "README.md", "LICENSE.md")
MIN_README_CHARS = 200

# Coarse pre-screen only — the real safety review happens in the PR. Matches
# whole words, lowercased.
UNSAFE_KEYWORDS = {
    "bioweapon", "child sexual", "csam", "ethnic cleansing", "credit card dump",
    "make a bomb", "mass shooting", "ransomware payload", "suicide method",
}


@dataclass
class Issue:
    severity: str  # "error" | "warning"
    file: str
    message: str

    def __str__(self) -> str:  # readable in CI logs and tool results
        return f"[{self.severity}] {self.file}: {self.message}"


def _err(file: str, message: str) -> Issue:
    return Issue("error", file, message)


def _warn(file: str, message: str) -> Issue:
    return Issue("warning", file, message)


def _read_yaml(path: Path, issues: list[Issue]):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        issues.append(_err(path.name, f"invalid YAML: {e}"))
        return None


def _read_json(path: Path, issues: list[Issue]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        issues.append(_err(path.name, f"invalid JSON: {e}"))
        return None


def _pydantic_issues(file: str, exc: ValidationError) -> list[Issue]:
    return [
        _err(file, f"{'.'.join(str(p) for p in e['loc'])}: {e['msg']}")
        for e in exc.errors()
    ]


def load_package(folder: Path) -> tuple[Optional[TemplatePackage], list[Issue]]:
    """Parse a package folder. Returns (package, issues); package is None when
    structural errors prevent parsing at all."""
    folder = Path(folder)
    issues: list[Issue] = []

    for name in REQUIRED_FILES:
        if not (folder / name).exists():
            issues.append(_err(name, "required file is missing"))
    if any(i.severity == "error" for i in issues):
        return None, issues

    template_raw = _read_yaml(folder / "template.yaml", issues)
    steps_raw = _read_yaml(folder / "steps.yaml", issues)
    if template_raw is None or steps_raw is None:
        return None, issues

    # steps.yaml may be a bare list or {steps: [...]}
    if isinstance(steps_raw, dict) and "steps" in steps_raw:
        steps_raw = steps_raw["steps"]
    if not isinstance(steps_raw, list):
        issues.append(_err("steps.yaml", "expected a list of steps (or {steps: [...]})"))
        return None, issues

    data: dict = {"template": template_raw, "steps": steps_raw}

    grading_path = folder / "grading.yaml"
    if grading_path.exists():
        grading_raw = _read_yaml(grading_path, issues)
        if isinstance(grading_raw, dict):
            data["grading"] = grading_raw
        elif grading_raw is not None:
            issues.append(_err("grading.yaml", "expected a mapping of step id → grading rule"))

    for fname, key in (("metadata.yaml", "metadata"), ("creator.yaml", "creator")):
        p = folder / fname
        if p.exists():
            raw = _read_yaml(p, issues)
            if raw is not None:
                data[key] = raw

    for fname, key in (
        ("sample_inputs.json", "sample_inputs"),
        ("expected_outputs.json", "expected_outputs"),
    ):
        p = folder / fname
        if p.exists():
            raw = _read_json(p, issues)
            if raw is not None:
                data[key] = raw

    data["readme"] = (folder / "README.md").read_text(encoding="utf-8")
    data["license_text"] = (folder / "LICENSE.md").read_text(encoding="utf-8")

    try:
        pkg = TemplatePackage(**data)
    except ValidationError as e:
        issues.extend(_pydantic_issues("(package)", e))
        return None, issues
    return pkg, issues


# ── Grading decision tree (spec §4) ──────────────────────────────────────────

def _check_grading(step: StepSpec, rule: Optional[GradingRule]) -> list[Issue]:
    f = "steps.yaml"
    sid = step.id
    issues: list[Issue] = []

    if rule is None:
        issues.append(_warn(f, f"step '{sid}' has no grading rule (ungraded)"))
        return issues
    if rule.type == "none":
        return issues

    if step.task_type == "multiple_choice":
        if rule.type != "answer_key":
            issues.append(_err(f, f"step '{sid}': multiple_choice requires grading type answer_key"))
        if not rule.options or len(rule.options) < 2:
            issues.append(_err(f, f"step '{sid}': multiple_choice needs at least 2 options"))
        if not rule.correct_answer:
            issues.append(_err(f, f"step '{sid}': multiple_choice needs correct_answer"))
        elif rule.options and rule.correct_answer not in rule.options:
            issues.append(_err(f, f"step '{sid}': correct_answer {rule.correct_answer!r} is not among options"))
    elif step.task_type == "numeric_input":
        if rule.type != "numeric":
            issues.append(_err(f, f"step '{sid}': numeric_input requires grading type numeric"))
        has_target = (
            rule.expected_value is not None
            or rule.expected_range is not None
            or rule.formula
        )
        if not has_target:
            issues.append(_err(f, f"step '{sid}': numeric grading needs expected_value, expected_range, or formula"))
        if rule.expected_value is not None and rule.tolerance is None:
            issues.append(_warn(f, f"step '{sid}': expected_value without tolerance grades on exact match"))
    else:  # structured_response / open_response / document_review
        if rule.type not in ("rubric", "llm_judge"):
            issues.append(_err(f, f"step '{sid}': {step.task_type} requires rubric or llm_judge grading"))
        if not rule.criteria:
            issues.append(_err(f, f"step '{sid}': {rule.type} grading needs rubric criteria"))
        if rule.type == "llm_judge" and not rule.anchor_examples:
            issues.append(_err(f, f"step '{sid}': llm_judge grading needs anchor_examples"))

    if rule.points <= 0:
        issues.append(_err(f, f"step '{sid}': points must be > 0"))
    return issues


def validate_package(folder: Path) -> list[Issue]:
    """Full validation: structure, schemas, step graph, grading rules,
    documentation, and a coarse unsafe-content scan."""
    pkg, issues = load_package(folder)
    if pkg is None:
        return issues

    # Step ids unique
    seen: set[str] = set()
    for s in pkg.steps:
        if s.id in seen:
            issues.append(_err("steps.yaml", f"duplicate step id '{s.id}'"))
        seen.add(s.id)
    if not pkg.steps:
        issues.append(_err("steps.yaml", "package has no steps"))

    # Broken references
    for s in pkg.steps:
        for dep in s.depends_on:
            if dep == s.id:
                issues.append(_err("steps.yaml", f"step '{s.id}' depends on itself"))
            elif dep not in seen:
                issues.append(_err("steps.yaml", f"step '{s.id}' depends on unknown step '{dep}'"))
        if s.role and pkg.template.roles and s.role not in pkg.template.roles:
            issues.append(_err("steps.yaml", f"step '{s.id}' uses role '{s.role}' not declared in template.yaml roles"))
    for sid in pkg.grading:
        if sid not in seen:
            issues.append(_err("grading.yaml", f"grading rule for unknown step '{sid}'"))

    # Grading decision tree + human/AI mode fit
    for s in pkg.steps:
        issues.extend(_check_grading(s, pkg.grading_for(s)))
        if s.actor_mode in ("human_with_ai", "team_with_ai") and not s.ai_assist:
            issues.append(_warn(
                "steps.yaml",
                f"step '{s.id}' is {s.actor_mode} but ai_assist is unset "
                "(suggests | critiques | grades | decides)",
            ))

    # Minimum documentation
    if len((pkg.readme or "").strip()) < MIN_README_CHARS:
        issues.append(_err("README.md", f"README must be at least {MIN_README_CHARS} characters"))
    if not pkg.template.objective.strip():
        issues.append(_err("template.yaml", "objective must not be empty"))
    if not (pkg.license_text or "").strip():
        issues.append(_err("LICENSE.md", "LICENSE.md must not be empty"))

    # Coarse unsafe-content scan over all text content
    hay = " ".join([
        pkg.readme or "",
        pkg.template.title,
        pkg.template.objective,
        *(s.task_description for s in pkg.steps),
    ]).lower()
    for kw in sorted(UNSAFE_KEYWORDS):
        if kw in hay:
            issues.append(_err("(package)", f"unsafe content keyword detected: {kw!r} — flagged for review"))

    return issues
