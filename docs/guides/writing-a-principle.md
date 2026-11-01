# Writing a principle

A principle is a value that guides judgment where nothing more specific applies
([kinds of item](../concepts/kinds-of-item.md)). Principles are always in an agent's context, so a handbook
has few of them, each short.

## When to use it
When a value shapes many decisions and you want an agent to apply it to cases no item names. A value that
applies to one kind of task only is usually a guideline instead.

## Writing it
- **Frontmatter:** the common fields. A principle has no `applies_when`, because it always applies.
- **Principle:** the value, in one or two sentences, stated so it can be applied.
- **Reason:** why it matters to you. The reason is what lets an agent generalize from it.
- **In practice** (optional): one to three short cases that show it guiding a judgment.

## Worked example

````markdown
---
id: knowledge.one-source-per-fact
kind: principle
title: One source per fact
summary: Every fact is written in one place; everywhere else links to it or is generated from it
status: active
---

# One source per fact

## Principle
Every fact is written in exactly one place. Everywhere else links to it, or is generated from it.

## Reason
Copies drift, because nothing tells the person changing one copy that another exists.

## In practice
- A README that needs the list of supported versions links to where the list is kept.
- A table derived from data is generated, and a check fails when it is out of date.
````
