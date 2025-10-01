#!/usr/bin/env python3
# Create issues from fridge_mvp_tasks.csv using GitHub CLI (`gh`)
import csv, subprocess, sys, os

CSV_FILE = "fridge_mvp_tasks.csv"
if not os.path.exists(CSV_FILE):
    print(f"CSV not found: {CSV_FILE}")
    sys.exit(1)

with open(CSV_FILE, newline='') as f:
    for row in csv.DictReader(f):
        title = f"{row['ID']}: {row['Title']}"
        body = (
            f"Estimate: {row['Estimate (h)']}h\n"
            f"Start: {row['Start']}\n"
            f"Due: {row['Due']}\n"
            f"Milestone: {row['Milestone']}"
        )
        labels = [x.strip() for x in row['Labels'].split(',') if x.strip()]
        cmd = ["gh","issue","create","--title",title,"--body",body]
        for lab in labels:
            cmd += ["--label", lab]
        subprocess.run(cmd, check=True)
print("✅ Issues created from CSV.")
