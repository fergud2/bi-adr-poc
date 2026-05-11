---
id: ADR-0013
title: Enforce Row-Level Access Policies in Query Service
status: Accepted
date: 2026-04-18
owner: platform-security-team
application: internal-bi-platform
system: analytics-platform
domain: security
tags:
  - row-level-security
  - authorization
  - query-service
review_date: 2026-10-18
supersedes:
superseded_by:
---

# ADR-0013: Enforce Row-Level Access Policies in Query Service

## Context

Different users may be allowed to see different slices of the same dataset, such as region, department, or account ownership.

## Decision

Enforce row-level access policies inside the Query Service by injecting mandatory predicates into validated SQL.

## Alternatives Considered

- Rely only on dashboard filters.
- Create separate physical tables per department.
- Rely only on source database permissions.

## Consequences

Positive:
- Consistent enforcement across dashboards, saved questions, and NL queries.
- Central audit point.
- Reduces accidental leakage through generated SQL.

Negative:
- SQL generation and validation are more complex.
- Policy bugs can have high impact.
