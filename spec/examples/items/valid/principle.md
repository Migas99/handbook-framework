---
id: quality.tests-earn-their-place
kind: principle
title: Tests earn their place
summary: Fewer tests that catch real regressions beat many that restate the implementation
status: active
---

# Tests earn their place

## Principle
A test is kept only when it would catch a plausible bug and survive a refactor that keeps behavior the
same.

## Reason
Tests are code that is maintained. Tests that restate the implementation fail on every change and catch
nothing.

## In practice
- A test that only checks a mock was called is rewritten to check an outcome.
- A failing test is investigated before its assertion is touched.
