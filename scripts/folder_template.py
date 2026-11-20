"""Validator for app-format templates (template.json + stages/*.json).

This is the format the SkillSimm app seeds directly and the format of the
starters in examples/. It is repo-local (stdlib only) and NOT part of the
vendored `template_package/` module, which validates the YAML lite format.

Checks mirror what the app's seeder reads (backend app/seed.py,
`_load_folder_template`): the master file, every stage file, seat numbers,
form fields, AI answers, and the files the template points at.

    python scripts/folder_template.py examples/team-decision-starter
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_MASTER = ("template_id", "name", "team_size")
OPTION_TYPES = {"select", "multi_select"}
KNOWN_FIELD_TYPES = {"select", "multi_select", "text", "string", "number", "textarea",
                     "likert", "file_select", "doc_confirm", "folder_confirm"}
TASK_TYPES = {"human", "human_with_ai", "hitl_decision", "auto"}


@dataclass
class Issue:
    severity: str  # "error" | "warning"
    file: str
    message: str

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}: {self.message}"


def _read_json(path: Path, rel: str, issues: list[Issue]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        issues.append(Issue("error", rel, "file not found"))
    except json.JSONDecodeError as e:
        issues.append(Issue("error", rel, f"not valid JSON (line {e.lineno}, column {e.colno}: {e.msg})"
                                          " — check for a missing comma, quote or bracket"))
    return None


def _slots_ok(values, team_size: int) -> bool:
    return all(isinstance(v, int) and 1 <= v <= team_size for v in values)


def validate_folder(folder: Path) -> list[Issue]:
    folder = Path(folder)
    issues: list[Issue] = []
    err = lambda f, m: issues.append(Issue("error", f, m))  # noqa: E731
    warn = lambda f, m: issues.append(Issue("warning", f, m))  # noqa: E731

    master = _read_json(folder / "template.json", "template.json", issues)
    if not isinstance(master, dict):
        if master is not None:
            err("template.json", "must be a JSON object { ... }")
        return issues

    T = "template.json"
    for key in REQUIRED_MASTER:
        if key not in master or master[key] in ("", None):
            err(T, f"missing required key '{key}'")
    if not master.get("version"):
        warn(T, "no 'version' — the app will use 1.0.0; bump it (e.g. 1.0.1) each time you change the template")
    team_size = master.get("team_size")
    if not isinstance(team_size, int) or team_size < 1:
        err(T, "'team_size' must be a whole number of seats, 1 or more")
        team_size = 0
    if not (folder / "README.md").exists():
        warn("README.md", "add a README.md describing the simulation for reviewers")

    def file_ref(rel_path: str, where: str, missing_is_error: bool = True):
        if not isinstance(rel_path, str) or not rel_path:
            return
        if not (folder / rel_path).exists():
            (err if missing_is_error else warn)(where, f"points at '{rel_path}', which is not in the folder")

    # ── seats ────────────────────────────────────────────────────────────────
    if team_size:
        for i, lens in enumerate(master.get("lens_assignments") or []):
            if not _slots_ok([lens.get("member_slot")], team_size):
                err(T, f"lens_assignments[{i}].member_slot must be between 1 and team_size ({team_size})")
        staffing = master.get("staffing") or {}
        sizes = staffing.get("allowed_sizes") or []
        if sizes and not _slots_ok(sizes, team_size):
            err(T, f"staffing.allowed_sizes must be between 1 and team_size ({team_size})")
        order = staffing.get("human_seat_order") or []
        if order and sorted(order) != list(range(1, len(order) + 1)):
            err(T, "staffing.human_seat_order must list each seat number once (e.g. [5, 1, 2, 3, 4])")
        elif order and len(order) != team_size:
            err(T, f"staffing.human_seat_order lists {len(order)} seats but team_size is {team_size}")

    # ── materials ────────────────────────────────────────────────────────────
    for i, mat in enumerate(master.get("materials") or []):
        where = f"{T} materials[{i}] ('{mat.get('name', '?')}')"
        if not mat.get("name"):
            err(T, f"materials[{i}] needs a 'name'")
        file_ref(mat.get("path"), where)
        slots = (mat.get("audience") or {}).get("slots")
        if slots is not None and team_size and not _slots_ok(slots, team_size):
            err(where, f"audience.slots must be seat numbers between 1 and {team_size}")

    # ── other referenced files ───────────────────────────────────────────────
    file_ref(master.get("evaluation_config"), f"{T} evaluation_config", missing_is_error=False)
    file_ref(master.get("reference_decisions"), f"{T} reference_decisions", missing_is_error=False)
    for key in ("evaluation_config", "reference_decisions"):
        p = master.get(key)
        if isinstance(p, str) and p.endswith(".json") and (folder / p).exists():
            _read_json(folder / p, p, issues)
    if master.get("code_module"):
        file_ref(str(master["code_module"]).replace(".", "/"), f"{T} code_module", missing_is_error=False)

    # ── stages ───────────────────────────────────────────────────────────────
    stages_dir = folder / (master.get("stages_dir") or "stages/").rstrip("/")
    stage_files = sorted(stages_dir.glob("*.json")) if stages_dir.is_dir() else []
    if not stage_files:
        err("stages/", "no stage files — add at least one stages/NN_name.json")
    stages: list[tuple[str, dict]] = []
    for sf in stage_files:
        rel = f"stages/{sf.name}"
        data = _read_json(sf, rel, issues)
        if isinstance(data, dict):
            stages.append((rel, data))
        elif data is not None:
            err(rel, "must be a JSON object { ... }")

    stage_ids: dict[str, str] = {}
    task_ids: dict[str, str] = {}
    has_answer_keys = False
    for rel, st in stages:
        sid = st.get("stage_id")
        if not sid:
            err(rel, "missing 'stage_id'")
        elif sid in stage_ids:
            err(rel, f"stage_id '{sid}' is already used in {stage_ids[sid]}")
        else:
            stage_ids[sid] = rel
        tasks = st.get("tasks")
        if not isinstance(tasks, list) or not tasks:
            err(rel, "needs a non-empty 'tasks' list")
            continue
        for ti, t in enumerate(tasks):
            tid = t.get("task_id")
            where = f"{rel} task '{tid or ti}'"
            if not tid:
                err(rel, f"tasks[{ti}] is missing 'task_id'")
            elif tid in task_ids:
                err(where, f"task_id is already used in {task_ids[tid]}")
            else:
                task_ids[tid] = rel
            if t.get("type", "auto") not in TASK_TYPES:
                err(where, f"type '{t.get('type')}' is not one of {sorted(TASK_TYPES)}")
            slot = t.get("participant_slot")
            if slot is not None and team_size and not _slots_ok([slot], team_size):
                err(where, f"participant_slot {slot} is outside seats 1–{team_size}")
            schema = t.get("field_schema") or {}
            if not isinstance(schema, dict):
                err(where, "field_schema must be an object of fields")
                schema = {}
            for fname, spec in schema.items():
                ftype = (spec or {}).get("type", "text")
                if ftype not in KNOWN_FIELD_TYPES:
                    warn(where, f"field '{fname}' has type '{ftype}', which the app may not render "
                                f"(known: {', '.join(sorted(KNOWN_FIELD_TYPES))})")
                if ftype in OPTION_TYPES and not (spec.get("options") or []):
                    err(where, f"field '{fname}' is a {ftype} but has no options")
            for rf in t.get("required_fields") or []:
                if rf not in schema:
                    err(where, f"required field '{rf}' is not defined in field_schema")
            skill = t.get("ai_guidance_skill")
            if skill:
                file_ref(skill, f"{where} ai_guidance_skill")
            ai = t.get("ai_answer")
            if ai:
                has_answer_keys = True
                options = [o for spec in schema.values() if isinstance(spec, dict)
                           for o in (spec.get("options") or [])]
                for k in ("correct", "wrong"):
                    v = ai.get(k)
                    if v is not None and v not in options:
                        err(where, f"ai_answer.{k} must match one of the field's options word for word")

    for rel, st in stages:
        sid = st.get("stage_id")
        for dep in st.get("dependencies") or []:
            if dep == sid:
                err(rel, f"stage '{sid}' depends on itself")
            elif dep not in stage_ids:
                err(rel, f"depends on unknown stage '{dep}' (known: {', '.join(stage_ids) or 'none'})")

    # ── AI mediation targets ─────────────────────────────────────────────────
    med = master.get("ai_mediation") or {}
    for qid, q in (med.get("questions") or {}).items():
        if qid not in task_ids:
            err(T, f"ai_mediation.questions has '{qid}', which is not a task_id in any stage")
        if team_size and not _slots_ok(q.get("target_slots") or [], team_size):
            err(T, f"ai_mediation.questions.{qid}.target_slots must be seats 1–{team_size}")

    # ── public-repo guard ────────────────────────────────────────────────────
    if (folder / "evaluation" / "reference_decisions.json").exists() or (folder / "code" / "scoring.py").exists():
        warn("evaluation/", "answer keys or scoring code are in this folder. This repository is public — "
                            "anyone can read them. Leave placeholders and send keys privately to your reviewer.")
    if has_answer_keys:
        warn("stages/", "ai_answer values are visible to anyone reading this public repository. "
                        "Use placeholders if the right answer must stay secret.")
    return issues


def main(argv: list[str]) -> int:
    failed = 0
    for a in argv:
        issues = validate_folder(Path(a))
        errors = [i for i in issues if i.severity == "error"]
        print(f"\n{'FAIL' if errors else 'PASS'}  {a}")
        for i in errors + [i for i in issues if i.severity != "error"]:
            print(f"  {i}")
        failed += bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
