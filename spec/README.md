# The spec

What a handbook is, as data. The `handbook` command embeds these files, and the reference documentation
is generated from them, so they are the only place each rule is written. The decisions behind them are in
[docs/adr](../docs/adr/README.md).

| File | Defines |
|---|---|
| [kinds.yaml](kinds.yaml) | The seven kinds of item: what each is, how binding it is, when agents receive it, its body sections, and how to classify a statement |
| [statuses.yaml](statuses.yaml) | What each status means, and whether agents receive items that have it |
| [domains.yaml](domains.yaml) | The core and standard domains, with their family, tier, definition and membership test; the tie-break order; the reserved codes |
| [ids.yaml](ids.yaml) | The rules of IDs and aliases, and how skill names are derived |
| [layout.yaml](layout.yaml) | The files and folders of a handbook, and which are generated |
| [schemas/common.schema.json](schemas/common.schema.json) | The patterns of codes, IDs and versions, shared by the other schemas |
| [schemas/item.schema.json](schemas/item.schema.json) | An item's frontmatter: its fields, the fields of each kind, and the statuses each kind allows |
| [schemas/handbook.schema.json](schemas/handbook.schema.json) | `handbook.toml` |
| [examples/](examples/) | For each schema, files that must pass and files that must fail, each stating why |

## Schemas and the rules that span files
The schemas, in [JSON Schema](https://json-schema.org) 2020-12, check one file at a time. Rules that need
several files are stated in the data files, and `handbook check` enforces them:
- an item's path follows its ID, and its domain is enabled;
- IDs, aliases and the IDs that items reference exist and are unique;
- an extension's code is neither a framework domain's nor a reserved one;
- every skill name is unique and at most 64 characters;
- an item's body has its kind's required sections, in order.

Frontmatter is validated as it is written: a date such as `2026-11-01` is the text it reads as.

## Examples
Each file in [examples/](examples/) stands alone: it tests one schema, and the IDs it references need not
exist. Files under `valid/`, and `valid.toml`, must pass; files under `invalid/`, and `invalid.toml`, must
fail, for the reason stated in their first comment.
