---
title: Fixed body sections per kind
status: accepted
date: 2026-11-01
related: [seven-kinds-of-item.md, one-file-per-item.md]
---

# Fixed body sections per kind

## Context
What agents read is generated from parts of items: the always-on core from agreements and their reasons,
domain skills from guidelines and rules. Free-form bodies cannot be taken apart, and their quality varies
by author: in an earlier project, a fifth of the decision records had no alternatives, because nothing
required them.

## Decision
Each kind has fixed sections, in a fixed order. `handbook check` validates the required ones, marked here
without an asterisk:

| Kind | Sections |
|---|---|
| Principle | Principle · Reason · In practice* |
| Working agreement | Agreement · Reason |
| Rule | Rule · Reason · When it fails · Examples* |
| Guideline | Guideline · Reason · Examples* |
| Procedure | Outcome · Before you start · Steps · Done when |
| Reference | About · the facts, generated from `source` or written inline |
| Decision | Context · Decision · Consequences · Alternatives considered |

- A rule's *When it fails* says how to comply, because an agent usually opens a rule after a check cites
  it.
- A procedure's mechanical steps name its command and point to the command's help, without copying it.
- A decision's *Consequences* names, by ID, the items it created or changed, and validation checks they
  exist.

## Consequences
- The generator takes exactly the parts each view needs.
- Every item meets a minimum, and authors know what to write.
- Very small items carry a little structure.

## Alternatives considered
- **Free-form bodies, with only the metadata fixed:** the most flexible, but parts cannot be extracted and
  quality varies.
- **One skeleton for every kind:** uniform, but procedures and decisions do not fit it.
