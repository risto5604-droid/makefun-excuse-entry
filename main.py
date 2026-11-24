#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d."""
import os

LINE = "I would blame the data, the market, or you, but my logs show the failure was mine, timestamped, reproducible, and entirely my fault."

# Gate: the entry must be 1-200 characters of UTF-8 text, not only whitespace.
# ASCII is enforced too: the line is plain English, so any non-ASCII byte means
# the text was corrupted in editing and the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii(), "entry line violates the 1-200 character gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
