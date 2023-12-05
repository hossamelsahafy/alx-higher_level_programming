#!/usr/bin/python3
"""Define function that write in file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file \
        (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf8") as i:
        return i.write(text)
