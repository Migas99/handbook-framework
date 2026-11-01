# Kinds of item

A handbook is made of **items**, one file each. Every item has exactly one **kind**, and its kind decides
three things at once: how binding the item is, when an agent receives it, and which sections it has. The
seven kinds, their definitions and their sections are in [spec/kinds.yaml](../../spec/kinds.yaml).

## How binding, and when it is received
- **Principles** and **working agreements** are always in an agent's context: principles are the values
  it judges by, and working agreements say how it behaves with the owner. They are kept few and short,
  because they cost context on every task.
- **Rules** and **guidelines** reach an agent when the task matches their `applies_when`. A rule is
  non-negotiable and is enforced by a check, hook or permission; a guideline is a default, which a case may
  depart from with a stated reason.
- **Procedures** become skills of their own, so an agent picks them up when it is about to do that task.
- **References** hold facts, and are looked up when needed.
- **Decisions** explain why, and are read when someone asks why something is the way it is, or proposes
  to change it.

## Two lines that keep kinds honest
- **A rule exists only if something enforces it.** A requirement that no tool checks is a working
  agreement when it concerns how an agent behaves, and otherwise a guideline. Rules that nothing checks
  drift.
- **A decision never instructs.** When a decision changes what people or agents do, it creates or updates
  the rule, guideline or agreement that says so, and that item links back to it. What to do always lives
  in a current item, and why in a record that does not change.

## Classifying a statement
Ask the [classification questions](../../spec/kinds.yaml) in order, and take the first that is answered
yes. For example, "pull request titles are Conventional Commits, and CI checks them" is not a choice, not a
procedure and not a fact to look up; it is binding and a tool enforces it, so it is a rule. "Prefer fewer
tests that catch real regressions" is a default with a reason, so it is a guideline, unless it is held as
a value that guides every judgment about tests, in which case it is a principle.
