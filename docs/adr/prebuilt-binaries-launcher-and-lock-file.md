---
title: Prebuilt binaries, a committed launcher, and checksums in a lock file
status: accepted
date: 2026-11-01
related: [written-in-go.md, depends-only-on-git-and-a-command-line.md, semantic-versioning-and-migrations.md]
---

# Prebuilt binaries, a committed launcher, and checksums in a lock file

## Context
Every caller must run exactly the version a handbook pins, on any machine and in any CI system, with
nothing installed beforehand. The program runs inside workspaces where agents work, so it must be the one
that was released: a release replaced after publishing must not run.

## Decision
- Each release attaches a binary per operating system and architecture, with their checksums.
- A handbook commits a launcher, `./handbook`, a short POSIX `sh` script. It reads the version from
  `handbook.toml`, downloads that release's binary once into a user cache, checks it against the SHA-256
  recorded in the handbook's lock file, and runs it.
- `handbook upgrade` writes the lock file. It is derived from the version, like the generated views.
- The download location is a URL template with a default, so a mirror on another host works.

## Consequences
- A machine needs only `sh`, `curl` and a SHA-256 tool, which Linux and macOS have.
- A tampered release fails verification instead of running.
- Each release must publish binaries and checksums, which the release build automates.
- Native Windows needs its own launcher, added later.

## Alternatives considered
- **Building from source with the Go toolchain:** nothing to host, but every machine and CI system needs
  Go, which undoes the reason for choosing it.
- **Package managers:** familiar, but a machine has one installed version while each handbook pins its
  own, and each manager is an ecosystem to maintain. They can be an extra later.
