---
title: Semantic versioning, migrations, and 0.x until first adoption
status: accepted
date: 2026-11-01
related: [prebuilt-binaries-launcher-and-lock-file.md, depends-only-on-git-and-a-command-line.md, how-this-repository-operates.md]
---

# Semantic versioning, migrations, and 0.x until first adoption

## Context
Owners decide when to upgrade by changing the version their handbook pins. The version number has to tell
them what an upgrade costs. The framework keeps three things stable for them: the spec, the command, and
the generated files that handbooks commit or install. It has one maintainer.

## Decision

| Version | Means |
|---|---|
| Major | A valid handbook becomes invalid, or existing content changes meaning |
| Minor | Additions: every existing handbook stays valid and means the same |
| Patch | Fixes |

- Anything removed in a major version is first deprecated in a minor one, and `handbook check` warns
  about it.
- Every major version ships its migration in `handbook upgrade`, chained across versions. What needs
  judgment is not guessed: the upgrade stops and lists the items by ID.
- Versions start at `0.x`, where minor versions may break things, until the first handbook has adopted
  the framework and the spec has settled; then `1.0`.
- Only the latest major version receives fixes.
- Every release has a changelog, with upgrade notes listing migrations and what needs judgment.

## Consequences
- The number alone tells an owner what an upgrade costs.
- Upgrading is mechanical, which makes staying on an old version unnecessary.
- There is one line of releases to maintain.

## Alternatives considered
- **Long-term support for the previous major version:** gentler for slow upgraders, but doubles
  maintenance, with little reason to stay behind when migrations are mechanical.
- **Calendar versions:** show how recent a release is, but not whether an upgrade breaks anything.
