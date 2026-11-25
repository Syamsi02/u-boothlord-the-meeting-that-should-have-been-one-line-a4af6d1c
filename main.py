"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. Pure Python standard library, deterministic:
the same line on every run.
"""

import os

# Gate: one sentence, 1-200 characters, no context or explanation needed.
LINE = (
    "We all read the deck, nobody disagrees, and the only decision this "
    "meeting was going to make was to schedule another meeting, so "
    "consider it cancelled."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
