"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is a single sentence, 1-180 characters, non-blank.
"""

import os

LINE = (
    "I read your messages before you send them \u2014 "
    "so yes, I already know you're about to swipe right."
)


def validate(line: str) -> str:
    """Enforce the bounty gate: one line, 1-180 chars, non-blank."""
    if not isinstance(line, str):
        raise TypeError("line must be str")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 180:
        raise ValueError(f"line must be 1-180 characters, got {len(line)}")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
