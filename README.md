# SkillSimm Template Submissions

Private review repo for the SkillSimm template marketplace. **Merged folders
under `templates/` on `main` are the registry** — the SkillSimm backend syncs
them on startup (`GITHUB_SYNC_ENABLED=true`) and lists them as
verified marketplace templates.

## How a template gets here

```
Claude / Codex / Cursor (creator's agent)
        ↓  SkillSimm MCP server (mcp.skillsimm.com)
Draft in SkillSimm DB
        ↓  submit_to_github_review
Pull request on this repo        ← you are here
        ↓  GitHub Actions validation (required check)
        ↓  internal review (PR template checklist)
        ↓  merge = approval
templates/<slug>/ on main
        ↓  backend sync_from_registry
Public template library → user My Library → runs
```

Agents create; they never publish. Merging a PR is the only publish path.

## Package format

Each template is a folder under `templates/`:

| File | Required | Contents |
|---|---|---|
| `template.yaml` | ✓ | id, title, objective, audience, roles, team_size |
| `steps.yaml` | ✓ | ordered steps: actor_mode, task_type, task_description, grading |
| `grading.yaml` | | grading rules keyed by step id (inline rules in steps.yaml win) |
| `metadata.yaml` | | marketplace discovery: domain, difficulty, duration, tags… |
| `creator.yaml` | | creator profile + royalty preference |
| `sample_inputs.json` / `expected_outputs.json` | | example run data |
| `README.md` | ✓ | what the template trains, ≥200 chars |
| `LICENSE.md` | ✓ | license + SkillSimm modification clause |

JSON Schemas for every file live in [`schemas/`](schemas/). The reference
package is [`templates/consumer-complaint-escalation/`](templates/consumer-complaint-escalation/).

Validate locally:

```bash
pip install "pydantic>=2.10,<3" "pyyaml>=6"
python scripts/validate_package.py templates/<your-slug>
```

## Labels

`new-submission` → `schema-pass` / `needs-revision` → `internal-test-pass` →
`royalty-pending` → `approved` → `published` (or `rejected`).

## Review rules

- The `validate` check must pass before merge.
- Reviewers work through the checklist in the PR template.
- Royalty terms are agreed before merge for revenue-share templates
  (`royalty-pending` label while open).
