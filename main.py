#!/usr/bin/env python3
"""Write one short funny rant to /output/entry.txt.

No network, no input files, no arguments. The text is fixed: two runs
write byte-identical output.
"""

from pathlib import Path

RANT = (
    "Mark from accounts does not email, he circles back. "
    "He circles back to the email he sent yesterday, circles back to the "
    "meeting we already had, circles back to ask if I have had a chance "
    "to circle back. I have answered him three times. He has read none "
    "of them. He is not following up, he is doing laps around my inbox "
    "while the actual work sits there, untouched, watching him run."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = RANT
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"rant must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("rant must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("rant must be a single text with no line breaks")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("rant must not contain control characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
