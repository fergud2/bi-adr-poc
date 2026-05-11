---
id: ADR-0012
title: Use Worker Queue for MVP Async Jobs
status: Accepted
date: 2026-04-12
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: workflow
tags:
  - worker
  - async-jobs
  - reports
review_date: 2026-10-12
supersedes: ADR-0011
superseded_by:
---

# ADR-0012: Use Worker Queue for MVP Async Jobs

## Context

CSV imports, scheduled reports, and export generation need asynchronous execution. A full durable workflow platform was rejected for the MVP in ADR-0011.

## Decision

Use a worker queue for MVP async jobs. Jobs must store status, retry count, input references, and error messages in the metadata database.

## Alternatives Considered

- Durable workflow engine.
- In-process background tasks.
- Manual batch scripts.

## Consequences

Positive:
- Faster MVP delivery.
- Clear async execution path.
- Compatible with later workflow engine migration.

Negative:
- Limited visual workflow management.
- Requires careful idempotency design.
