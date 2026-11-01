# Writing a decision

A decision records a choice among alternatives at a point in time, with its context
([kinds of item](../concepts/kinds-of-item.md)). It explains why, and never instructs: what people and
agents do because of it is stated in the items it created or changed. An accepted decision is never edited;
a later decision supersedes it.

## When to use it
When a choice shapes the structure of a system or an organization, sets a contract others depend on,
chooses a language, tool or platform, changes a way of working, or is costly to reverse.

## Writing it
- **Frontmatter:** the common fields, plus `date`. `decided_in` says where it was discussed;
  `supersedes` names the decisions it replaces.
- **Context:** the situation, the forces in tension and the constraints.
- **Decision:** the decision, stated directly.
- **Consequences:** what becomes easier and harder, and, by ID, the items the decision created or changed.
- **Alternatives considered:** each option rejected, with its reason, so it is not proposed again.

## Worked example

````markdown
---
id: design.rest-at-the-edge
kind: decision
title: REST at the edge
summary: Clients reach the system through REST APIs described in OpenAPI
status: accepted
date: 2026-11-01
decided_in: The design discussion of the first release
---

# REST at the edge

## Context
Clients are web and mobile applications, written by different teams. They need an interface that every
language and tool supports, and that can be described and checked.

## Decision
Clients reach the system through REST APIs over HTTPS, each described in OpenAPI.

## Consequences
- `design.api-errors` and `design.api-pagination` state how errors and pagination work.
- Every API has a description that client code can be generated from.
- Streaming needs a separate mechanism.

## Alternatives considered
- **GraphQL:** flexible queries, but caching and per-field authorization are harder.
- **gRPC to clients:** compact and typed, but poorly supported in browsers.
````
