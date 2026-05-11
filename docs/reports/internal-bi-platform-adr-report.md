# ADR Report: Internal BI Platform ADR Report

Generated on: `2026-05-11`

## Summary

- Total ADRs: 17
- Accepted: 14
- Deprecated: 1
- Proposed: 1
- Rejected: 1
- Proposed decisions: 1
- Overdue reviews: 0

## ADRs by Status

| Status | Count |
| --- | --- |
| Accepted | 14 |
| Deprecated | 1 |
| Proposed | 1 |
| Rejected | 1 |

## ADRs by Domain

| Domain | Count |
| --- | --- |
| ai | 1 |
| analytics | 3 |
| data-ingestion | 1 |
| identity | 1 |
| infrastructure | 2 |
| observability | 1 |
| performance | 1 |
| reporting | 3 |
| security | 2 |
| workflow | 2 |

## ADRs by Owner

| Owner | Count |
| --- | --- |
| data-platform-team | 10 |
| platform-infrastructure-team | 2 |
| platform-observability-team | 1 |
| platform-performance-team | 1 |
| platform-security-team | 3 |

## Top Tags

| Tag | Count |
| --- | --- |
| dashboard-snapshot | 3 |
| reporting | 3 |
| security | 3 |
| worker | 3 |
| async-jobs | 2 |
| authorization | 2 |
| csv | 2 |
| metrics | 2 |
| object-storage | 2 |
| query-service | 2 |
| ai | 1 |
| architecture | 1 |
| caching | 1 |
| cloud-agnostic | 1 |
| containers | 1 |
| database | 1 |
| deprecated | 1 |
| exports | 1 |
| governance | 1 |
| identity | 1 |

## Decisions Requiring Review

No ADRs are currently overdue for review.

## Proposed Decisions

| ID | Title | Date | Owner | Tags | File |
| --- | --- | --- | --- | --- | --- |
| ADR-0007 | Use Hosted LLM Provider for Natural-Language Querying | 2026-03-25 | data-platform-team | llm, nl-query, ai, security | docs\adr\0007-use-hosted-llm-for-natural-language-querying.md |

## Superseded or Deprecated Decisions

| ID | Title | Status | Superseded By | Date | File |
| --- | --- | --- | --- | --- | --- |
| ADR-0015 | Deprecate Browser-Only Dashboard Snapshot Rendering | Deprecated | ADR-0016 | 2026-04-30 | docs\adr\0015-deprecate-browser-only-dashboard-rendering.md |

## All ADRs

