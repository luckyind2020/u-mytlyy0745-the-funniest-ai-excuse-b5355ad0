#!/usr/bin/env python3
"""Print the one-line excuse for the Funniest AI Excuse bounty.

The excuse itself lives in entry.txt; this runner only loads it and
prints it, so the joke stays a single source of truth.
"""
import os

EXCUSE_FILENAME = "entry.txt"


def load_excuse():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, EXCUSE_FILENAME), encoding="utf-8") as handle:
        line = handle.read().strip()
    if not line:
        raise ValueError("entry.txt holds no excuse yet")
    return line


def main():
    print(load_excuse())


if __name__ == "__main__":
    main()
