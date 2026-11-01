---
title: One file per item, and no global decision numbers
status: accepted
date: 2026-11-01
related: [item-metadata-and-meaningful-ids.md, fixed-body-sections-per-kind.md]
---

# One file per item, and no global decision numbers

## Context
Items range from a rule of three lines to a decision of a page, and each carries its own metadata. Agents
mostly read what is generated from items, so the storage format serves authors, reviews, history and
validation.

## Decision
- Each item is one Markdown file, `<domain>/<slug>.md`, with its metadata as frontmatter. The path follows
  the ID, and validation checks that they match.
- Readable pages per domain are generated from the files.
- Decisions live in their domain's folder like any other item, without a global number. The chronological
  log of decisions is generated, sorted by date.

## Consequences
- Metadata uses standard frontmatter, with no custom parsing.
- Each item has its own history, status and review, and overrides and checks work per file.
- A full handbook has many small files, readable through the generated pages.
- Parallel branches never compete for the next decision number.

## Alternatives considered
- **One page per domain, with items as sections:** fewer files, but metadata inside sections needs a
  custom format, and busy pages conflict.
- **Pages per domain for small kinds, files for decisions and procedures:** two ways to author and to
  parse.
- **Every item as data in YAML tables:** prose, examples and code inside YAML strings are hard to write
  and review.
- **A global decision number:** familiar, but a second identifier next to the ID, and a source of
  conflicts.
