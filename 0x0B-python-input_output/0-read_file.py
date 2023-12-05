#!/usr/bin/python3
"""Define function that read file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r", encoding="utf8") as i:
        print(i.read(), end="")