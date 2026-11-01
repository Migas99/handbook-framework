# Writing a guideline

A guideline is a default, with its reason ([kinds of item](../concepts/kinds-of-item.md)). It is followed
unless a case calls for something else, and then the reason is given.

## When to use it
When you have a preferred way of doing something that a case may reasonably depart from, or a requirement
no tool enforces yet.

## Writing it
- **Frontmatter:** the common fields, plus `applies_when`, which decides when an agent reads it: name the
  task, in the words an agent would use for it.
- **Guideline:** the default, stated directly.
- **Reason:** why it is the default. The reason is what lets an agent judge when departing is justified.
- **Examples** (optional): the preferred form, shown.

## Worked example

````markdown
---
id: quality.test-through-public-behavior
kind: guideline
title: Test through public behavior
summary: Tests exercise use cases and public interfaces, not private functions
applies_when: Writing or changing tests
status: active
because: [quality.tests-earn-their-place]
---

# Test through public behavior

## Guideline
Tests exercise the use cases and public interfaces of a component, and assert outcomes.

## Reason
Tests of private functions break on every refactor that keeps behavior the same, and protect nothing a
user relies on.

## Examples
- A test publishes a work through its use case and checks it is listed, rather than calling the
  validation helper directly.
````
