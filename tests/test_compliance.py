"""The rules of the Compliance check, as CI runs them: every rule with a case that must pass and one
that must fail."""

import importlib.util
import os
import subprocess
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "compliance.py"

spec = importlib.util.spec_from_file_location("compliance", SCRIPT)
assert spec is not None and spec.loader is not None
compliance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compliance)
# A banned name, read from the script, so the list stays in one place.
BANNED = compliance.NAMES.pattern.split("(")[1].split("|")[0]

COMPLETE = "Closes #3\n\n## Why\nBecause.\n\n## What changed\nThis.\n\n## How it was verified\nTests."


def run(*arguments: str, stdin: str = "") -> int:
    environment = {key: value for key, value in os.environ.items() if key != "GITHUB_ACTIONS"}
    return subprocess.run(
        [str(SCRIPT), *arguments], input=stdin, capture_output=True, text=True, env=environment
    ).returncode


class RulesTest(unittest.TestCase):
    def test_titles(self) -> None:
        self.assertEqual(run("title", "feat(spec): add the kinds of item"), 0)
        self.assertEqual(run("title", "feat!: rename the status field"), 0)
        for title in ("feature: add the kinds", "feat: Add the kinds", "feat: add the kinds."):
            with self.subTest(title=title):
                self.assertEqual(run("title", title), 1)

    def test_descriptions(self) -> None:
        self.assertEqual(run("description", stdin=COMPLETE), 0)
        self.assertEqual(run("description", stdin=COMPLETE.replace("Closes #3", "Closes owner/repo#3")), 0)
        self.assertEqual(run("description", stdin=COMPLETE.replace("\n", "\r\n")), 0)
        for missing in ("Closes #3", "## Why", "## What changed", "## How it was verified"):
            with self.subTest(missing=missing):
                self.assertEqual(run("description", stdin=COMPLETE.replace(missing, "")), 1)

    def test_attribution(self) -> None:
        self.assertEqual(run("attribution", "A commit message", stdin="fix: drop stale views\n"), 0)
        for line in ("Co-authored-by: someone <someone@example.com>", "Generated with some tool"):
            with self.subTest(line=line):
                self.assertEqual(run("attribution", "A commit message", stdin=f"fix: x\n\n{line}\n"), 1)

    def test_names(self) -> None:
        self.assertEqual(run("names", "An added line", stdin="An agent tool reads AGENTS.md.\n"), 0)
        self.assertEqual(run("names", "An added line", stdin=f"Thanks to {BANNED.capitalize()}.\n"), 1)


if __name__ == "__main__":
    unittest.main()
