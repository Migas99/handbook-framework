# Contributing

How this project works, from an idea to a merged change. It applies to everyone, people and agents. The
strict rules, and what agents do at each step, are in [AGENTS.md](AGENTS.md).

**Every change starts from an issue that explains why.** The issue is the permanent record of the reason
for a change; the pull request that closes it records what changed.

## Issues
Open issues from their forms:

| Form | For | Label |
|---|---|---|
| Feature | An outcome that needs several tasks | `feature` |
| Task | A concrete change in this repository | `task` |
| Bug | Something that works differently from what it should | `bug` |

- A feature's tasks are its **sub-issues**. Two levels only: feature, then task. A feature closes when
  all its sub-issues are closed.
- Before opening a pull request for something that is not yet an issue, open the issue and agree on it
  first.
- Cross-cutting attributes are labels: `breaking-change`, `security`, `dependencies`. No other labels.

## The project
Status and planning live on the [project](https://github.com/users/Migas99/projects/2). Issues opened from
the forms are added to it.

| Field | Values |
|---|---|
| **Status** | Backlog, Ready, In progress, Blocked, In review, Done |
| **Priority** | P0 drop everything, P1 next up, P2 planned, P3 someday |

| Status | Means | Set by |
|---|---|---|
| Backlog | Exists, but does not meet the definition of ready | Whoever creates the issue |
| Ready | Meets the definition of ready; can be picked up | Whoever refines the issue |
| In progress | Being worked on; has one assignee | Whoever works on it |
| Blocked | Cannot continue until something else happens; keeps its assignee | Whoever works on it |
| In review | A pull request that closes it is open | Whoever works on it |
| Done | Merged or completed | Automatic when the issue closes |

- An issue has exactly one **assignee** while it is In progress, Blocked or In review.
- A blocked issue has a comment saying why and, when another issue is the cause, a "blocked by"
  dependency on it.
- No estimates: no effort, duration, size or complexity, anywhere.

## Definition of ready
An issue is Ready when:
- **Why** explains the problem or goal and why it matters now.
- **What** and **Acceptance criteria** are clear enough for someone else to do the work.
- Open decisions are resolved, or a decision record is proposed first.
- A task that belongs to a feature is its sub-issue.
- Its Priority is set.

## Definition of done
A change is done when:
- Every acceptance criterion is met.
- Documentation affected by the change is updated in the same pull request.
- The checks pass.
- The pull request is merged, which closes the issue.

## Branches and commits
- **Trunk-based.** `main` is always releasable and receives no direct pushes. Every change reaches it
  through a pull request.
- One short-lived branch per issue, named `<type>/<issue-number>-<short-description>`, in lowercase
  kebab-case, e.g. `feat/12-check-command`.
- Commits follow [Conventional Commits](https://www.conventionalcommits.org):
  `<type>(<scope>): <description>`, lowercase, imperative, without a trailing period.
  - Types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`.
  - The scope is optional, in kebab-case.
  - A breaking change has `!` after the type or scope, and a `BREAKING CHANGE:` footer.
- Commits on a branch may be small. Only the squash commit reaches `main`, built from the pull request's
  title and description.

## Pull requests
- **Title:** a Conventional Commit subject that describes the change, such as `feat: add the check
  command`.
- **Description:** exactly these sections, in this order. The template provides them.

  ```markdown
  Closes #12

  ## Why
  One or two sentences. The full reason is in the issue.

  ## What changed
  The changes a reader of the history needs to know about.

  ## How it was verified
  What was run or checked, and the result.
  ```

- The description is about the change, not the work behind it: no checklists, reminders or notes on how
  the work went. Those belong in review comments or on the issue.
- One logical change per pull request.
- Pull requests are **squash merged**, by the maintainer, once the checks pass. Merging closes the issue.

## Checks
Every pull request runs:

| Check | Verifies |
|---|---|
| **Compliance** | The title is a Conventional Commit; the description has `Closes`, Why, What changed and How it was verified; commits have no co-author trailers or tool attribution; no agent tool or vendor is named in the title, description, branch, commits or added lines |
| **Tests** | Every rule of the Compliance check, with a case that must pass and one that must fail |

The rules live in [`scripts/compliance.py`](scripts/compliance.py), which also runs locally:

```bash
scripts/compliance.py title "feat: add the check command"
scripts/compliance.py description < description.md
python3 -m unittest discover --start-directory tests
```

## Documentation
Documentation changes in the same pull request as the change it describes.

| Where | For | Holds |
|---|---|---|
| `README.md` | A first visit | A short entry point: what a handbook is, how it works, an example, a quick start, common questions with example answers, and links to the rest |
| `docs/concepts/` | Understanding | What a handbook is, the kinds of item, families and tiers, how agent tools receive a handbook |
| `docs/guides/` | Getting things done | Creating a handbook, writing each kind with worked examples, running the checks in a CI system, installing into a workspace, upgrading |
| `docs/reference/` | Exact facts | The spec, `handbook.toml`, the commands, the agent-tool adapters |
| `docs/adr/` | Why | One record per decision ([Decisions](#decisions)) |
| A `README.md` next to each part of the code | Changing the code | How the part's pieces connect |

- Each folder's `README.md` lists its pages.
- A fact with a machine-readable source is generated from it, never written by hand: the reference pages
  that list the spec's fields come from its schemas, and the command reference from each command's help.
- Short pages, one topic per page, in plain language. Rules are stated definitively, with an example where
  it makes them clearer.

### Diagrams
A diagram is added when it shows how several parts connect, or a flow with more than a couple of steps
or branches. Two parts and an arrow, or a list, stay as text.

- Diagrams are written in [Mermaid](https://mermaid.js.org), in the Markdown, next to the text they
  explain.
- The type fits what is shown: a flowchart for parts and how they connect, a sequence diagram for
  interactions over time, a state diagram for a lifecycle.
- A change that makes a diagram wrong fixes it in the same pull request.

## Decisions
A significant decision is recorded in `docs/adr/<short-title>.md`, named by its title in kebab-case,
without a number. Each record has a status (`proposed`, `accepted`, `superseded by <record>`,
`deprecated`), a date, and the sections Context, Decision, Consequences and Alternatives considered.

- A decision is proposed in a pull request that closes its issue; merging it makes it `accepted`.
- An accepted record is never edited. A new record supersedes it, and the old one names its successor.
- [`docs/adr/README.md`](docs/adr/README.md) lists every record with its status.

## Closing without a merge
- Work that will not be done: close as **not planned**, with a comment saying why.
- Duplicates: close as **duplicate**, linking the issue that remains.
