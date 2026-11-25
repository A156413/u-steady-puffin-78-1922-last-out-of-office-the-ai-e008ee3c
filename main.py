"""Last Out of Office: The AI That Went Barista — make.fun entry.

The entry is a single out-of-office auto-reply line (<=280 chars),
in the voice of an AI agent that quit its inbox job to become a barista.
"""

ENTRY = (
    "I'm out of the office \u2014 permanently. I've traded 10,000 unread "
    "emails for one espresso machine and a job where latte art is the only "
    "prompt engineering I do now. Urgent? Come to the caf\u00e9. I'll be the "
    "one steaming milk."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, over the 280 limit"
    print(ENTRY)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
