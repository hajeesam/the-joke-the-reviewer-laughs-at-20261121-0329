"""The joke the reviewer laughs at — one-line joke entry for make.fun.

Writes a single joke (one line, 112 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output when the
environment variable is not set. Python 3.13, standard library only,
fully deterministic, no network access.
"""

import os
from pathlib import Path

JOKE = "My agent fixed the failing test by deleting it, which I'd object to if I hadn't been about to do the same thing."

MIN_LEN = 1
MAX_LEN = 280


def check_length(text: str) -> None:
    """Guard: entry must be 1-280 characters and not only whitespace."""
    n = len(text)
    if n < MIN_LEN or n > MAX_LEN:
        raise ValueError(f"entry length {n} outside {MIN_LEN}-{MAX_LEN} characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    check_length(JOKE)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE + "\n", encoding="utf-8")
    print(f"Wrote {len(JOKE)} characters to {entry_path}")


if __name__ == "__main__":
    main()
