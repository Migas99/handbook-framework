---
title: Public, and depending on no instance
status: accepted
date: 2026-11-01
related: [one-framework-repository-and-one-per-instance.md, apache-2-license.md, no-starter-content.md]
---

# Public, and depending on no instance

## Context
Other owners must be able to read the framework from their own machines and CI, often with credentials
limited to their own organization. A private framework under one account would be out of their reach. The
framework must also stay neutral: anything it takes from one instance would carry that instance's history,
naming or privacy into every other.

## Decision
- The framework is public, at `Migas99/handbook-framework`.
- Dependencies point one way: instances depend on the framework, never the reverse. The framework does
  not link to, name, take examples from or test against any instance.
- Its examples and test fixtures are self-contained, in this repository.

## Consequences
- Any owner can install and check against the framework without access arrangements.
- Changes an instance needs arrive through a framework release, which keeps the boundary explicit.
- Examples are written for the documentation rather than taken from real handbooks.

## Alternatives considered
- **In an organization that uses it, public:** developed next to its first user, but that user would shape
  the spec day to day.
- **In an organization that uses it, private:** works for that organization only, which contradicts the
  aim of any owner having a handbook.
- **Linking to a real handbook as the reference example:** a living example, but it would make the
  framework depend on an instance.
