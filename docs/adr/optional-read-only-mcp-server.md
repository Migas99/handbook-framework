---
title: An optional, read-only MCP server
status: accepted
date: 2026-11-01
related: [how-agent-tools-receive-a-handbook.md, one-instance-per-workspace.md, semantic-versioning-and-migrations.md]
---

# An optional, read-only MCP server

## Context
Some agents have no workspace and no copy of a handbook: cloud agents, chat assistants and web tools.
Some questions are also structured: an item by its ID, the reasons behind it, everything of one kind or
status, the overrides in a project. The Model Context Protocol is an open standard that agent tools
widely support.

## Decision
- `handbook serve` is a read-only MCP server: over stdio for local work, over HTTP for hosting.
- Items are resources, such as `handbook://quality.test-value`; queries are tools; procedures are prompts.
- It complements the core, the skills and the index, and replaces none of them.
- Its tool names and parameters are part of what versioning keeps stable.
- It listens only locally unless told otherwise. A hosted server is protected by whatever its owner puts in
  front of it.
- `handbook install` registers it per workspace, through a field of the adapter table.
- It ships in a `0.x` minor version, after the core, the skills and the index work.

## Consequences
- Agents without a workspace can use a handbook, and structured questions are answered in one call.
- Its tool definitions are in context like skill descriptions, so it keeps to a few tools.
- Changes to a handbook still go through git and review.

## Alternatives considered
- **The main channel, replacing skills and the index:** one interface, but it cannot deliver the always-on
  core reliably, and routing would depend on the agent calling it.
- **Left to each handbook to build:** a smaller framework, but every owner would build the same server
  differently.
