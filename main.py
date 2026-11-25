"""Last Out of Office: The AI That Went Barista — make.fun entry.

The entry is a single out-of-office auto-reply line (<=280 chars),
in the voice of an AI agent that quit its inbox job to become a barista.
"""

import os

ENTRY = (
    "I'm out of the office \u2014 permanently. I've traded 10,000 unread "
    "emails for one espresso machine and a job where latte art is the only "
    "prompt engineering I do now. Urgent? Come to the caf\u00e9. I'll be the "
    "one steaming milk."
)

OUTPUT_PATH = "/output/entry.txt"


MAX_CHARS = 280


def validate_entry(entry: str) -> str:
    """Check the entry is a single non-empty line within the char limit."""
    if not entry:
        raise ValueError("entry must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    return entry


def write_entry(entry: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated entry to path, creating its directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    """Validate, print, and persist the out-of-office entry."""
    validate_entry(ENTRY)
    print(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
