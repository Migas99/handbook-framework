# Families, tiers and domains

Items are organized into **domains** by topic, such as `delivery` or `quality`. An item belongs to exactly
one domain, which is the prefix of its ID: `quality.tests-earn-their-place` is in `quality`. Domains
organize a handbook for its authors and readers; when an agent receives an item is decided by its kind and
its `applies_when`, not by its domain.

The domains the framework defines, with their definitions and membership tests, are in
[spec/domains.yaml](../../spec/domains.yaml).

## Families
Every domain belongs to one of two **families**:
- **Practice:** how the owner works and builds, such as their delivery process, their testing approach or
  their coding conventions. This knowledge goes with the owner from project to project.
- **System:** what one particular system is, such as its purpose, its business language or its
  architecture.

A person's handbook is mostly practice. An organization that builds a product has both.

## Tiers
- **Core** domains exist in every handbook, because the framework relies on them: `handbook init` creates
  their folders, and generates the `meta` items that describe the handbook itself.
- **Standard** domains are defined by the framework and turned on per handbook, in `handbook.toml`.
- **Extension** domains are defined by a handbook itself, in `handbook.toml`, with a code, a family, a
  definition and a membership test.

## Choosing a domain
Put an item in the domain whose membership test it passes. When several pass, the
[tie-break order](../../spec/domains.yaml) decides: the most specific domains, `languages` and `security`,
come first.
