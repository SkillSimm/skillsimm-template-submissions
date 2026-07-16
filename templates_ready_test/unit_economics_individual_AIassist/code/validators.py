"""
Custom validators for the S0 Unit-Economics Calculator (multiple-choice redesign).

Each validator gates a stage before it can advance. Signature:
    fn(stage_output, prior_stages) -> {"valid": bool, "errors": [...], "warnings": [...]}

These are structural / presence checks only — that an option was actually picked
(and, for the ranking, that the four levers are distinct). Whether the chosen
option is *correct* is graded by code.scoring at run end.
"""

COMP_FIELDS = [
    ("comp_users", "paid-user count"),
    ("comp_price", "monthly price"),
    ("comp_cost", "monthly fixed cost"),
    ("comp_monthburn", "monthly burn"),
]

ROLE_FIELDS = [
    ("fin_revenue", "monthly revenue"),
    ("fin_variable_cost", "total variable cost"),
    ("founder_problem", "core business issue"),
]

RANK_FIELDS = ["rank_1", "rank_2", "rank_3", "rank_4"]


def validate_comprehensive(stage_output, prior_stages):
    """Stage 1: a comprehensive-check question is answered when its option is picked."""
    errors, warnings = [], []
    for key, label in COMP_FIELDS:
        if not _picked(stage_output.get(key)):
            warnings.append(f"Pick an answer for {label}.")
    return _result(errors, warnings)


def validate_role_questions(stage_output, prior_stages):
    """Stage 2: a role question is answered when its option is picked."""
    errors, warnings = [], []
    for key, label in ROLE_FIELDS:
        if not _picked(stage_output.get(key)):
            warnings.append(f"Pick an answer for {label}.")
    return _result(errors, warnings)


def validate_ranking(stage_output, prior_stages):
    """Stage 3: all four ranks chosen and distinct (no lever used twice)."""
    errors, warnings = [], []
    picks = [(_text(stage_output.get(f))) for f in RANK_FIELDS]
    if any(not p for p in picks):
        errors.append("Choose a lever for all four ranks.")
    elif len(set(picks)) != 4:
        errors.append("Each lever must be ranked once — remove the duplicate.")
    return _result(errors, warnings)


# ---- helpers ----------------------------------------------------------------
def _picked(value) -> bool:
    return _text(value) != ""


def _text(value) -> str:
    return "" if value is None else str(value).strip()


def _result(errors, warnings):
    return {"valid": len(errors) == 0, "errors": errors, "warnings": warnings}
