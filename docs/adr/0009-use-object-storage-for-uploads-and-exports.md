---
id: ADR-0009
title: Use S3-Compatible Object Storage for Uploads and Exports
status: Accepted
date: 2026-04-01
owner: platform-infrastructure-team
application: internal-bi-platform
system: analytics-platform
domain: infrastructure
tags:
  - object-storage
  - csv
  - exports
review_date: 2026-10-01
supersedes:
superseded_by:
---

# ADR-0009: Use S3-Compatible Object Storage for Uploads and Exports

## Context

The platform needs to store uploaded CSV files, generated dashboard snapshots, and exported artifacts.

## Decision

Use S3-compatible object storage with signed upload URLs and lifecycle policies.

## Alternatives Considered

- Store files on application server disk.
- Store files directly in PostgreSQL.
- Use a shared network file system.

## Consequences

Positive:
- Cloud-agnostic storage abstraction.
- Scales independently from application services.
- Supports lifecycle and retention policies.

Negative:
- Requires secure bucket/container policies.
- Requires cleanup for failed imports and expired exports.
