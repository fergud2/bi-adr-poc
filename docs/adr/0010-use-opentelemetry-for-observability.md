---
id: ADR-0010
title: Use OpenTelemetry for Observability Instrumentation
status: Accepted
date: 2026-04-05
owner: platform-observability-team
application: internal-bi-platform
system: analytics-platform
domain: observability
tags:
  - opentelemetry
  - traces
  - metrics
  - logs
review_date: 2026-10-05
supersedes:
superseded_by:
---

# ADR-0010: Use OpenTelemetry for Observability Instrumentation

## Context

The platform has multiple services and asynchronous jobs. Operators need traces, metrics, and logs to diagnose failures and validate runtime dependencies.

## Decision

Instrument services using OpenTelemetry and export telemetry through a collector to the enterprise observability backend.

## Alternatives Considered

- Vendor-specific instrumentation only.
- Logging only.
- Add observability after production launch.

## Consequences

Positive:
- Vendor-neutral instrumentation.
- Runtime dependency discovery.
- Better incident response.

Negative:
- Requires consistent propagation of trace context.
- Requires careful handling of sensitive data in logs and traces.
