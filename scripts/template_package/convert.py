"""Package ⇄ DB conversion.

`package_to_master` turns a parsed package into the master-dict shape the
seeder upserts (steps already in engine `steps_json` form — note that
`seed._load_folder_template` builds steps from stages/*.json and ignores a
master "steps" key, so packages carry engine-ready steps explicitly).

`template_to_package` serializes a Template row into package files for the
submission PR. Each engine step keeps its original package step under a
`package` key, so MCP-created templates round-trip losslessly.
"""
from __future__ import annotations

import json
from typing import Any, Optional

import yaml

from .schema import GradingRule, StepSpec, TemplatePackage

_HITL_MODES = ("human", "human_with_ai", "team_with_ai")


def _engine_step(pkg: TemplatePackage, step: StepSpec, index: int) -> dict:
    """Map a package step onto the engine steps_json spec (see seed.py)."""
    rule = pkg.grading_for(step)
    is_hitl = step.actor_mode in _HITL_MODES
    return {
        "task_id": step.id,
        "name": step.title,
        "description": step.task_description,
        "step_type": "hitl" if is_hitl else "auto",
        "step_index": index,
        "stage_id": step.id,
        "stage_index": index,
        "stage_dependencies": list(step.depends_on),
        "role": step.role,
        "hitl_prompt": step.task_description if is_hitl else None,
        "hitl_options": list(rule.options) if (rule and rule.options) else None,
        "llm_instructions": None if is_hitl else step.task_description,
        "requires_ai_review": False,
        "review_type": "none",
        "evaluation_point": bool(rule and rule.type != "none"),
        "evaluation_weight": rule.points if rule else 0,
        # Lossless round-trip payload (package-native step definition).
        "package": {
            **step.model_dump(exclude_none=True, exclude={"grading"}),
            **({"grading": rule.model_dump(exclude_none=True)} if rule else {}),
        },
    }


def package_to_master(pkg: TemplatePackage) -> dict:
    """Master dict for the seeder/sync upsert path."""
    steps_json = [_engine_step(pkg, s, i) for i, s in enumerate(pkg.steps)]

    rubric: dict[str, Any] = {}
    reference: dict[str, Any] = {}
    for s in pkg.steps:
        rule = pkg.grading_for(s)
        if not rule or rule.type == "none":
            continue
        if rule.type in ("rubric", "llm_judge"):
            rubric[s.id] = {
                "criteria": rule.criteria or [],
                "points": rule.points,
                "type": rule.type,
                **({"anchor_examples": rule.anchor_examples} if rule.anchor_examples else {}),
            }
        elif rule.type == "answer_key":
            reference[s.id] = {"correct_answer": rule.correct_answer, "points": rule.points}
        elif rule.type == "numeric":
            reference[s.id] = {
                k: v
                for k, v in (
                    ("expected_value", rule.expected_value),
                    ("expected_range", rule.expected_range),
                    ("tolerance", rule.tolerance),
                    ("formula", rule.formula),
                    ("points", rule.points),
                )
                if v is not None
            }

    meta = pkg.metadata.model_dump(exclude_none=True) if pkg.metadata else {}
    if pkg.creator and pkg.creator.name and not meta.get("author"):
        meta["author"] = pkg.creator.name
    ts = meta.pop("team_size", None)
    if ts:
        meta["team_size"] = ts  # keep {min,max} shape _registry_fields_from_master reads

    return {
        "template_id": pkg.template.id,
        "name": pkg.template.title,
        "version": pkg.template.version,
        "team_size": pkg.template.team_size,
        "ai_chat_enabled": pkg.template.ai_chat_enabled,
        "group_communication_allowed": pkg.template.group_communication_allowed,
        "metadata": meta,
        "steps_json": steps_json,
        "evaluation_criteria": {"rubric": rubric} if rubric else {},
        "reference_decisions": reference,
        "objective": pkg.template.objective,
        "audience": pkg.template.audience,
        "roles": pkg.template.roles,
    }


# ── Template row → package files ─────────────────────────────────────────────

def _yaml(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False)


def _package_step_from_engine(spec: dict) -> dict:
    """Recover a package step from an engine steps_json entry — lossless when
    the `package` key is present, best-effort otherwise."""
    if isinstance(spec.get("package"), dict):
        return dict(spec["package"])
    is_hitl = spec.get("step_type") == "hitl"
    step: dict = {
        "id": spec.get("task_id") or f"step_{spec.get('step_index', 0)}",
        "title": spec.get("name") or "Untitled step",
        "actor_mode": "human_with_ai" if is_hitl else "ai",
        "task_type": "multiple_choice" if spec.get("hitl_options") else (
            "structured_response" if is_hitl else "open_response"
        ),
        "task_description": spec.get("description")
        or spec.get("hitl_prompt")
        or spec.get("llm_instructions")
        or "",
    }
    if spec.get("role"):
        step["role"] = spec["role"]
    if spec.get("stage_dependencies"):
        step["depends_on"] = list(spec["stage_dependencies"])
    if spec.get("hitl_options"):
        step["grading"] = {
            "type": "answer_key",
            "options": list(spec["hitl_options"]),
            "points": spec.get("evaluation_weight") or 1,
        }
    return step


