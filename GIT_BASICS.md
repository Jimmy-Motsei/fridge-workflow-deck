# Git Basics — One‑Page Cheat Sheet

A quick reference for everyday Git work. Safe defaults, short explanations, and “what to do when it barks.”

---

## Mental model (4 places a change can live)

1) **Working folder** — your files on disk  
2) **Staging area** (index) — “put these edits in the next snapshot”  
3) **Local repo** — your commits stored in `.git/`  
4) **Remote repo** — GitHub’s copy

```
Edit → git add → git commit → git push
               ↑            ↑
           stage set    sync history
```

---

## New project (single dev)

```bash
mkdir my-app && cd my-app
git init
echo "<!doctype html>" > index.html
git add index.html
git commit -m "feat: initial page"

# connect to GitHub (replace with your repo URL)
git branch -M main
git remote add origin https://github.com/USER/my-app.git
git push -u origin main
```

---

## Daily loop

```bash
# see what's changed
git status

# stage specific files or everything
git add app.js styles.css
# or: git add -A

# commit (snapshot into local history)
git commit -m "feat: thing I actually did"

# sync to GitHub
git push
```

---

## Pulling remote changes (recommended: rebase)

```bash
git pull --rebase origin main
# if conflicts:
#   (edit files to fix) → git add <file> → git rebase --continue
```

**Why rebase?** Linear history; your commits are replayed on top of the latest remote.

---

## Branching workflow

```bash
# create a feature branch
git checkout -b feature/offer-engine

# work… then commit & push
git add -A
git commit -m "feat: offer rules v1"
git push -u origin feature/offer-engine

# open a PR (GitHub CLI)
gh pr create --fill
```

Merge the PR in GitHub, then update local:
```bash
git checkout main
git pull --rebase
```

---

## Fixups & amends

```bash
# add a forgotten file to the last commit (no new commit)
git add forgot.txt
git commit --amend --no-edit

# squash local commits before opening PR
git rebase -i HEAD~3
# mark extra commits as 's' (squash), save & exit
```

---

## Undo / clean up

```bash
# throw away unstaged local edits in a file
git restore path/to/file

# unstage (keep working copy)
git restore --staged path/to/file

# DISCARD everything back to last commit
git reset --hard HEAD

# reset branch to remote (danger: discards local commits)
git fetch origin
git reset --hard origin/main
```

---

## Rebase vs Merge (visual)

```
# Before
origin/main:  A──B──C
your branch:  A──B──x──y

# Rebase (recommended for feature branches)
A──B──C──x'──y'   (linear; x,y replayed)
# Merge
A──B──C───M
      └──x──y    (non‑linear; extra merge commit M)
```

---

## Common errors → Remedies

- **`[rejected] (fetch first)`**  
  Remote has new commits.  
  → `git pull --rebase origin main` then `git push`.

- **`cannot pull with rebase: You have unstaged changes`**  
  Clean your tree first.  
  → `git add … && git commit` **or** `git stash` **or** `git restore -- .`

- **`fatal: The current branch has no upstream`**  
  First push sets upstream.  
  → `git push -u origin <branch>`

- **`Updates were rejected because the tip of your current branch is behind`**  
  Same as fetch first; pull with rebase.

---

## Quick aliases (optional)

```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

Use: `git lg` to see the graph quickly.

---

## Safe defaults to remember

- Prefer `git pull --rebase` over plain `git pull`.  
- Use `git push --force-with-lease` (not `--force`) *only for your own feature branches* after rebasing.  
- Commit messages: `feat:`, `fix:`, `chore:`, `docs:` with a clear verb.

```
Happy committing! 🚀
```
