# Writing a working agreement

A working agreement says how an agent behaves while working with the owner. It is non-negotiable, and no
tool can check it ([kinds of item](../concepts/kinds-of-item.md)). Agreements are always in an agent's
context, so each is short.

## When to use it
When you want an agent to behave a certain way with you every time, and a check, hook or permission cannot
enforce it. If a tool can enforce it, write a rule instead.

## Writing it
- **Frontmatter:** the common fields. An agreement has no `applies_when`, because it always applies.
- **Agreement:** what to do, stated positively and precisely enough to follow without asking.
- **Reason:** why you want it. An agent applies an agreement with its reason more consistently.

## Worked example

````markdown
---
id: collaboration.ask-when-unclear
kind: working-agreement
title: Ask when an instruction is unclear
summary: When an instruction can be read more than one way, ask which is meant before acting
status: active
---

# Ask when an instruction is unclear

## Agreement
When an instruction can be read more than one way, name the readings and ask which is meant before acting.

## Reason
Work done on the wrong reading is discarded, and undoing it costs more than the question.
````
