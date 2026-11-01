---
title: Always-on usage is reported, not capped
status: accepted
date: 2026-11-01
related: [how-agent-tools-receive-a-handbook.md, seven-kinds-of-item.md]
---

# Always-on usage is reported, not capped

## Context
The always-on core and the skill descriptions are in every agent's context, on every task. Their size is
a cost on every task, and owners need to see it to keep it in check. Token counts differ between
providers.

## Decision
- `handbook check` reports the size of the always-on core in words, and warns when it grows large. There
  is no hard cap.
- The core counts the Principle, Agreement and Reason sections. The framework's own guide to the handbook
  has a fixed size and is not counted.
- Words are counted, not tokens, so the result is the same for every provider.
- Skill descriptions keep within the Agent Skills format's own limit; a domain whose description would
  exceed it is split into several skills.

## Consequences
- Owners always see the size of what they make always-on.
- Nothing stops a core from growing, so discipline is the owner's.

## Alternatives considered
- **A default cap that a handbook can raise up to a maximum:** enforces discipline, with room for larger
  organizations.
- **One fixed cap for everyone:** the strongest discipline, but one number cannot fit a person and an
  organization alike.
