---
title: Apache-2.0, with a NOTICE
status: accepted
date: 2026-11-01
related: [public-and-depending-on-no-instance.md]
---

# Apache-2.0, with a NOTICE

## Context
Anyone must be able to use the framework, for any purpose and free of charge, while it stays clear who
built it. The framework also generates files inside other owners' handbooks.

## Decision
- The framework is licensed under the Apache License, Version 2.0.
- `NOTICE` names its author: `Copyright 2026 José Cunha`.
- The README states that files the `handbook` command generates in a handbook belong to whoever generated
  them.

## Consequences
- Use, modification and redistribution are free; redistributions keep the copyright notices, the license
  and the `NOTICE`.
- The license grants no use of the author's name for endorsement, and includes a patent grant.
- Plain use requires no credit, as with every mainstream open-source license.
- Handbooks need not carry the framework's `NOTICE` for what it generates.

## Alternatives considered
- **MIT:** just as free, but credit is only a copyright line, with no `NOTICE` and no patent grant.
- **A license requiring visible credit in every product that uses it:** rare, and it discourages adoption.
- **Creative Commons:** suits written content, not software.
