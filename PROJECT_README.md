# Fridge MVP — Project Operating Guide

This repo’s **GitHub Project (v2)** is: **Fridge MVP** (user-level project #2).  
Use this page as the quick reference for how we plan, track, and ship.

## Views & Fields
Create the following **fields** in the Project (Table view):
- **Status** *(Single select)*: `Todo` / `In Progress` / `Done`
- **Start** *(Date)*: when work begins
- **Due** *(Date)*: target finish date
- **Estimate (h)** *(Number)*: initial time estimate

> Optional fields (add later if useful): **Owner**, **Risk**, **Blocked By**, **Release**

## Item Types
- **Task**: execution work (use the *Task* template below)
- **Feature**: user-facing change (use *Feature request* template)
- **Bug**: broken behaviour (use *Bug report* template)

## Labels (create once in the repo)
- `MVP` – core pilot work
- `WhatsApp` – channel-related
- `Ops` – dashboard/back-office
- `Runner` – field/collection flow
- `Data` – data model, pricing rules

```bash
# create labels (safe to run; -f ignores "already exists")
gh label create "MVP" --color FFD966 -d "Project work" -f
gh label create "WhatsApp" --color 1D76DB -d "WhatsApp channel" -f
gh label create "Ops" --color 5319E7 -d "Operations UI" -f
gh label create "Runner" --color 0E8A16 -d "Runner mobile flow" -f
gh label create "Data" --color FBCA04 -d "Data model / rules" -f
```

## Workflow
1. **Create** items via issue templates (Task / Feature / Bug).
2. **Add** the issue to **Fridge MVP** project (UI: *Add → Add from repository*).
3. **Set fields**: Status, Start, Due, Estimate (h).
4. **Work** on a branch named `issue-<number>-<slug>`; open a PR referencing the issue.
5. **Move** Status → `Done` when merged & deployed.

## Useful CLI
```bash
# create a task issue quickly
gh issue create --title "A2: Conversation flow – Sell" --label "MVP,WhatsApp" --body "See FlowSpec"

# add the last created issue to the project
OWNER="Jimmy-Motsei"; PROJECT_NUMBER=2
LAST_URL=$(gh issue list --limit 1 --sort created --json url -q '.[0].url')
gh project item-add "$PROJECT_NUMBER" --owner "$OWNER" --url "$LAST_URL"

# open the project board
gh project view 2 --owner "Jimmy-Motsei" --web
```

## Conventions
- **Commit messages**: `feat:`, `fix:`, `chore:`, `docs:`
- **PR title**: `A<ID> - short summary` (link the issue)
- **Definition of Done**: Acceptance criteria met, tests/flows updated, docs touched, item moved to `Done`.

---

### Importing the starter CSV
If you haven’t yet imported the starter tasks, run the CSV-to-issues script from the repo root (requires `gh`):

```bash
python3 scripts/csv_to_issues.py   # or use the inline one-liner we shared
```
