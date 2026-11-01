# Writing a reference

A reference holds facts that are looked up, such as registries, glossaries and tables
([kinds of item](../concepts/kinds-of-item.md)).

## When to use it
When a set of facts is consulted rather than followed. Facts that several items or tools rely on are kept
as data in `data/`, and the reference names that table in `source`; its facts are then generated from it.
Facts used in one place only are written inline.

## Writing it
- **Frontmatter:** the common fields. `applies_when` is optional; `source` names the table under `data/`
  when the facts are generated.
- **About:** what the facts are, and how they are kept current.
- **Facts:** the facts, generated from `source` or written inline.

## Worked example

````markdown
---
id: delivery.priorities
kind: reference
title: Priorities
summary: What each priority of a work item means
status: active
---

# Priorities

## About
The priorities a work item can have. Every issue has one once it is Ready.

## Facts
| Priority | Means |
|---|---|
| P0 | Drop everything |
| P1 | Next up |
| P2 | Planned |
| P3 | Someday |
````
