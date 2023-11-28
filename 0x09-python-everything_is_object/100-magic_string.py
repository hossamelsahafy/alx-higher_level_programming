#!/usr/bin/python3
"""Define function"""


def magic_string():
    """Define Magic"""
    magic_string.n = getattr(magic_string, "n", 0) + 1
    return "BestSchool, " * (magic_string.n - 1) + "BestSchool"
