#!/usr/bin/env bash
# One-time GitHub label setup for the gap-claim workflow. Run manually:
#   bash scripts/setup_gap_labels.sh
# Requires: gh CLI authenticated with repo access.
set -euo pipefail
REPO="SkillSimm/skillsimm-template-submissions"

# The generic claim label (used by the issue template)
gh label create "gap-claim" --repo "$REPO" --color "d4c5f9" \
  --description "Creator claiming a GAPS.md item" --force

# Per-gap labels: create them from the current GAPS.md entries.
# Re-run after each publish; existing labels are updated in place (--force).
grep -oE 'gap:[a-z0-9-]+' GAPS.md | sort -u | while read -r label; do
  gh label create "$label" --repo "$REPO" --color "0e8a16" \
    --description "Uncovered demand item from GAPS.md" --force
  echo "label: $label"
done
