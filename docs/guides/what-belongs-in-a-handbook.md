# What belongs in a handbook

A handbook holds what an agent would not do on its own. Every item that reaches an agent costs context on
every task it applies to, and helps only when it changes what the agent does. Research on repository
instruction files found that general overviews and widely known practice add cost without improving
results, while instructions that describe what is particular to a project help
(Gloaguen et al., "Evaluating AGENTS.md", arXiv:2602.11988).

## The test
Before writing an item, ask: **would a capable agent already do this, unprompted?** Write the item when the
answer is no:

- **A preference among reasonable options:** squash merging, a commit format, a testing approach.
- **A convention particular to the owner:** how issues move, how decisions are recorded, how code is laid
  out.
- **A constraint from outside the code:** never merge, never estimate, discuss before recording.
- **A fact only the owner has:** a glossary, a registry of identifiers, where things are hosted.
- **The reason behind any of these,** so an agent can judge the cases the item does not name.

## Where items come from
The best source is the corrections you make. Each time you tell an agent "not like that" or "we do it this
way", that statement is a candidate item. Decisions you take, and conventions your reviews keep repeating,
are the others. Start small and grow from real corrections, rather than writing a handbook up front.

## Choosing the kind
Classify each statement with the [classification questions](../../spec/kinds.yaml), then follow the guide
for its kind:

| Kind | Guide |
|---|---|
| Principle | [Writing a principle](writing-a-principle.md) |
| Working agreement | [Writing a working agreement](writing-a-working-agreement.md) |
| Rule | [Writing a rule](writing-a-rule.md) |
| Guideline | [Writing a guideline](writing-a-guideline.md) |
| Procedure | [Writing a procedure](writing-a-procedure.md) |
| Reference | [Writing a reference](writing-a-reference.md) |
| Decision | [Writing a decision](writing-a-decision.md) |