def template_to_package(template: Any, creator: Optional[dict] = None) -> dict[str, str]:
    """Serialize a Template ORM row (duck-typed) into {relative_path: content}.

    Grading/answer keys are included only for creator-authored templates
    (source == "user"): for curated/forked templates the reference decisions
    are SkillSimm server-only IP and must never leave the DB (same redaction
    rule as main._template_detail).
    """
    include_answers = (getattr(template, "source", None) or "local") == "user"
    steps_json = getattr(template, "steps_json", None) or []

    steps: list[dict] = []
    grading: dict[str, dict] = {}
    for spec in steps_json:
        step = _package_step_from_engine(spec)
        rule = step.pop("grading", None)
        if rule and not include_answers:
            rule = {"type": rule.get("type", "none"), "points": rule.get("points", 1)}
        if rule:
            grading[step["id"]] = rule
        steps.append(step)

    roles = sorted({s["role"] for s in steps if s.get("role")})
    template_yaml = {
        "id": template.template_id,
        "title": template.name,
        "objective": (getattr(template, "learning_goals", None) or [""])[0]
        or f"Train judgment for {template.name}",
        "audience": getattr(template, "audience", None) or getattr(template, "industry", None),
        "roles": roles,
        "version": template.version or "1.0.0",
        "team_size": template.team_size or 5,
        "ai_chat_enabled": bool(template.ai_chat_enabled),
        "group_communication_allowed": bool(template.group_communication_allowed),
    }
    template_yaml = {k: v for k, v in template_yaml.items() if v is not None}

    metadata = {
        k: v
        for k, v in {
            "domain": getattr(template, "domain", None),
            "industry": getattr(template, "industry", None),
            "difficulty": getattr(template, "difficulty", None),
            "duration_minutes": getattr(template, "duration_minutes", None),
            "team_size": {
                "min": getattr(template, "team_size_min", None),
                "max": getattr(template, "team_size_max", None),
            },
            "task_type": getattr(template, "task_type", None),
            "scoring_type": getattr(template, "scoring_type", None),
            "license": getattr(template, "license", None),
            "author": getattr(template, "author", None),
            "ai_modes": getattr(template, "ai_modes", None) or [],
            "tags": getattr(template, "tags", None) or [],
            "learning_goals": getattr(template, "learning_goals", None) or [],
        }.items()
        if v not in (None, [], {"min": None, "max": None})
    }

    readme = _render_readme(template_yaml, steps)
    license_text = (
        f"# License\n\n{getattr(template, 'license', None) or 'CC-BY-4.0'}\n\n"
        "Submitted to the SkillSimm template registry. SkillSimm may modify, "
        "delist, or version this template for safety and quality.\n"
    )

    files: dict[str, str] = {
        "template.yaml": _yaml(template_yaml),
        "steps.yaml": _yaml({"steps": steps}),
        "metadata.yaml": _yaml(metadata),
        "README.md": readme,
        "LICENSE.md": license_text,
    }
    if grading:
        files["grading.yaml"] = _yaml(grading)
    if creator:
        files["creator.yaml"] = _yaml(creator)
    sample = getattr(template, "attachments_json", None)
    if sample:
        files["sample_inputs.json"] = json.dumps(sample, indent=2)
    return files


def _render_readme(template_yaml: dict, steps: list[dict]) -> str:
    lines = [
        f"# {template_yaml['title']}",
        "",
        template_yaml.get("objective", ""),
        "",
        f"- **Audience:** {template_yaml.get('audience') or 'general'}",
        f"- **Team size:** {template_yaml.get('team_size', 5)}",
        f"- **Roles:** {', '.join(template_yaml.get('roles') or []) or '—'}",
        "",
        "## Steps",
        "",
    ]
    for i, s in enumerate(steps, 1):
        lines.append(
            f"{i}. **{s['title']}** (`{s['id']}`) — {s['actor_mode']}, {s['task_type']}"
        )
        if s.get("task_description"):
            lines.append(f"   {s['task_description']}")
    lines += [
        "",
        "---",
        "Submitted via the SkillSimm Template MCP. Review happens in this pull "
        "request; merge publishes the template to the registry.",
        "",
    ]
    return "\n".join(lines)
