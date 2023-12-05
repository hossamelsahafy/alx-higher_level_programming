#!/usr/bin/python3
"""Define function that overwrite on the file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file\
        (UTF8) and returns the number of characters"""

    with open(filename, "w", encoding="utf8") as i:
        return i.write(text)
