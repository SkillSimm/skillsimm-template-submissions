# Contributing a template

**New to this — or don't code?** Start at the
[Simulation Hub create guide](https://skillsimm.github.io/skillsimm-template-submissions/create.html):
write a four-section structured report (workflow, materials, human decision
boundaries & SOP, edge cases) and an AI agent builds and submits the package
for you. The rest of this document covers the hands-on paths.

Most submissions arrive through the **SkillSimm Template MCP** — point your
agent (Claude Code, Codex, Cursor) at `https://mcp.skillsimm.com/mcp` with a
SkillSimm API token and ask it to create a template; the
`submit_to_github_review` tool opens the PR here for you.

### No AI agent? Start from an example (browser only)

Follow [Start from an example](https://skillsimm.github.io/skillsimm-template-submissions/edit.html):

1. Fork this repo and press `.` on your fork to open github.dev.
2. Copy `examples/team-decision-starter/` or `examples/session-desk-starter/`
   into `templates/<your-slug>/` (lowercase, hyphens).
3. Work through the starter's README: name, seats, materials, questions, AI
   settings, grading.
4. Commit & push, then open a PR. The `validate` check lists anything to fix
   (file, task and what's wrong).

### From the command line

1. Branch from `main`: `publish/<slug>`.
2. Copy a starter (`python scripts/new_template.py --slug <slug> --from-example
   team-decision|session-desk`) or scaffold the lite YAML format
   (`python scripts/new_template.py --slug <slug>`).
3. Run `python scripts/validate_package.py templates/<slug>` until clean.
4. Open a PR. The `validate` workflow must pass; reviewers then work through
   the checklist.

### Answer keys stay private

This repository is public. Don't commit real answer keys
(`evaluation/reference_decisions.json`, `ai_answer` values that must stay
secret, scoring code). Leave placeholders and send the keys to your reviewer;
SkillSimm adds them when it sets the template up. The validator warns when it
sees them.

## What reviewers look for

Clear instructions, sound step logic, honest grading (answer keys verified,
rubrics measurable), safe and original content, and a template that produces a
meaningful evaluation report when run.

## Licensing & royalties

By submitting you agree SkillSimm may modify, delist, or version the template
for safety/quality. State your royalty preference in `creator.yaml`
(`fixed_fee | revenue_share | per_run | open_source | enterprise_only`);
revenue terms are settled before merge.

## Keeping the validator in sync

Two validators run in CI. `scripts/folder_template.py` (app format) is local
to this repo and stdlib-only; keep its checks in line with what the app's
seeder reads (`Simulation_TaskFlow/backend/app/seed.py`,
`_load_folder_template`). `scripts/template_package/` (lite format) is vendored from
`Simulation_TaskFlow/backend/app/template_package` (canonical source). When the
schema changes there, copy the module over in the same PR that updates
`schemas/`.
