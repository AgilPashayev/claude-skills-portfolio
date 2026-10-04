#!/usr/bin/env python3
"""Print commit subjects between two git refs. Run this; do not paste it into context."""

from __future__ import annotations

import subprocess
import sys


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> int:
    start = sys.argv[1] if len(sys.argv) > 1 else None
    end = sys.argv[2] if len(sys.argv) > 2 else "HEAD"

    if start is None:
        try:
            start = git("describe", "--tags", "--abbrev=0")
        except subprocess.CalledProcessError:
            start = git("rev-list", "--max-parents=0", "HEAD")

    log = git("log", f"{start}..{end}", "--pretty=format:%s")
    if not log:
        print("No commits in range.")
        return 0

    skip_prefixes = ("merge ", "wip:", "chore:", "chore(")
    for line in log.splitlines():
        lowered = line.lower()
        if lowered.startswith(skip_prefixes) or lowered.startswith("merge "):
            continue
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
