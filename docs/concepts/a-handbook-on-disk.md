# A handbook on disk

A handbook is a repository with its configuration at the root, one folder per enabled domain, and what
`handbook build` generates. Every file and folder, and which are generated, is in
[spec/layout.yaml](../../spec/layout.yaml).

For example, a handbook that turns on two standard domains:

```
handbook.toml                          the configuration: name, prefix, framework version, domains
handbook.lock                          checksums of the pinned framework release
handbook                               the launcher: ./handbook check
README.md
collaboration/
  one-decision-at-a-time.md            collaboration.one-decision-at-a-time
delivery/
  commit-format.md                     delivery.commit-format
  open-pull-request.md                 delivery.open-pull-request
quality/
  tests-earn-their-place.md            quality.tests-earn-their-place
code/
  errors-say-what-to-do.md             code.errors-say-what-to-do
design/
  events-between-contexts.md           design.events-between-contexts
commands/
  open-pull-request                    run by the procedure delivery.open-pull-request
generated/                             written by handbook build
```

- **An item's path follows its ID:** `<domain>/<slug>.md` holds the item `<domain>.<slug>`.
- **Decisions sit in their domain**, like any other item, without a number.
- **The launcher** runs the framework version pinned in `handbook.toml`, verified against
  `handbook.lock`, so every person, agent and CI system runs the same version.
- **`generated/` is committed,** and `handbook check` fails when it is out of date.

The [examples](../../spec/examples/) in the spec show what each kind of item, and `handbook.toml`, look
like.
