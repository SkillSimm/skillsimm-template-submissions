# Team decision starter (based on *Shake Shack FY2014 · Executive Team + AI*)

A five-seat executive team makes connected decisions about one company. Each
executive holds private facts the others need, an AI coach helps without giving
answers, and the CEO ranks the team's priorities at the end.

This is a trimmed copy of SkillSimm's `Shak_team_AIassist` template. The seats,
stages, AI settings and staffing are the real ones. The answer keys, scoring
code, instructor debrief and private briefings were removed because this
repository is public. Stage 1 questions are placeholders for the same reason.

## What this template shows

| Feature | Where it lives |
|---|---|
| 5 seats with titles and goals (CFO, CMO, COO, CTO, CEO) | `template.json` → `lens_assignments`; each task's `participant_slot` and `role` |
| Private materials only one seat can open | `template.json` → `materials[].audience.slots` |
| Shared materials everyone sees | `materials[]` entries with no `audience` |
| Questions that need two colleagues' facts | `stages/01_comprehension.json` (placeholders) |
| One decision per executive, multiple choice | `stages/02_functional_decisions.json`, `field_schema` type `select` |
| CEO ranking plus a written reason | `stages/03_priority_ranking.json`, four `select` fields and one `textarea` |
| Stages that run in order | each stage's `dependencies` |
| AI coach that teaches a method, never answers | `ai_chat_policy: "coach"`, `skills/executive_coach.md`, `chat_context_override` |
| AI suggestion on a question card, sometimes right, sometimes wrong | task `ai_answer` + `template.json` → `ai_answer_randomization` |
| AI offers to ask a colleague for you | `template.json` → `ai_mediation` |
| 1–5 people per team; empty seats' work goes to the CEO | `template.json` → `staffing` (`allowed_sizes`, `human_seat_order`, `vacant_functions: "pool"`) |
| CEO may take over a stuck task; facilitator alert after 20 min | `coordination.routing.takeover`, `coordination.escalation` |
| Nudge when someone is idle | `coordination.nudges` |
| Unscored survey at the end | `stages/99_post_survey.json` (`stage_kind: "survey_post"`, `likert` + `textarea`) |
| Scoring weights | task `evaluation_point` / `evaluation_weight`, `evaluation/rubric.json` |

## Make it yours — in this order

1. **Name it.** `template.json`: `name`, `metadata` (`domain`, `industry`,
   `difficulty`, `duration_minutes`, `tags`, `learning_goals`, `author`).
   Leave `template_id` as the folder name with `_` instead of `-`.
2. **Seats.** Keep five seats or change `team_size`. For every seat, update its
   `lens_assignments` entry and the tasks that use its `participant_slot`. If you
   remove a seat, also fix `staffing.allowed_sizes`, `staffing.human_seat_order`,
   `coordination.contacts.rules`, `materials[].audience.slots`,
   `ai_mediation.questions[].target_slots` and the survey tasks.
3. **Materials.** Replace each `materials/*.md` file. Markdown works; for PDFs,
   upload the file and change `path` and `mime` (`application/pdf`).
4. **Questions.** Edit `hitl_prompt`, the field `label` (usually the same text)
   and `options` in each stage file. Write Stage 1 so each answer needs facts
   from two colleagues' private briefings.
5. **AI.** Rewrite `skills/executive_coach.md` for your case. To turn off AI
   suggestions on cards, delete the `ai_answer` blocks or set
   `ai_answer_randomization.enabled` to `false`. To turn off AI chat, set
   `ai_chat_enabled` to `false`.
6. **Grading.** Describe what good answers look like in `evaluation/rubric.json`.
   Don't commit real answer keys: this repository is public. Send them to your
   reviewer privately; `evaluation/reference_decisions.example.json` shows the
   shape they'll take.
7. **Check.** Open a pull request; the `validate` check lists anything to fix.

The original Shak case teaches the "Standardization–Autonomy Dial": a company
should license only what it can codify, make profitable before copying, and
monitor from a distance. Its full version (with keys) runs on SkillSimm.
