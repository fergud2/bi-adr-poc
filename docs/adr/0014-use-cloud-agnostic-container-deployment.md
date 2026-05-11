---
id: ADR-0014
title: Use Cloud-Agnostic Container Deployment
status: Accepted
date: 2026-04-22
owner: platform-infrastructure-team
application: internal-bi-platform
system: analytics-platform
domain: infrastructure
tags:
  - containers
  - kubernetes
  - cloud-agnostic
review_date: 2026-10-22
supersedes:
superseded_by:
---

# ADR-0014: Use Cloud-Agnostic Container Deployment

## Context

The platform should be deployable to different cloud environments without tightly coupling the architecture to one provider.

## Decision

Package the Web App, Backend API, Query Service, NL Query Service, and Worker Service as containers. Prefer Kubernetes or an equivalent container runtime managed by the platform team.

## Alternatives Considered

- Serverless functions for all components.
- Single virtual machine deployment.
- Single monolithic container.

## Consequences

Positive:
- Portable deployment model.
- Independent scaling of services.
- Compatible with common enterprise platform practices.

Negative:
- Requires container orchestration operational capability.
- Adds deployment complexity compared with a monolith.
