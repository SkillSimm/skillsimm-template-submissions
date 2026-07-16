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

Submitting by hand works too:

1. Branch from `main`: `publish/<slug>`.
2. Add your package under `templates/<slug>/` (see the reference package and
   `schemas/`).
3. Run `python scripts/validate_package.py templates/<slug>` until clean.
4. Open a PR. The `validate` workflow must pass; reviewers then work through
   the checklist.

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

`scripts/template_package/` is vendored from
`Simulation_TaskFlow/backend/app/template_package` (canonical source). When the
schema changes there, copy the module over in the same PR that updates
`schemas/`.
