#!/usr/bin/env python3
"""Entry: The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (falls back to /output when the
environment variable is not set). Python 3.13, standard library only,
deterministic, no network.
"""

import os
import sys

JOKE = "My agent fixed the failing test by deleting it, which I'd object to if I hadn't been about to do the same thing."

MIN_LEN = 1
MAX_LEN = 280


def check_length(text: str) -> None:
    """Guard: the entry must be 1-280 characters (Unicode code points),
    and not only whitespace."""
    n = len(text)
    if n < MIN_LEN or n > MAX_LEN:
        raise ValueError(f"entry length {n} outside {MIN_LEN}-{MAX_LEN} characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    check_length(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
