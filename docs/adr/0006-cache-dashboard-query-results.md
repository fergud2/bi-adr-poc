---
id: ADR-0006
title: Cache Dashboard Query Results
status: Accepted
date: 2026-03-20
owner: platform-performance-team
application: internal-bi-platform
system: analytics-platform
domain: performance
tags:
  - caching
  - redis
  - performance
review_date: 2026-09-20
supersedes:
superseded_by:
---

# ADR-0006: Cache Dashboard Query Results

## Context

Repeated dashboard loads can create avoidable pressure on source PostgreSQL systems and increase user-facing latency.

## Decision

Use a Redis-compatible cache for dashboard tile query results, keyed by semantic query specification, filter values, dataset version, and permission scope.

## Alternatives Considered

- No caching.
- Browser-only caching.
- Materialize all dashboard results into the metadata database.

## Consequences

Positive:
- Faster dashboard loads.
- Reduced source database load.
- Tunable freshness by dashboard type.

Negative:
- Requires cache invalidation rules.
- May produce stale results within configured TTL.
