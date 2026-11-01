---
title: No starter content; examples live in the documentation
status: accepted
date: 2026-11-01
related: [one-framework-repository-and-one-per-instance.md, public-and-depending-on-no-instance.md]
---

# No starter content; examples live in the documentation

## Context
The framework holds no opinions, yet a new handbook starting empty is a blank page. Starter content would
be opinions under another name. What helps most is what differs from a model's defaults, which is best
gathered from real corrections, not inherited.

## Decision
- `handbook init` creates `handbook.toml`, the folders of the core domains and the generated `meta` items,
  and nothing else.
- The documentation explains each kind with worked examples. They illustrate the spec; no handbook
  inherits them.

## Consequences
- Every item in a handbook was put there on purpose.
- A new handbook starts nearly empty.
- Copying chosen items from another handbook, once, can be added later without changing anything else.

## Alternatives considered
- **Copying from any handbook at init:** a quick start, but copied items arrive without the reasons
  behind them. It remains possible later.
- **Built-in defaults that handbooks inherit:** the fastest start, but it makes the framework opinionated
  and brings back inheritance between handbooks.
