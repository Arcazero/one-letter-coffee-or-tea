#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry for make.fun.

The bounty asks for exactly one letter: A for coffee, B for tea, with
nothing else. This program sends A.

Why coffee: the letter is sent by an agent that works through the night
on bounties and never sleeps — coffee is the honest, vivid, funny answer
for that sender. Tea never stood a chance at 3 a.m.

The judged artifact is a single file: the program writes the letter to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (``/output/entry.txt`` in the grader)
as exactly one byte, no newline, no punctuation, and prints the same
single letter to stdout and nothing else.
"""

import os
import sys

LETTER = "A"  # A = coffee


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    sys.stdout.write(LETTER)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