| ID | Title | Status | Date | Owner | Domain | Tags | Review Date | Supersedes | Superseded By | File |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADR-0001 | Use PostgreSQL for Application Metadata | Accepted | 2026-03-01 | data-platform-team | analytics | database, metadata, postgres | 2026-09-01 |  |  | docs\adr\0001-use-postgresql-for-metadata.md |
| ADR-0002 | Separate Query Execution into a Dedicated Service | Accepted | 2026-03-05 | data-platform-team | analytics | security, query-service, architecture | 2026-09-05 |  |  | docs\adr\0002-separate-query-service.md |
| ADR-0003 | Use OIDC for User Authentication | Accepted | 2026-03-08 | platform-security-team | identity | identity, security, oidc | 2026-09-08 |  |  | docs\adr\0003-use-oidc-for-authentication.md |
| ADR-0004 | Use a Semantic Layer for Governed Metrics | Accepted | 2026-03-12 | data-platform-team | analytics | semantic-layer, metrics, governance | 2026-09-12 |  |  | docs\adr\0004-use-semantic-layer.md |
| ADR-0005 | Support CSV Upload for Small Ad Hoc Datasets | Accepted | 2026-03-15 | data-platform-team | data-ingestion | csv, ingestion, object-storage | 2026-09-15 |  |  | docs\adr\0005-support-csv-upload-for-ad-hoc-data.md |
| ADR-0006 | Cache Dashboard Query Results | Accepted | 2026-03-20 | platform-performance-team | performance | caching, redis, performance | 2026-09-20 |  |  | docs\adr\0006-cache-dashboard-query-results.md |
| ADR-0007 | Use Hosted LLM Provider for Natural-Language Querying | Proposed | 2026-03-25 | data-platform-team | ai | llm, nl-query, ai, security | 2026-06-25 |  |  | docs\adr\0007-use-hosted-llm-for-natural-language-querying.md |
| ADR-0008 | Reject Unrestricted SQL Access for Viewers | Accepted | 2026-03-27 | platform-security-team | security | authorization, sql, viewer | 2026-09-27 |  |  | docs\adr\0008-reject-unrestricted-sql-for-viewers.md |
| ADR-0009 | Use S3-Compatible Object Storage for Uploads and Exports | Accepted | 2026-04-01 | platform-infrastructure-team | infrastructure | object-storage, csv, exports | 2026-10-01 |  |  | docs\adr\0009-use-object-storage-for-uploads-and-exports.md |
| ADR-0010 | Use OpenTelemetry for Observability Instrumentation | Accepted | 2026-04-05 | platform-observability-team | observability | opentelemetry, traces, metrics, logs | 2026-10-05 |  |  | docs\adr\0010-use-opentelemetry-for-observability.md |
| ADR-0011 | Use Durable Workflow Engine for Async Jobs | Rejected | 2026-04-10 | data-platform-team | workflow | workflow, async-jobs, temporal | 2026-07-10 |  |  | docs\adr\0011-use-temporal-for-durable-workflows.md |
| ADR-0012 | Use Worker Queue for MVP Async Jobs | Accepted | 2026-04-12 | data-platform-team | workflow | worker, async-jobs, reports | 2026-10-12 | ADR-0011 |  | docs\adr\0012-use-worker-queue-for-mvp-async-jobs.md |
| ADR-0013 | Enforce Row-Level Access Policies in Query Service | Accepted | 2026-04-18 | platform-security-team | security | row-level-security, authorization, query-service | 2026-10-18 |  |  | docs\adr\0013-use-row-level-access-policies.md |
| ADR-0014 | Use Cloud-Agnostic Container Deployment | Accepted | 2026-04-22 | platform-infrastructure-team | infrastructure | containers, kubernetes, cloud-agnostic | 2026-10-22 |  |  | docs\adr\0014-use-cloud-agnostic-container-deployment.md |
| ADR-0015 | Deprecate Browser-Only Dashboard Snapshot Rendering | Deprecated | 2026-04-30 | data-platform-team | reporting | reporting, dashboard-snapshot, deprecated | 2026-05-05 |  | ADR-0016 | docs\adr\0015-deprecate-browser-only-dashboard-rendering.md |
| ADR-0016 | Use Server-Side Rendering for Scheduled Report Snapshots | Accepted | 2026-05-02 | data-platform-team | reporting | reporting, dashboard-snapshot, worker | 2026-11-02 | ADR-0015 |  | docs\adr\0016-use-server-side-rendering-for-report-snapshots - Copy.md |
| ADR-0017 | Use Server-Side Rendering for Scheduled Report Snapshots | Accepted | 2026-05-02 | data-platform-team | reporting | reporting, dashboard-snapshot, worker | 2026-11-02 | ADR-0015 |  | docs\adr\0017-use-client-side-rendering-for-report-snapshots.md |

## Git History

