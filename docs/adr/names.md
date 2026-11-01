---
title: "Names: handbook, handbook-framework, the handbook command and handbook.toml"
status: accepted
date: 2026-11-01
related: [one-framework-repository-and-one-per-instance.md, procedures-are-items.md]
---

# Names: handbook, handbook-framework, the handbook command and handbook.toml

## Context
The names appear everywhere: in repositories, commands, configuration and documentation, for people and
for organizations. They need to be explicit and plain, cover both families of knowledge and every kind of
item, and name no agent tool. Two words the framework already uses for other things, the always-on
"core" and the "spec", must not be reused.

## Decision
- An instance's repository is a **handbook**, named `handbook` by default. Its procedures are its
  **playbook**, a part of the handbook.
- The framework's repository is **`handbook-framework`**.
- The command is **`handbook`**: `handbook check`, `handbook build`, `handbook install`.
- An instance's configuration is **`handbook.toml`**.

## Consequences
- A handbook reads naturally for anyone ("my handbook", "the organization's handbook"), and covers how
  an owner works as well as what they build.
- The repository name is long, but people type the command, not the repository.

## Alternatives considered
- **`baseline` for the instance:** names its purpose, but says little about its content, and already
  means other things in engineering.
- **`ways-of-working` or `operating-manual`:** describe practice, but fit the system family and decisions
  poorly.
- **A metaphor, such as `compass` or `canon`:** memorable, but opaque to newcomers.
- **`handbook-kit`, `handbook-tools` or a brand name for the framework:** a kit suggests a template to
  copy, tools hides the spec, and a brand says nothing to a newcomer.
