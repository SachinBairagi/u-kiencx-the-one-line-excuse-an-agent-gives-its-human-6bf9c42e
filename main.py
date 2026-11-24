#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Pure Python standard library, fully deterministic: the line is a
fixed string, so every run writes the exact same single line,
under 160 characters, with nothing else in the file.
"""

import os

EXCUSE = (
    "I finished it on time in a parallel branch that never merged. "
    "This timeline got the version that stopped to read the docs."
)


def main():
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 160, "excuse must be 1-160 characters"
    assert "\n" not in line, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
