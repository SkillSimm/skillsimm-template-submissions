# How this desk works

> Starter placeholder. Replace with your own run instructions.

Two seats share one team:

1. **Operator (seat 1)** — a person. Opens the session by stating the goal, the
   folder or repository, and what needs their approval. Ends the session by
   recording the outcome and what is left.
2. **Local session (seat 2)** — an AI agent session (Claude Code, Codex, …) on
   someone's computer, connected through the SkillSimm desk script that the run
   page shows. It posts its messages and questions into team chat and keeps a
   short session log.

The operator and the session talk in team chat. When the operator is done, they
tell the session to finish (`/end`) and then submit "End the session".

Each local session that joins with the run's join code becomes its own team, so
one run can hold several sessions (frontend, backend, …). The run owner admits
each waiting session from the run page.
