---
title: Depends only on git and a command line; the version is pinned only in handbook.toml
status: accepted
date: 2026-11-01
related: [written-in-go.md, prebuilt-binaries-launcher-and-lock-file.md, semantic-versioning-and-migrations.md, how-this-repository-operates.md]
---

# Depends only on git and a command line; the version is pinned only in handbook.toml

## Context
The framework must not depend on any agent provider, and for the same reason on any git host or CI
system. Owners use different hosts and CI systems, and a framework that ships code for one of them ties
every owner to it. The version a handbook uses must also be the same for every caller: people, agents,
hooks and CI.

## Decision
- The framework needs only git and a command line. Its contract is the `handbook` command, with its
  subcommands, exit codes and JSON output.
- The framework ships no code for a CI system. Any CI system runs `handbook check`; the documentation
  shows the call for common ones.
- Releases are git tags.
- The framework version a handbook uses is written only in `handbook.toml`, and every caller runs exactly
  that version.

## Consequences
- Moving a handbook to another host or CI system changes nothing in the framework.
- Each owner writes the few lines that call `handbook check` in their CI system.
- How every caller runs the pinned version is decided by the distribution.
- The repository where the framework is developed may still use its host's features; this applies to the
  product.

## Alternatives considered
- **A reusable CI workflow for one host:** saves a few lines, but ties the framework to that host.
- **Optional CI adapters per host:** quicker to adopt, but a maintained surface per host for little gain,
  since the call does not vary.
- **The version pinned in several files** (the handbook's configuration, a tool manager and the CI
  workflow): copies of one fact that drift.
