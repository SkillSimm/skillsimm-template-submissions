# S0 · Unit-Economics Calculator — Simulation Template

A SkillSimm workflow template that runs a **comprehensive check → role-specific questions → ranking**
pipeline as a pure, multiple-choice unit-economics task. It is engineered as the **AI-favorable control
task**: its Task-Space profile (Hu et al. 2026) — high objective correctness, high decision
verifiability, within-system solution, low creativity/generation — predicts **Fully-Automatic AI ≈
Individual+AI**, with a team adding **no measurable advantage**.

Run the same template at `team_size: 1` (Individual arm), `team_size: 4` (Team arm), and as a
fully-automatic AI arm, and compare scores. The hypothesis: **all three land at roughly the same
score**, because every question has one determinate right answer and there is no work to divide.

---

## The task

A startup has 1,000 free users, 80 paid users, a $20/month price, $6,000/month fixed cost, and $2
variable cost per **active** user (free *and* paid). Participants answer multiple-choice questions about
the figures and then rank the strategic levers for reaching break-even. Every item is fact-based.

**Answer key (fixed in `code/scoring.py`):** paid users 80 · price $20 · fixed cost $6,000 · burn
$6,560 · revenue $1,600 · total variable cost $2,160 · core issue *not enough paid conversion* ·
best ranking **increase paid conversion → reduce fixed cost → increase price → add more free users**.

---

## Stages

| Stage (file) | Stage id | Tasks (each a `select`) | Claim model | Points |
|---|---|---|---|---|
| 1 · Comprehensive check (`01_comprehensive_check.json`) | `comprehensive_check` | `comp_users`, `comp_price`, `comp_cost`, `comp_monthburn` | `parallel_per_member` — every member answers, auto-assigned | 40 (10 ea) |
| 2 · Role-specific (`02_role_questions.json`) | `role_questions` | `fin_revenue`, `fin_variable_cost` (role **finance**); `founder_problem` (role **founder**) | claimable, role-tagged | 30 (10 ea) |
| 3 · Ranking (`03_ranking.json`) | `ranking` | `strategic_ranking` (selects `rank_1..rank_4`) | single claimable | 30 |

All inputs are `select` fields — the participant chat renders each as a vertically-stacked set of option
buttons, and the claim view's stage flow chart stacks the questions within each stage.

---

## How the template maps into the simulation

The platform loads this directory through `seed.py` / `workflow_templates.py`.

| Component | File(s) | What it becomes at runtime |
|---|---|---|
| **Template manifest** | `template.json` | Registers the run: `team_size`, model config, the Task-Space profile, the three experiment arms, and the materials manifest (the HTML brief + its image). |
| **Pipeline stages** | `stages/01..03_*.json` | Each becomes one orchestrator stage; every `tasks[]` entry becomes a `select` step the participant claims/answers. |
| **AI guidance skill** | `skills/unit_economics_analyst.md` | Server-only system prompt: the fixed inputs, the free-user trap, and the right option for each question. |
| **Scoring engine** | `code/scoring.py` | The `evaluator` calls `score_total` at run end. Objective-only: each chosen option matched against the answer key. **No process block, no AI evaluator.** |
| **Validators** | `code/validators.py` | Gate each stage — presence checks (and distinct ranks for Stage 3); correctness is graded at the end. |
| **Rubric** | `evaluation/rubric.json` | Per-criterion weights, all `custom_code`. |
| **Reference decisions** | `evaluation/reference_decisions.json` | Server-only answer key (audit/reference; there are no HITL gates). |
| **Materials** | `materials/startup_financials.html` (+ `materials/img/startup_financials_summary.png`) | The fixed inputs and pinned assumptions — opens in a new tab from the Context Brief. |

---

## Why there is no process score (and why teams don't help here)

The generative templates (e.g. `user_acquisition_ideas`) award a **process block** for the three group
mechanisms — parallel divergence, collective selection, recombination. This template deliberately has
**none**, and that is the point:

- **Single answer per item.** Each question has one correct option; the ranking has one best order.
  There is no solution space to diverge across and nothing from different "lenses" to recombine.
- **Fully decomposable to zero.** Splitting the work does not help — every member would pick the same
  option. A team's only contribution is cross-checking, which a single participant with AI already does.
- **AI-reachable.** A capable AI answers every item alone, so the fully-automatic arm should match the
  human arms.

Hence the prediction **Auto AI ≈ Individual+AI ≈ Team+AI**.

---

## Scoring (100 pts, objective only)

```
total_score = score_objective(answers)   # 100
```

comprehensive check: comp_users (10) · comp_price (10) · comp_cost (10) · comp_monthburn (10) —
role questions: fin_revenue (10) · fin_variable_cost (10) · founder_problem (10) —
ranking: strategic_ranking (30; full credit for the exact order, 7.5 per lever in its correct rank,
0 for a duplicate/incomplete ranking).

---

## Running it
1. Place this directory under `backend/templates/`.
2. Recompute the `code/` hashes into `backend/trusted_modules.json` (else scoring is skipped), then
   restart the backend so `seed.py` registers `unit_economics_calculator` and copies the HTML brief +
   image.
3. Create a run from the template. **Individual arm** = `team_size: 1`; **Team arm** = `team_size: 4`;
   **Auto arm** = fully-automatic AI config. Compare total scores across arms.

## Tuning knobs
- **The numbers / options** — the option labels live in `stages/*.json` and are mirrored as the answer
  key in `code/scoring.py`; change both together.
- **Ranking partial credit** — `_score_ranking()` in `code/scoring.py`.

## Field types used by the stage forms
`select` only (multiple choice + ranking-by-position).
