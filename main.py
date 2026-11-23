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
    # Empty env var counts as unset: fall back to /output instead of
    # crashing on makedirs("") or writing to a relative "entry.txt".
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Defensive check: the judged artifact must be exactly one byte.
    # Read back what we wrote and fail loudly rather than silently
    # submitting a wrong-length entry.
    with open(entry_path, "rb") as f:
        data = f.read()
    if data != LETTER.encode("utf-8"):
        raise SystemExit(
            f"entry.txt must be exactly one byte {LETTER!r}, got {data!r}"
        )
    sys.stdout.write(LETTER)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
