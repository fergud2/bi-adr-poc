---
id: ADR-0005
title: Support CSV Upload for Small Ad Hoc Datasets
status: Accepted
date: 2026-03-15
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: data-ingestion
tags:
  - csv
  - ingestion
  - object-storage
review_date: 2026-09-15
supersedes:
superseded_by:
---

# ADR-0005: Support CSV Upload for Small Ad Hoc Datasets

## Context

Analysts frequently need to join or visualize manually curated datasets before formal pipelines exist.

## Decision

Support CSV uploads into managed internal analytical tables, with validation, schema inference, size limits, and audit logging.

## Alternatives Considered

- Require all data to come from PostgreSQL.
- Let analysts upload files directly into source databases.
- Use spreadsheets as the long-term data source.

## Consequences

Positive:
- Enables rapid analysis.
- Reduces engineering bottlenecks for small datasets.
- Keeps ad hoc data inside governed platform controls.

Negative:
- Requires validation and cleanup workflows.
- May encourage long-lived manual datasets unless lifecycle controls are added.
