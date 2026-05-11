---
id: ADR-0004
title: Use a Semantic Layer for Governed Metrics
status: Accepted
date: 2026-03-12
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: analytics
tags:
  - semantic-layer
  - metrics
  - governance
review_date: 2026-09-12
supersedes:
superseded_by:
---

# ADR-0004: Use a Semantic Layer for Governed Metrics

## Context

Business users need consistent definitions for metrics such as revenue, churn, active users, and retention. Natural-language querying also needs a constrained business model rather than unrestricted raw database schemas.

## Decision

Introduce a semantic layer containing approved datasets, fields, measures, metrics, joins, default filters, and row-level policies.

## Alternatives Considered

- Allow dashboards to define metrics independently.
- Allow raw SQL as the primary modeling interface.
- Use a third-party semantic layer from day one.

## Consequences

Positive:
- Consistent metric definitions.
- Safer natural-language querying.
- Better access control.

Negative:
- Analysts must model datasets before broad use.
- Requires ownership and certification workflows.
