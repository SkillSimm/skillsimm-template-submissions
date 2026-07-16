# SkillSimm Template Submissions

The creator pipeline for **SkillSimm simulations** — workplace simulations
where real people make the judgment calls inside AI-assisted workflows.
Templates are submitted here as pull requests, validated by CI, reviewed by
humans, and published to the SkillSimm library.

**🌐 Start at the Simulation Hub: <https://skillsimm.github.io/skillsimm-template-submissions/>**

| I want to… | Go to |
|---|---|
| Create a simulation (no code needed) | [Create guide](https://skillsimm.github.io/skillsimm-template-submissions/create.html) — write a 4-section structured report, submit through an AI agent |
| Browse published simulations | [Gallery](https://skillsimm.github.io/skillsimm-template-submissions/explore.html) |
| Understand the package format | [Format reference](https://skillsimm.github.io/skillsimm-template-submissions/format.html) · [`schemas/`](schemas/) |
| Submit a package by hand | [CONTRIBUTING.md](CONTRIBUTING.md) |

## How a simulation gets published

```
You describe → AI drafts → CI validates → Humans review → Test run → Published
```

Nothing publishes without human review. Creators describe a workflow —
what it looks like, the materials needed, the human decision boundaries and
standard operating procedure, and the edge cases. The SkillSimm Template MCP
(`https://mcp.skillsimm.com/mcp`) turns that report into a formal package and
opens a PR here; the `validate` workflow and a reviewer checklist gate the merge.

## Repository layout

```
templates/   one folder per simulation package (see the reference:
             templates/consumer-complaint-escalation/)
schemas/     JSON Schemas for template.yaml, steps.yaml, metadata.yaml, creator.yaml
scripts/     validate_package.py + vendored validator module
docs/        the Simulation Hub site (GitHub Pages, served from main:/docs)
```

Validate a package locally:

```bash
python scripts/validate_package.py templates/<slug>
```
