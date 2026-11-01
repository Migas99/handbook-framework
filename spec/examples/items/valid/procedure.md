---
id: delivery.open-pull-request
kind: procedure
title: Open a pull request
summary: Open a pull request to the standard, and move its issue to In review
applies_when: The work on a branch is done and ready for review
status: active
command: commands/open-pull-request
---

# Open a pull request

## Outcome
A pull request that closes its issue, with a standard title and description, and the issue In review.

## Before you start
The branch is pushed, and its changes are committed.

## Steps
1. Write the description: `Closes #<issue>`, then Why, What changed and How it was verified.
2. Run `commands/open-pull-request`; its help lists its options.
3. Fix any failing check before asking for review.

## Done when
The pull request is open, its checks pass, and its issue is In review.
