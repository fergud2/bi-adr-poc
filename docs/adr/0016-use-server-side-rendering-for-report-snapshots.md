---
id: ADR-0016
title: Use Server-Side Rendering for Scheduled Report Snapshots
status: Accepted
date: 2026-05-02
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: reporting
tags:
  - reporting
  - dashboard-snapshot
  - worker
review_date: 2026-11-02
supersedes: ADR-0015
superseded_by:
---

# ADR-0016: Use Server-Side Rendering for Scheduled Report Snapshots

## Context

Scheduled reports need to deliver dashboard snapshots reliably without depending on an active user browser session.

## Decision

Use server-side rendering in the Worker Service for scheduled dashboard report snapshots. Email delivery may include a secure dashboard link and optionally a rendered snapshot.

## Alternatives Considered

- Browser-only rendering.
- Email links only.
- Pre-render all dashboards continuously.

## Consequences

Positive:
- Reliable scheduled report delivery.
- Better auditability.
- Supports future PDF/PNG exports.

Negative:
- Requires rendering service hardening.
- Must enforce permissions under the schedule owner context.
