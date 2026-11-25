#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun one-liner entry.

Writes a single passive-aggressive note from a smart fridge to its
owner into ``entry.txt`` inside the output directory. The output
directory is taken from the ``MAKEFUN_OUTPUT_DIR`` environment
variable when set, and defaults to ``/output``.
"""

import os

LINE = (
    "Fourteen door openings last night, and the only thing taken was "
    "the ice cream. The yogurt from March has tenure now; it has "
    "outlived two of your diets."
)


def output_dir() -> str:
    """Resolve the directory the entry file belongs in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_line(line: str) -> str:
    """Guard the gate: one line, 1 to 200 characters, not blank."""
    if "\n" in line or "\r" in line:
        raise ValueError("the note must be a single line")
    if not line.strip():
        raise ValueError("the note must not be blank")
    if len(line) > 200:
        raise ValueError("the note exceeds the 200 character limit")
    return line


def main() -> None:
    note = check_line(LINE)
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(note)


if __name__ == "__main__":
    main()
