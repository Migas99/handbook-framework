# Writing a rule

A rule is a requirement that a check, hook or permission enforces
([kinds of item](../concepts/kinds-of-item.md)). An agent usually opens a rule because a check failed and
cited the rule's ID, so the rule says how to comply.

## When to use it
When a requirement has no exceptions and a tool enforces it. If no tool enforces it yet, write a guideline,
and turn it into a rule once the check exists.

## Writing it
- **Frontmatter:** the common fields, plus `applies_when` and `enforced_by`, which names the check, hook or
  permission as people see it.
- **Rule:** the requirement, precisely.
- **Reason:** why the requirement exists.
- **When it fails:** what to do when the check fails, in steps the agent can follow.
- **Examples** (optional): what passes.

## Worked example

````markdown
---
id: delivery.changes-through-pull-requests
kind: rule
title: Changes reach main through pull requests
summary: Nothing is pushed to main directly; every change is a reviewed pull request
applies_when: Pushing a change, or finishing work on a branch
status: active
enforced_by: The ruleset on main
---

# Changes reach main through pull requests

## Rule
Every change reaches `main` through a pull request whose checks pass. Nothing is pushed to `main`
directly.

## Reason
`main` is always releasable, and review and checks are how a change earns its place there.

## When it fails
1. Push the commits to a branch named after the issue.
2. Open a pull request for it, and fix any failing check.

## Examples
- A branch `feat/12-check-command`, merged through its pull request.
````
