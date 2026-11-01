---
title: One instance per workspace, nothing installed user-wide
status: accepted
date: 2026-11-01
related: [how-agent-tools-receive-a-handbook.md, standards-first-with-bridge-adapters.md]
---

# One instance per workspace, nothing installed user-wide

## Context
A person can work for several owners on the same machine, for example on an organization's work in one
directory and on personal projects in another. Each context must follow only its own owner's handbook.
Anything installed for the whole user, such as skills in a user-wide folder, is visible in every context,
and combining two handbooks would make one owner's defaults look like another's decisions.

## Decision
- One context follows one handbook. Handbooks are never merged or layered.
- Everything `handbook install` writes lands in a **workspace directory**, and applies to everything below
  it: the local copy of the handbook, the generated `AGENTS.md`, compatibility pointers, skills and
  environment settings. Nothing is installed user-wide.
- `handbook install` refuses a second handbook in a workspace, or in a directory above or below one.

## Consequences
- Contexts that share a machine stay separate.
- No precedence rules between handbooks are needed.
- Adapters must make each agent tool see only the workspace's handbook: through instruction files in
  parent directories, pointers in each repository, or a configuration home per workspace.

## Alternatives considered
- **One handbook per environment** (machine, container or user): simplest, but only holds while contexts
  never share an environment, and breaks silently when they do.
- **One handbook per repository:** visible to every tool, but every repository needs the setup, and a new
  one is unscoped until someone adds it.
- **Merging handbooks, with the project's winning on conflicts:** one owner's defaults would fill the
  other's gaps, presenting undecided questions as decided.
