---
id: ADR-0003
title: Use OIDC for User Authentication
status: Accepted
date: 2026-03-08
owner: platform-security-team
application: internal-bi-platform
system: analytics-platform
domain: identity
tags:
  - identity
  - security
  - oidc
review_date: 2026-09-08
supersedes:
superseded_by:
---

# ADR-0003: Use OIDC for User Authentication

## Context

Internal users should authenticate with company-managed identity. The BI application should not manage passwords directly.

## Decision

Use OpenID Connect through the company identity provider.

## Alternatives Considered

- Local username/password authentication.
- SAML-only integration.
- Shared internal reverse proxy authentication without app-level identity context.

## Consequences

Positive:
- Centralized identity lifecycle.
- Supports SSO and MFA.
- Provides consistent user identity claims.

Negative:
- Requires integration testing with the identity provider.
- Requires clear token validation and session handling rules.
