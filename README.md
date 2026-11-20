# SkillSimm Template Submissions

The creator pipeline for **SkillSimm simulations** — workplace simulations
where real people make the judgment calls inside AI-assisted workflows.
Templates are submitted here as pull requests, validated by CI, reviewed by
humans, and published to the SkillSimm library.

**🌐 Start at the Simulation Hub: <https://skillsimm.github.io/skillsimm-template-submissions/>**

| I want to… | Go to |
|---|---|
| Create a simulation with an AI agent (Claude, ChatGPT) | [Create guide](https://skillsimm.github.io/skillsimm-template-submissions/create.html) — write a 4-section structured report, submit through an AI agent |
| Create a simulation **without** an AI agent | [Start from an example](https://skillsimm.github.io/skillsimm-template-submissions/edit.html) — copy a starter from [`examples/`](examples/), edit it in your browser, open a PR |
| See what a template can do | [`examples/`](examples/) — a 5-seat executive team (from the Shake Shack case) and a 2-seat AI session desk |
| Set up and run a simulation | [Set up and run](https://skillsimm.github.io/skillsimm-template-submissions/edit.html#run) |
| Browse jobs & the simulations that practice them | [Jobs & simulations](https://skillsimm.github.io/skillsimm-template-submissions/jobs.html) |
| Understand the package format | [Format reference](https://skillsimm.github.io/skillsimm-template-submissions/format.html) · [`schemas/`](schemas/) |
| Submit a package from the command line | [CONTRIBUTING.md](CONTRIBUTING.md) |

## How a simulation gets published

```
You describe → AI drafts ─┐
                          ├→ CI validates → Humans review → Test run → Published
You copy a starter + edit ┘
```

Nothing publishes without human review. There are two ways in:

- **With an AI agent.** Describe a workflow — what it looks like, the
  materials needed, the human decision boundaries and standard operating
  procedure, and the edge cases. The SkillSimm Template MCP
  (`https://mcp.skillsimm.com/mcp`, also listed in the
  [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.SkillSimm%2Fskillsimm/versions/latest))
  turns that report into a package and opens a PR here.
- **Without one.** Fork this repo, copy a starter from `examples/` into
  `templates/<your-slug>/`, edit it in github.dev (press `.` on your fork),
  and open a PR.

Either way, the `validate` workflow and a reviewer checklist gate the merge.
This repository is public: leave answer keys out of your PR and send them to
your reviewer privately.

## Repository layout

```
templates/   one folder per submitted simulation
examples/    starters to copy (app format: template.json + stages/*.json)
schemas/     JSON Schemas for the lite format (template.yaml, steps.yaml, …)
scripts/     validate_package.py (both formats), folder_template.py (app format),
             new_template.py (scaffold), vendored template_package/ (lite format)
docs/        the Simulation Hub site (GitHub Pages, served from main:/docs)
```

Copy a starter and validate it locally:

```bash
python scripts/new_template.py --slug my-case --from-example team-decision
python scripts/validate_package.py templates/my-case
```
