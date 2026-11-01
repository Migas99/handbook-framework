---
title: One framework repository, and one repository per instance
status: accepted
date: 2026-11-01
related: [public-and-depending-on-no-instance.md, procedures-are-items.md, names.md]
---

# One framework repository, and one repository per instance

## Context
A handbook is the baseline that agents follow for a person or an organization. Each owner needs their
own, with their own content, and the owners must not depend on each other. What a handbook is, and the
tools that check and deliver it, are the same for every owner. If the definition and the tools are copied
into each handbook, every copy drifts, and fixes have to be ported by hand.

## Decision
- The framework is one repository: the spec, which defines what a handbook is, and the tooling. It holds
  no opinions and names no owner.
- Each owner's handbook, an instance, is its own repository, and pins a version of the framework.
- An instance supplies its identity through its configuration: its name, its prefix, the domains it
  enables and where it lives.

## Consequences
- Spec and tooling are fixed once, released, and reach every instance through a version bump.
- Instance content never mixes with the framework or with other instances.
- The framework must stay free of opinions, so anything an owner prefers belongs in their instance.
- Starting means two repositories: the framework, and the first instance.

## Alternatives considered
- **A template repository copied for each instance:** simple to start, but every copy diverges and spec or
  tooling fixes must be ported by hand.
- **One owner's instance that is also the framework:** one repository, but that owner's opinions mix with
  the neutral spec, and every other instance inherits or strips them.
