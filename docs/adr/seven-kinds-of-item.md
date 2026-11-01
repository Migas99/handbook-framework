---
title: Seven kinds of item
status: accepted
date: 2026-11-01
related: [item-metadata-and-meaningful-ids.md, fixed-body-sections-per-kind.md, how-agent-tools-receive-a-handbook.md]
---

# Seven kinds of item

## Context
A handbook mixes statements that bind differently: values, requirements, defaults, steps, facts and the
history of choices. When how binding a statement is depends on where it sits, people and agents have to
guess, and advice written as rules goes unchecked. Agents also follow what they read: every statement
they load costs context, and helps only when it says something they would not do by default.

## Decision
Every item has exactly one kind, and its kind fixes how binding it is, when it is loaded, its template,
its statuses and what it must link to:

| Kind | What it is | How binding | Loaded |
|---|---|---|---|
| Principle | A value that guides judgment where nothing more specific applies | Always applies; applied with judgment | Always |
| Working agreement | How an agent behaves while working with the owner | Non-negotiable; no tool can check it | Always |
| Rule | A requirement that a check, hook or permission enforces | Non-negotiable; the tool is the backstop | When it applies |
| Guideline | A default, with its reason | Followed unless a case calls for otherwise, with the reason stated | When it applies |
| Procedure | Steps to reach a result | Followed when doing that task | As a skill |
| Reference | Facts that are looked up | Facts | On lookup |
| Decision | A choice among alternatives at a point in time | Explains why; never instructs | When asking why |

Classifying a statement takes the first answer that is yes: a choice with alternatives is a decision;
steps to a result are a procedure; facts that are looked up are a reference; something binding without
exceptions is a rule when a tool can enforce it and a working agreement when none can; a default with a
reason is a guideline; a value that guides judgment is a principle.

- A decision never carries instructions: a decision that changes behavior creates or updates the item that
  states it, and that item links back.
- A rule names what enforces it. Without enforcement, it is a guideline.
- Anything binding states its reason, or links to the principle or decision that gives it.
- Only principles and working agreements are always loaded.

## Consequences
- How binding a statement is, and when it reaches an agent, follows from one field.
- The always-loaded part of a handbook stays small and limited to two kinds.
- Authors have seven kinds to learn, and classify each statement.

## Alternatives considered
- **Six kinds, with working agreements as rules enforced by agreement:** one kind fewer, but "rule" would
  mean two things that load differently, and rules nothing checks would drift.
- **Two separate fields, form and strength (must, should, value):** flexible, but some combinations make
  no sense, and loading and templates would depend on two fields.
