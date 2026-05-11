---
id: ADR-0007
title: Use Hosted LLM Provider for Natural-Language Querying
status: Proposed
date: 2026-03-25
owner: data-platform-team
application: internal-bi-platform
system: analytics-platform
domain: ai
tags:
  - llm
  - nl-query
  - ai
  - security
review_date: 2026-06-25
supersedes:
superseded_by:
---

# ADR-0007: Use Hosted LLM Provider for Natural-Language Querying

## Context

Business users want to ask natural-language questions over governed datasets. Building and operating a custom LLM is out of scope for the MVP.

## Decision

Use a hosted LLM provider through an internal gateway. The gateway will control prompts, provider configuration, rate limits, audit logging, and data minimization.

## Alternatives Considered

- Build a custom LLM.
- Disable natural-language querying for MVP.
- Use only keyword search over dashboards.

## Consequences

Positive:
- Faster time to market.
- Better language quality than a custom MVP model.
- Provider can be changed behind the gateway.

Negative:
- Requires legal/security review.
- Requires strict controls over prompt content.
- Requires monitoring for unsafe SQL generation.
