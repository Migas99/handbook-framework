---
title: "Domains: families, tiers, organized by topic"
status: accepted
date: 2026-11-01
related: [item-metadata-and-meaningful-ids.md, how-agent-tools-receive-a-handbook.md]
---

# Domains: families, tiers, organized by topic

## Context
When an agent loads an item is already decided by its `applies_when`, so domains do not route. They
organize: where an author puts an item, where a reader finds it, and what an ID's prefix means. Different
owners need different domains, yet tooling and readers need some to be the same in every handbook.
Knowledge about how an owner works also differs from knowledge about one system they build.

## Decision
- Domains are organized by topic, flat, and every item belongs to exactly one.
- Each domain belongs to a **family**: **practice** (how we work and build) or **system** (what one
  particular system is).
- Each domain has a **tier**: **core** domains exist in every handbook; **standard** domains are defined
  by the framework and enabled per handbook; **extension** domains are defined by the handbook itself,
  with a code, a family, a definition and a membership test.

| Tier | Practice | System |
|---|---|---|
| Core | `meta`, `collaboration`, `delivery`, `quality`, `knowledge` | |
| Standard | `design`, `code`, `languages`, `security`, `environment`, `operations` | `product`, `domain-model`, `architecture` |

- When two membership tests pass, the more specific domain wins: `languages`, then `security`, then the
  order above.
- Extensions cannot reuse a framework domain's code.

## Consequences
- Every handbook shares the core and standard domains, so tooling and readers know what to expect.
- A personal handbook mostly enables practice domains; an organization building a product also enables
  the system ones.
- A few topics touch two domains, which the tie-break order settles.

## Alternatives considered
- **Domains by moment in the lifecycle (plan, build, verify, ship, run):** matches the agent's moment, but
  `applies_when` already does that, topics would split across moments, and authors look up by topic.
- **Only core domains in the framework:** the most neutral, but every handbook would redefine the common
  domains, and tooling could assume nothing beyond the core.
