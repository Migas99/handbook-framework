---
title: Item metadata and meaningful IDs
status: accepted
date: 2026-11-01
related: [seven-kinds-of-item.md, one-file-per-item.md, domains-by-family-tier-and-topic.md]
---

# Item metadata and meaningful IDs

## Context
Tools generate indexes from items, check their links and resolve overrides; agents decide from them what
to load. Projects that follow a handbook need to say which items they depart from, and pull requests need
to cite the items a change was checked against. All of that needs a stable way to name an item, and
metadata that stores each fact once.

## Decision
Every item carries:

| Field | Holds |
|---|---|
| `id` | `<domain>.<slug>`, such as `quality.test-value`; unique, never reused |
| `kind` | One of the seven kinds |
| `title` | Its name; it can change freely |
| `summary` | What it says, in one line |
| `applies_when` | When an agent should read it, in one line; required for rules, guidelines and procedures |
| `status` | One of the statuses its kind allows |
| `because` | IDs of the principles or decisions that justify it |
| `related` | IDs of related items |

- The domain is derived from the ID's prefix, not stored again.
- Links between items use IDs, not paths.
- A renamed item keeps its old ID in `aliases`, which still resolves, with a warning to update the
  reference.
- Kinds add their own fields: a rule has `enforced_by`; a decision has `date`, `decided_in`, `supersedes`
  and `superseded_by`; a procedure has `command`; a reference has `source`.
- A project overrides an item by its ID, with a reason. Rules cannot be overridden.

## Consequences
- Citations are readable where people and agents see them: in overrides, pull requests and check output.
- Moving or renaming files breaks no link, and renames are covered by aliases.
- IDs must be chosen with care, because they are never reused.

## Alternatives considered
- **Opaque numbers, such as `QUA-012`:** never need renaming, but a citation means nothing without a
  lookup.
- **The file path as identity:** nothing extra to maintain, but moving or splitting a file breaks every
  override and citation.
