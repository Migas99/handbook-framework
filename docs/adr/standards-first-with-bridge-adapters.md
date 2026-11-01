---
title: Standards first, with bridge adapters for the major agent CLIs
status: accepted
date: 2026-11-01
related: [how-agent-tools-receive-a-handbook.md, one-instance-per-workspace.md, optional-read-only-mcp-server.md]
---

# Standards first, with bridge adapters for the major agent CLIs

## Context
A handbook must work with whichever agent tool a person uses. Tools differ in which instruction file they
read, where they look for skills and how they see a workspace, and they change these conventions often.
Support should not depend on which tools the maintainer happens to use.

## Decision
- `handbook install` always writes the open-standard outputs: `AGENTS.md`, skills in the Agent Skills
  format in the neutral location, and MCP registration once the server exists. A tool that follows them
  needs nothing else.
- An adapter row only bridges what a tool does differently, such as its own instruction file or skills
  folder.
- The first release has rows for the most widely used agent command-line tools at that time.
- Each row cites its source, the tool's documentation and the date it was checked; has an automated test
  that installs into a temporary workspace and checks every file is where the row says; and can be checked
  live by anyone who has the tool, in its non-interactive mode.
- Rows whose date is old are reviewed. More rows arrive as contributions, in minor versions.

## Consequences
- The major tools work from the first release, whatever a person has installed.
- Rows stay small, and shrink as tools adopt the standards.
- Keeping rows current is ongoing work, made visible by their dates.

## Alternatives considered
- **Rows only for the tools the maintainer uses:** less to maintain, but support would depend on one
  person's tools.
- **Standards only, with no bridges:** nothing to maintain, but tools that read only their own files would
  get nothing.
