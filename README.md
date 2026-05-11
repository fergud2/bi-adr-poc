# BI ADR POC

This repository is a proof-of-concept for managing Architecture Decision Records (ADRs) in Git and generating an ADR report for an application.

## Contents

```text
docs/
  adr/
    0001-use-postgresql-for-metadata.md
    ...
  reports/
scripts/
  generate_adr_report.py
.github/
  workflows/
    adr-report.yml
```

## ADR Metadata Standard

Each ADR uses YAML front matter:

```yaml
---
id: ADR-0001
title: Use PostgreSQL for Application Metadata
status: Accepted
date: 2026-03-01
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: analytics
tags:
  - database
  - metadata
review_date: 2026-09-01
supersedes:
superseded_by:
---
```

Allowed statuses:

```text
Proposed
Accepted
Rejected
Superseded
Deprecated
```

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/generate_adr_report.py \
  --adr-dir docs/adr \
  --application internal-bi-platform \
  --title "Internal BI Platform ADR Report" \
  --output docs/reports/internal-bi-platform-adr-report.md \
  --include-git
```

Validate only:

```bash
python scripts/generate_adr_report.py \
  --adr-dir docs/adr \
  --validate-only
```

Filter by domain:

```bash
python scripts/generate_adr_report.py \
  --adr-dir docs/adr \
  --domain security \
  --title "Security ADR Report" \
  --output docs/reports/security-adr-report.md
```

Filter by tag:

```bash
python scripts/generate_adr_report.py \
  --adr-dir docs/adr \
  --tag nl-query \
  --title "Natural Language Querying ADR Report" \
  --output docs/reports/nl-query-adr-report.md
```

## GitHub Actions

The workflow at `.github/workflows/adr-report.yml` validates ADR metadata and generates a Markdown report on pull requests and pushes to `main`.

## Upload to a Test GitHub Repository

Create an empty GitHub repository first, then run:

```bash
git init
git add .
git commit -m "Initial ADR POC"

git branch -M main
git remote add origin https://github.com/YOUR_ORG_OR_USER/bi-adr-poc.git
git push -u origin main
```

Using GitHub CLI:

```bash
gh repo create bi-adr-poc --private --source=. --remote=origin --push
```

## Notes

This is a POC. Before production use, add organization-specific metadata such as criticality tier, data classification, affected systems, architecture review board reference, and security review ID.
