---
id: ADR-0002
title: Separate Query Execution into a Dedicated Service
status: Accepted
date: 2026-03-05
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: analytics
tags:
  - security
  - query-service
  - architecture
review_date: 2026-09-05
supersedes:
superseded_by:
---

# ADR-0002: Separate Query Execution into a Dedicated Service

## Context

The platform must execute analytical SQL against source PostgreSQL systems while protecting those systems from unsafe, expensive, or unauthorized queries.

## Decision

Create a dedicated Query Service responsible for read-only SQL validation, query execution, row-level policy injection, timeouts, result limits, and caching.

## Alternatives Considered

- Execute SQL directly from the Backend API.
- Let frontend clients connect directly to data sources.
- Use a third-party BI query engine only.

## Consequences

Positive:
- Clear security boundary.
- Easier to audit query execution.
- Allows query execution to scale independently.

Negative:
- Additional service to build and operate.
- More internal API contracts to maintain.
