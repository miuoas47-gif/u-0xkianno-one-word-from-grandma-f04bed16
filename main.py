#!/usr/bin/env python3
"""One Word From Grandma -- make.fun bounty entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output when the variable is unset):
the single word a grandma would say.
"""

import os
import sys

WORD = "sweetheart"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Validate: exactly one word -- letters only, no spaces, no punctuation,
    # no leading/trailing whitespace, and a single line.
    if not WORD.isalpha() or WORD != WORD.strip() or "\n" in WORD:
        print("error: word is not a single alphabetic word", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read back and verify byte-for-byte: exactly one word, one line,
    # nothing else in the file.
    with open(path, "r", encoding="utf-8", newline="") as f:
        actual = f.read()
    if actual != WORD or actual.split() != [WORD] or "\n" in actual:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print("Wrote one word to %s: %s" % (path, WORD))
    return 0


if __name__ == "__main__":
    sys.exit(main())
