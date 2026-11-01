# Writing a procedure

A procedure is the steps to reach a result. Its mechanical steps belong in a command, which does them the
same way every time; its judgment belongs in its text ([kinds of item](../concepts/kinds-of-item.md)).
Every procedure becomes a skill of its own.

## When to use it
When a task recurs and is done in a particular way. A step that can be scripted goes in the procedure's
command; the procedure names it.

## Writing it
- **Frontmatter:** the common fields, plus `applies_when`, which becomes the skill's description: name the
  moment the procedure is needed. `command` names the command, if there is one.
- **Outcome:** what exists when the procedure is done.
- **Before you start:** what must already be true.
- **Steps:** numbered. A mechanical step runs the command and points to its help rather than repeating it;
  a judgment step says what to decide and how.
- **Done when:** how to tell the outcome was reached.

## Worked example

````markdown
---
id: delivery.start-work-on-an-issue
kind: procedure
title: Start work on an issue
summary: Take a ready issue, set it in progress and create its branch
applies_when: About to start working on an issue
status: active
command: commands/start-work
---

# Start work on an issue

## Outcome
The issue is assigned and In progress, and a branch for it exists.

## Before you start
The issue is Ready. If it is not, say what is missing instead of starting.

## Steps
1. Decide the branch's type from the change: `feat`, `fix`, `docs` or another Conventional Commit type.
2. Run `commands/start-work` with the issue and the type; its help lists the options.

## Done when
The issue is In progress and assigned, and you are on its branch.
````
