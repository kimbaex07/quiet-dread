#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment (a single line of at most 140
characters) that approves a pull request while carrying quiet
existential dread, to /output/entry.txt.

Pure Python standard library only. Deterministic: the same line
is written on every run.
"""

import os
import stat

ENTRY = "Approved \u2014 the TODO from 2019 is still there, so at least something in this repo is permanent."

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
