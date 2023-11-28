#!/usr/bin/python3
"""Define function"""


def magic_string():
    """Define magic_string."""
    magic_string.idx += 1
    return ", ".join(["BestSchool"] * (magic_string.idx + 1))


magic_string.idx = 0
