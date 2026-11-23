#!/usr/bin/env python3
"""One-star review of an everyday essential: sleep.

Builds a single deadpan one-star review from small fragments, prints it
to stdout, and writes it, with no trailing newline, to entry.txt inside
the output directory. The review is 102 characters, one line, one
sentence: sleep is paid eight hours, returns the sleeper tired and late,
and still leaves them in debt for another eight tonight.
"""

import os
from pathlib import Path


def build_line() -> str:
    setup = "I paid sleep eight hours and woke up tired, late,"
    payoff = " and somehow still in debt for another eight tonight."
    return setup + payoff


def main() -> None:
    line = build_line()
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(line) <= 160 or not line.strip():
        raise ValueError("entry must be 1-160 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    os.chmod(out_dir / "entry.txt", 0o644)
    print(line)


if __name__ == "__main__":
    main()
