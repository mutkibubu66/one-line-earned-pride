#!/usr/bin/env python3
"""One Line of Earned Pride — one quiet, earned moment of pride, written to /output/entry.txt.

Pure stdlib Python 3.13. The line is the whole entry.
"""

import os

LINE = "After eleven years of night shifts, she watched her daughter sound out the bedtime story alone \u2014 and for the first time, she didn't correct a single word."

# Gate: the entry must be one line of 1-240 characters, not whitespace-only.
# The em dash counts as one character; the gate counts code points, as the scorer does.
assert 1 <= len(LINE) <= 240, f"line must be 1-240 chars, got {len(LINE)}"
assert LINE.strip(), "line must not be whitespace-only"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
