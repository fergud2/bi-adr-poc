---
id: ADR-0008
title: Reject Unrestricted SQL Access for Viewers
status: Accepted
date: 2026-03-27
owner: platform-security-team
application: internal-bi-platform
system: analytics-platform
domain: security
tags:
  - authorization
  - sql
  - viewer
review_date: 2026-09-27
supersedes:
superseded_by:
---

# ADR-0008: Reject Unrestricted SQL Access for Viewers

## Context

Viewers need access to dashboards and approved analytical results, but unrestricted SQL would create data leakage and operational risk.

## Decision

Do not allow Viewer users to write arbitrary SQL. Viewers may only interact through dashboards, approved filters, and approved saved questions.

## Alternatives Considered

- Allow all authenticated users to write SQL.
- Allow SQL only with row limits.
- Allow SQL after a one-time warning.

## Consequences

Positive:
- Reduces data leakage risk.
- Reduces accidental source system impact.
- Simplifies permission model.

Negative:
- Power users may request Analyst access.
- Some ad hoc workflows require escalation.
