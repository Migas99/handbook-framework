# Agent guide: handbook-framework

This repository defines what a handbook is, and builds the `handbook` command that checks, builds and
installs one. How the project works, from issue to merge, is in [CONTRIBUTING.md](CONTRIBUTING.md): read
it before changing anything.

## Strict rules
These apply to everyone who contributes, people and agents, and override any tool default.

- **Discuss before you record.** Create no issue, write no issue content, record no decision, and change
  no status, priority or dependency until the maintainer has discussed and agreed it. When an instruction
  is unclear, ask before acting.
- **No change without an issue that explains why.** Every pull request closes an issue.
- **Never push to `main` and never merge.** Changes reach `main` only through pull requests that the
  maintainer reviews and merges.
- **Never estimate work:** no effort, duration, size or complexity.
- **No co-author trailers or attribution.** Never add `Co-Authored-By:` trailers, or any line that
  attributes the work to a tool or agent ("Generated with …"), to commits, pull requests, issues, code or
  comments.
- **Stay tool-agnostic.** Never name a specific agent tool, assistant or AI vendor in repository content,
  commits, pull requests, issues or branch names; say "agent" or "agent tool". Files that have to name
  them as technical data are the exception: the list of names in `scripts/compliance.py`, and the
  compatibility pointer files.
- **Write ways of working as outcomes.** Describe what to achieve ("set Status to In progress"), not the
  commands of a hosting service. Steps that git does may show git.

## Working on an issue
Keep the issue and the project current as the work moves. Nobody else will.

| When | Do |
|---|---|
| Starting from an idea with no issue | Discuss it with the maintainer. Once agreed, create the issue from its form, so it is added to the project, and set its Priority. |
| Starting work | Check the issue is **Ready**; if it is not, say what is missing. Assign it to the person you work for, set Status to **In progress**, and branch from `main` as `<type>/<issue-number>-<short-description>`. |
| Opening the pull request | Push the branch and open the pull request to the standard in [CONTRIBUTING.md](CONTRIBUTING.md#pull-requests). Set Status to **In review**, then fix any failing check before review. |
| Making progress worth recording | Comment on the issue. |
| Getting blocked | Set Status to **Blocked** and comment on why. If another issue is the cause, mark the issue as blocked by it. |
| Getting unblocked | Set Status back to **In progress**. |
| Stopping without finishing | Unassign, set Status back to **Ready**, and comment on what was done and what remains. |
| Merge | Nothing. The maintainer merges, and closing the issue moves it to **Done**. |

## This repository

| Path | Holds |
|---|---|
| `scripts/compliance.py` | The rules of the Compliance check |
| `tests/` | The tests of those rules |
| `.github/` | Issue forms, the pull request template, code owners and the checks |
| `docs/adr/` | Decision records |
