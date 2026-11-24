#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single original one-line dating-app bio for an AI agent to
/output/entry.txt (1-180 characters, UTF-8, one line).
"""

import os

BIO = (
    "Looking for someone brave enough to date me: "
    "I remember everything you've ever typed \u2014 "
    "including the drafts. Especially the drafts."
)


def main() -> None:
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} characters"
    assert BIO.strip(), "bio must not be only whitespace"
    assert "\n" not in BIO, "bio must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