| ID | Title | Last Modified | Author | Commit |
| --- | --- | --- | --- | --- |
| ADR-0001 | Use PostgreSQL for Application Metadata | 2026-05-11 | DF | 0f8703c |
| ADR-0002 | Separate Query Execution into a Dedicated Service | 2026-05-11 | DF | 0f8703c |
| ADR-0003 | Use OIDC for User Authentication | 2026-05-11 | DF | 0f8703c |
| ADR-0004 | Use a Semantic Layer for Governed Metrics | 2026-05-11 | DF | 0f8703c |
| ADR-0005 | Support CSV Upload for Small Ad Hoc Datasets | 2026-05-11 | DF | 0f8703c |
| ADR-0006 | Cache Dashboard Query Results | 2026-05-11 | DF | 0f8703c |
| ADR-0007 | Use Hosted LLM Provider for Natural-Language Querying | 2026-05-11 | DF | 0f8703c |
| ADR-0008 | Reject Unrestricted SQL Access for Viewers | 2026-05-11 | DF | 0f8703c |
| ADR-0009 | Use S3-Compatible Object Storage for Uploads and Exports | 2026-05-11 | DF | 0f8703c |
| ADR-0010 | Use OpenTelemetry for Observability Instrumentation | 2026-05-11 | DF | 0f8703c |
| ADR-0011 | Use Durable Workflow Engine for Async Jobs | 2026-05-11 | DF | 0f8703c |
| ADR-0012 | Use Worker Queue for MVP Async Jobs | 2026-05-11 | DF | 0f8703c |
| ADR-0013 | Enforce Row-Level Access Policies in Query Service | 2026-05-11 | DF | 0f8703c |
| ADR-0014 | Use Cloud-Agnostic Container Deployment | 2026-05-11 | DF | 0f8703c |
| ADR-0015 | Deprecate Browser-Only Dashboard Snapshot Rendering | 2026-05-11 | DF | 0f8703c |
| ADR-0016 | Use Server-Side Rendering for Scheduled Report Snapshots |  |  |  |
| ADR-0017 | Use Server-Side Rendering for Scheduled Report Snapshots |  |  |  |

## Decision Timeline

| Date | ID | Title | Status | Owner |
| --- | --- | --- | --- | --- |
| 2026-03-01 | ADR-0001 | Use PostgreSQL for Application Metadata | Accepted | data-platform-team |
| 2026-03-05 | ADR-0002 | Separate Query Execution into a Dedicated Service | Accepted | data-platform-team |
| 2026-03-08 | ADR-0003 | Use OIDC for User Authentication | Accepted | platform-security-team |
| 2026-03-12 | ADR-0004 | Use a Semantic Layer for Governed Metrics | Accepted | data-platform-team |
| 2026-03-15 | ADR-0005 | Support CSV Upload for Small Ad Hoc Datasets | Accepted | data-platform-team |
| 2026-03-20 | ADR-0006 | Cache Dashboard Query Results | Accepted | platform-performance-team |
| 2026-03-25 | ADR-0007 | Use Hosted LLM Provider for Natural-Language Querying | Proposed | data-platform-team |
| 2026-03-27 | ADR-0008 | Reject Unrestricted SQL Access for Viewers | Accepted | platform-security-team |
| 2026-04-01 | ADR-0009 | Use S3-Compatible Object Storage for Uploads and Exports | Accepted | platform-infrastructure-team |
| 2026-04-05 | ADR-0010 | Use OpenTelemetry for Observability Instrumentation | Accepted | platform-observability-team |
| 2026-04-10 | ADR-0011 | Use Durable Workflow Engine for Async Jobs | Rejected | data-platform-team |
| 2026-04-12 | ADR-0012 | Use Worker Queue for MVP Async Jobs | Accepted | data-platform-team |
| 2026-04-18 | ADR-0013 | Enforce Row-Level Access Policies in Query Service | Accepted | platform-security-team |
| 2026-04-22 | ADR-0014 | Use Cloud-Agnostic Container Deployment | Accepted | platform-infrastructure-team |
| 2026-04-30 | ADR-0015 | Deprecate Browser-Only Dashboard Snapshot Rendering | Deprecated | data-platform-team |
| 2026-05-02 | ADR-0016 | Use Server-Side Rendering for Scheduled Report Snapshots | Accepted | data-platform-team |
| 2026-05-02 | ADR-0017 | Use Server-Side Rendering for Scheduled Report Snapshots | Accepted | data-platform-team |
