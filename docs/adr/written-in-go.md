---
title: Written in Go
status: accepted
date: 2026-11-01
related: [depends-only-on-git-and-a-command-line.md, prebuilt-binaries-launcher-and-lock-file.md]
---

# Written in Go

## Context
The tooling reads Markdown frontmatter, YAML and TOML, validates them against schemas, generates files,
writes workspace files and runs migrations. It runs for every owner, in any CI system and in git hooks,
and must depend only on git and a command line. Whatever it needs installed is a cost for every adopter.

## Decision
The `handbook` command is written in Go and distributed as one binary per platform.

## Consequences
- Adopters install no runtime; hooks start fast; cross-compiling is simple.
- Text processing takes more code than in a scripting language.
- The documentation generator of an earlier project, written in Python, is not reused.

## Alternatives considered
- **Python:** quickest to write and could adapt existing code, but every adopter needs Python and its
  package tooling in every environment, CI included, and hooks start more slowly.
- **TypeScript:** a good Markdown ecosystem, but it needs Node everywhere and adds a language.
