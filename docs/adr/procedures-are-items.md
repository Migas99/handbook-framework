---
title: Procedures are items, and one repository holds a whole handbook
status: accepted
date: 2026-11-01
related: [one-framework-repository-and-one-per-instance.md, seven-kinds-of-item.md, names.md]
---

# Procedures are items, and one repository holds a whole handbook

## Context
A handbook holds both knowledge and procedures. Procedures work best split in two: mechanical steps in a
command that does them the same way every time, and judgment in written guidance, with a skill as the
front door. Keeping procedures in a separate repository from the rest of the handbook splits a
procedure's text from its command and its reasons, and gives each handbook two versions to pin.

## Decision
- A procedure is an item of kind `procedure`, in its domain's folder like any other item. Its `command`
  field names the command that does its mechanical steps.
- One repository holds a whole handbook: every item, and an optional `commands/` folder with the
  handbook's own commands.
- Skills are generated from procedure items. The playbook is the generated view of every procedure, its
  skill and its command, not a separate repository.
- The generic machinery (installer, generator, skill builder) belongs to the framework.

## Consequences
- A procedure's text and its command change in the same pull request.
- A handbook has one version to pin and one thing to install, and links never cross repositories.
- A handbook with commands also carries their code and tests; one without commands is documentation only.

## Alternatives considered
- **Two repositories, with the procedure text in the handbook and the commands in a playbook:** keeps
  documentation and code apart, but splits each procedure and needs paired pull requests and two pins.
- **Two repositories, with procedures and commands in the playbook:** keeps procedures whole, but needs
  two pins, IDs resolved across repositories, and an installer that combines both.
