# skillsimm-ats-ingest

Fetch and filter live job postings from public ATS boards — **no API keys, no scraping**.

Thousands of companies expose their open roles as public JSON:

| Source | Endpoint | Key needed |
|---|---|---|
| Greenhouse | `boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true` | no |
| Lever | `api.lever.co/v0/postings/{company}?mode=json` | no |
| Ashby | `api.ashbyhq.com/posting-api/job-board/{board}` | no |
| USAJobs | `data.usajobs.gov/api/search` | free key (`USAJOBS_API_KEY` + `USAJOBS_EMAIL`) |
| Adzuna | `api.adzuna.com/v1/api/jobs/us/search/1` | free key (`ADZUNA_APP_ID` + `ADZUNA_APP_KEY`) |

Keyed sources simply no-op (with a log line) when their env vars are unset —
the keyless ATS sources alone cover thousands of postings.

## Install

```bash
pip install -e tools/ats-ingest
```

## Use

```bash
# All financial-analyst postings from the seeded boards, title-filtered:
python -m ats_ingest fetch --family financial_analyst --cache-dir cache --out postings.jsonl

# See what's configured:
python -m ats_ingest boards

# Raw dump of every posting on the boards (no title filter):
python -m ats_ingest fetch --family data_analyst --no-filter --limit 500
```

Output is JSONL — one normalized posting per line: `source`, `external_id`
(dedupe key with source), `company`, `board_slug`, `title`, `location`, `url`,
`posted_at`, `raw_text` (HTML-stripped description), `content_hash`.

Fetches are polite: shared 0.5s/host rate limit, exponential backoff on
429/5xx, and a `--cache-dir` cache that is hit before any network call
(`--refresh` bypasses it).

## Add your company / your family

`src/ats_ingest/data/job_boards.json` is the seed list — families with
`title_rules` (substring filters), O*NET SOC anchors, and per-source board
slugs. Adding a board is a one-line PR; adding a family is a small JSON block.
Every slug in the committed list is live-verified.

## O*NET anchors

`python -m ats_ingest.onet --onet-dir <unzipped O*NET text db> --socs 13-2051.00,...`
regenerates `data/onet_anchors.json` from the free
[O*NET database](https://www.onetcenter.org/database.html) — the authoritative
task/tool vocabulary per occupation, used downstream as canonical anchors.

## Why this exists

This package powers the [SkillSimm](https://skillsimm.github.io/skillsimm-template-submissions/)
creator community: the same feeds drive a public job board matched to practice
simulations, and the demand-gap reports (`GAPS.md`) that tell creators which
simulation to build next. It's also a perfectly good standalone job-filtering
tool — use it for whatever you like (MIT).
