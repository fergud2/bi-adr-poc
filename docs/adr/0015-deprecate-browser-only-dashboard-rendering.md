---
id: ADR-0015
title: Deprecate Browser-Only Dashboard Snapshot Rendering
status: Deprecated
date: 2026-04-30
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: reporting
tags:
  - reporting
  - dashboard-snapshot
  - deprecated
review_date: 2026-05-05
supersedes:
superseded_by: ADR-0016
---

# ADR-0015: Deprecate Browser-Only Dashboard Snapshot Rendering

## Context

The initial reporting concept relied on the user's browser to render dashboard snapshots for scheduled reports.

## Decision

Deprecate browser-only dashboard snapshot rendering. Scheduled reports should be rendered server-side by the worker service.

## Alternatives Considered

- Browser-only snapshot rendering.
- Email links only.
- Server-side rendering.

## Consequences

Positive:
- More reliable scheduled reports.
- Does not require user browser sessions.
- Supports unattended delivery.

Negative:
- Requires rendering infrastructure in worker service.
