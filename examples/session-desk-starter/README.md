# Session desk starter (based on *SkillSimm · Session Desk*)

A person directs an AI agent session (Claude Code, Codex, …) running on
someone's computer. The person sits in seat 1 (Operator); the agent session sits
in seat 2 and talks through team chat. Nothing is scored. It is a working
session with a clear goal, approval rules and a record of the outcome.

This is a copy of SkillSimm's `SkillSimm_Session_Desk` template with the
internal install instructions replaced by a plain description.

## What this template shows

| Feature | Where it lives |
|---|---|
| The smallest useful template: 2 seats, 2 stages, 3 tasks | `template.json`, `stages/01_open.json`, `stages/02_work.json` |
| Free-text forms (goal, folder, approvals, outcome) | task `field_schema` with type `textarea` and `required_fields` |
| A seat filled by an AI agent instead of a person | `staffing.desk_teams.session_seat: 2` |
| Runs with 1 or 2 people | `staffing.allowed_sizes: [2, 1]`, `start.min_humans: 1` |
| No AI chat assistant, team chat on | `ai_chat_enabled: false`, `group_communication_allowed: true` |
| No time limit | `timing.enabled: false` |
| No scoring | every task `evaluation_point: false`; `metadata.scoring_type: "none"` |
| Anyone may pick up a stuck task | `coordination.routing.takeover.leader_only: false` |
| Contact details encrypted in exports | `privacy.encrypt_participant_contacts: true` |
| One run, many teams (one per agent session) | `staffing.desk_teams` |

## Make it yours

- **Change the forms.** In `stages/01_open.json`, edit or add fields in
  `field_schema` (e.g. a `select` for priority, a `text` for a ticket number) and
  list required ones in `required_fields`.
- **Add a review step.** Add a task to `stages/02_work.json` for seat 1, or add
  `stages/03_review.json` with `"dependencies": ["work"]`.
- **Use people in both seats.** Remove `desk_teams` from `staffing`, and the
  template becomes a two-person workflow (e.g. requester and specialist).
- **Turn on AI help.** Set `ai_chat_enabled: true` and add a `skills/*.md` file
  that tasks name in `ai_guidance_skill` (see the team decision starter).
- **Replace the material.** `materials/how_this_desk_works.md` is what both seats
  read first.
