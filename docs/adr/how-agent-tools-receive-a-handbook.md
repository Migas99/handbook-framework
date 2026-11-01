---
title: How agent tools receive a handbook
status: accepted
date: 2026-11-01
related: [seven-kinds-of-item.md, one-instance-per-workspace.md, standards-first-with-bridge-adapters.md, optional-read-only-mcp-server.md, always-on-usage-is-reported-not-capped.md]
---

# How agent tools receive a handbook

## Context
A handbook only helps if its items reach agents at the right moment, through any agent tool. Research on
repository instruction files (Gloaguen et al., "Evaluating AGENTS.md", arXiv:2602.11988) found that
always-loaded files raise the cost of every task and help little unless they state what differs from a
model's defaults. Routing that depends on an agent choosing to read an index is the weakest link.

## Decision
`handbook install` delivers a handbook through open standards:

- **The always-on core:** principles and working agreements, with a short guide to the handbook, in
  `AGENTS.md`.
- **One skill per enabled domain,** in the open Agent Skills format: its description is built from its
  items' `applies_when`, and its body holds the domain's items. A domain too large for one description is
  split into several skills.
- **One skill per procedure,** named `<prefix>-<id>`, with `applies_when` as its description.
- **Rules through their checks:** a failing check cites the rule's ID, and the agent loads that item.
- **An index** of every item, with its summary and `applies_when`, for people and for tools without
  skills.
- **An adapter table** in the framework, the only place where agent tools are named: where each reads
  instructions and skills, from which pointers and links are generated.

## Consequences
- Routing is the tool's job, through skill descriptions, rather than the agent remembering to read an
  index.
- Only the core and the skill descriptions are always in context.
- Supporting another agent tool means one more adapter row, with no content change.
- The generator has to write descriptions that summarize a whole domain well.

## Alternatives considered
- **Index first:** the core tells the agent to read the index and load what applies; works anywhere, but
  depends on the agent following it.
- **One skill per item:** the most precise triggering, but dozens or hundreds of descriptions stay in
  context and compete with each other.
