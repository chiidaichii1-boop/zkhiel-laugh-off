#!/usr/bin/env python3
"""One-Line Laugh-Off entry: write exactly one funny line to entry.txt.

The line (95 characters, verified by two deterministic runs):
My Roomba filed for custody of the dust bunnies and won -- I now pay child support in batteries.
"""

import os

# The joke: a robot vacuum suing for custody of the dust bunnies, with the
# punchline landing on the very last words -- child support paid in batteries.
ENTRY = "My Roomba filed for custody of the dust bunnies and won \u2014 I now pay child support in batteries."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry must be 1-200 non-whitespace characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
