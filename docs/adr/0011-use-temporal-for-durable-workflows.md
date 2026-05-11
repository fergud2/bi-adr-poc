---
id: ADR-0011
title: Use Durable Workflow Engine for Async Jobs
status: Rejected
date: 2026-04-10
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: workflow
tags:
  - workflow
  - async-jobs
  - temporal
review_date: 2026-07-10
supersedes:
superseded_by:
---

# ADR-0011: Use Durable Workflow Engine for Async Jobs

## Context

CSV imports and scheduled reports require asynchronous execution, retries, and job state tracking.

## Decision

Reject adopting a full durable workflow engine for the MVP. Use a simpler worker queue initially, while keeping service boundaries compatible with a future workflow engine.

## Alternatives Considered

- Temporal from day one.
- Celery/RQ-style worker queue.
- Cron-only scheduled jobs.

## Consequences

Positive:
- Reduces MVP operational complexity.
- Allows faster contractor implementation.

Negative:
- Long-running workflow visibility is more limited.
- Complex retries may require future migration.
