---
id: design.events-between-contexts
kind: decision
title: Contexts integrate through events
summary: Contexts share changes by publishing events, not by calling each other
status: accepted
date: 2026-11-01
---

# Contexts integrate through events

## Context
Contexts that call each other directly fail together, and every new consumer changes its producer.

## Decision
Contexts publish events when their data changes, and consumers keep what they need.

## Consequences
- `design.event-envelope` states the format of events.
- Consumers handle data that arrives later than the change.

## Alternatives considered
- **Direct calls between contexts:** simpler, but couples their availability.
- **A shared database:** no integration code, but every schema change affects every context.
