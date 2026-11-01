---
id: delivery.commit-format
kind: rule
title: Commits follow Conventional Commits
summary: Pull request titles and commit subjects are Conventional Commits
applies_when: Writing a commit message or a pull request title
status: active
enforced_by: The Compliance check, step "Title is a Conventional Commit"
because: [delivery.versions-from-history]
---

# Commits follow Conventional Commits

## Rule
Pull request titles and commit subjects follow Conventional Commits: `<type>(<scope>): <description>`,
lowercase, imperative, without a trailing period.

## Reason
Squash merging makes the title the commit on `main`, and versions and the changelog are derived from
those commits.

## When it fails
Rewrite the title as `<type>(<scope>): <description>`, using a type from the list in the check's
message.

## Examples
- `feat(check): report stale generated files`
- `fix: accept aliases in related`
