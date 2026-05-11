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
  - postgres
review_date: 2026-09-01
supersedes:
superseded_by:
---

# ADR-0001: Use PostgreSQL for Application Metadata

## Context

The BI platform needs a durable metadata store for users, workspaces, dashboards, charts, semantic models, report schedules, audit logs, and natural-language query history.

## Decision

Use PostgreSQL as the application metadata database.

## Alternatives Considered

- MySQL
- MongoDB
- SQLite
- Reusing the source PostgreSQL database

## Consequences

Positive:
- Strong relational consistency for metadata.
- Familiar operational model.
- Good JSON support for flexible dashboard and query specifications.

Negative:
- Requires schema migrations and backup strategy.
- Must be isolated from source business databases.
