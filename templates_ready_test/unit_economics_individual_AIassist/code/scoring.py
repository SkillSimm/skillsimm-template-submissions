"""
Custom scoring for the S0 Unit-Economics Calculator (multiple-choice redesign).

One block, 100 points total — OBJECTIVE ONLY. There is deliberately NO process
score and NO AI evaluator: every item is a multiple-choice question (or a
ranking) with a single determinate right answer, so the group mechanisms
(divergence, collective selection, recombination) have nothing to bite on. That
absence is the experimental point — Auto AI ≈ Individual+AI, and a team earns no
extra credit for coordinating on facts that have one right answer.

Runs SERVER-SIDE ONLY. Each chosen option is matched against the fixed answer
key mirrored from the stage JSON.

Point allocation (100):
  Stage 1 · Comprehensive check  — 4 × 10 = 40
  Stage 2 · Role-specific        — 3 × 10 = 30
  Stage 3 · Ranking              —          30
"""

# ---- Fixed inputs (mirror materials/startup_financials.html) ----------------
FREE_USERS = 1000
PAID_USERS = 80
PRICE = 20.0
FIXED_COST = 6000.0
VAR_COST_PER_USER = 2.0

# ---- Answer key: correct option label per variable (mirror stages/*.json) ----
ANSWER_KEY = {
    # Stage 1 — comprehensive check
    "comp_users": "80",
    "comp_price": "$20",
    "comp_cost": "$6,000",
    "comp_monthburn": "$6,560",
    # Stage 2 — role-specific
    "fin_revenue": "$1,600",
    "fin_variable_cost": "$2,160",
    "founder_problem": "Not enough paid conversion",
}

# Stage 3 — expected best ranking, best lever first.
RANKING_KEY = [
    "Increase paid conversion",
    "Reduce fixed cost",
    "Increase price",
    "Add more free users",
]
RANK_FIELDS = ["rank_1", "rank_2", "rank_3", "rank_4"]


# ============================================================================
# OBJECTIVE SCORE — 100 points
# ============================================================================
def score_objective(answers: dict) -> dict:
    """
    answers: flat dict merged across stages
        { comp_users, comp_price, comp_cost, comp_monthburn,
          fin_revenue, fin_variable_cost, founder_problem,
          rank_1, rank_2, rank_3, rank_4 }
    Returns a breakdown dict summing to <= 100.
    """
    b = {}

    # Stage 1 — comprehensive check (40 pts, 10 each)
    b["comp_users_correct"] = 10 if _match(answers.get("comp_users"), ANSWER_KEY["comp_users"]) else 0
    b["comp_price_correct"] = 10 if _match(answers.get("comp_price"), ANSWER_KEY["comp_price"]) else 0
    b["comp_cost_correct"] = 10 if _match(answers.get("comp_cost"), ANSWER_KEY["comp_cost"]) else 0
    b["comp_monthburn_correct"] = 10 if _match(answers.get("comp_monthburn"), ANSWER_KEY["comp_monthburn"]) else 0

    # Stage 2 — role-specific (30 pts, 10 each)
    b["fin_revenue_correct"] = 10 if _match(answers.get("fin_revenue"), ANSWER_KEY["fin_revenue"]) else 0
    b["fin_variable_cost_correct"] = 10 if _match(answers.get("fin_variable_cost"), ANSWER_KEY["fin_variable_cost"]) else 0
    b["founder_problem_correct"] = 10 if _match(answers.get("founder_problem"), ANSWER_KEY["founder_problem"]) else 0

    # Stage 3 — ranking (30 pts)
    b["strategic_ranking_score"] = _score_ranking(answers)

    b["objective_total"] = sum(v for k, v in b.items() if k != "objective_total")
    return b


# ============================================================================
# TOTAL  (no process block by design)
# ============================================================================
def score_total(final_plan: dict, stage_outputs: dict = None, ai_flags: dict = None) -> dict:
    answers = _flatten(final_plan, stage_outputs)
    obj = score_objective(answers)
    return {
        "objective": obj,
        "process": {
            "process_total": 0,
            "note": "No process block — every item is a single-answer multiple-choice / ranking; teams earn no mechanism credit.",
        },
        "total_score": round(obj["objective_total"], 1),
    }


# ---- ranking ----------------------------------------------------------------
def _score_ranking(answers: dict) -> float:
    """30 pts. Full credit for the exact order; partial credit for each lever
    placed in its correct rank. Zero if a lever is repeated or anything is
    missing (an invalid ranking)."""
    picks = [_norm(answers.get(f)) for f in RANK_FIELDS]
    if any(p == "" for p in picks):
        return 0.0
    if len(set(picks)) != 4:  # duplicate lever -> invalid ranking
        return 0.0
    key = [_norm(x) for x in RANKING_KEY]
    if picks == key:
        return 30.0
    correct_positions = sum(1 for p, k in zip(picks, key) if p == k)
    return round(correct_positions * 7.5, 1)  # 0 / 7.5 / 15 / 22.5 (exact handled above)


# ---- helpers ----------------------------------------------------------------
def _flatten(final_plan: dict, stage_outputs: dict) -> dict:
    """Merge every stage submission dict (and final_plan) into one flat answers
    map. The runtime passes stage_outputs keyed by stage_id; we don't depend on
    the stage names — we just union the leaf dicts."""
    merged = {}
    for source in (stage_outputs or {}, {"_final": final_plan or {}}):
        for value in source.values():
            if isinstance(value, dict):
                for k, v in value.items():
                    if v is not None and v != "":
                        merged[k] = v
    # final_plan may itself be a flat dict of fields
    if isinstance(final_plan, dict):
        for k, v in final_plan.items():
            if not isinstance(v, dict) and v is not None and v != "":
                merged[k] = v
    return merged


def _match(value, target) -> bool:
    return value is not None and _norm(value) == _norm(target)


def _norm(x) -> str:
    """Normalize an option string for tolerant comparison: trim, lowercase, and
    drop currency/grouping punctuation so '$6,560' == '$ 6560' == '6,560'."""
    if x is None:
        return ""
    s = str(x).strip().lower()
    for ch in ("$", ",", " "):
        s = s.replace(ch, "")
    return s
