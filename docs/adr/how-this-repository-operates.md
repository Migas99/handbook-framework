---
title: How this repository operates
status: accepted
date: 2026-11-01
related: [depends-only-on-git-and-a-command-line.md, semantic-versioning-and-migrations.md, public-and-depending-on-no-instance.md]
---

# How this repository operates

## Context
The framework is built in many steps, by its maintainer and by agents, in a public repository hosted on
GitHub. Its product must not depend on a host, but the repository's own development can use the host it
lives on. How work is done on the framework belongs to the project: if it lived in its maintainer's
handbook, which depends on the framework, the framework's development would depend on one of its own
instances, and outside contributors would need that handbook to contribute.

## Decision
- The ways of working live in this repository: [CONTRIBUTING.md](../../CONTRIBUTING.md) for everyone, and
  [AGENTS.md](../../AGENTS.md) for the strict rules and what agents do at each step. No handbook governs
  this repository.
- The repository uses its host's features: issue forms with labels, features with task sub-issues, a
  project with Status and Priority, a ruleset on `main`, and its own CI.
- Every change starts from an issue and reaches `main` through a squash-merged pull request whose checks
  pass.
- **Trunk-based:** one `main`, always releasable. A release is an annotated tag on `main`; a pre-release
  tag can be tried first.
- Releases are prepared from Conventional Commits by Release Please: merging its release pull request
  creates the tag, and the tag builds the binaries and checksums.
- The Compliance check is a Python script using only the standard library.

## Consequences
- Outside contributors find everything they need in the repository.
- The ways of working change through pull requests here, and its history explains them.
- Only tagged commits are releases, and owners choose when to adopt one.

## Alternatives considered
- **The ways of working in the maintainer's handbook:** one place for all their repositories, but a
  dependency from the framework's development on one of its instances.
- **Development and production branches, with release and hotfix branches:** suits batched releases,
  several supported versions or branches that map to environments; none of these applies.
- **Tagging releases by hand:** pure git, but more manual.
- **The Compliance check in Go:** one language in the repository, but more code for the same rules, and a
  toolchain to set up in CI.
