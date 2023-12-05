#!/usr/bin/python3
"""define function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, \
        after each line containing a specific string"""

    with open(filename, "r+") as f:
        l = f.readlines()
        i = 0
        while i < len(l):
            if search_string in l[i]:
                l.insert(i + 1, new_string)
                i += 1
            i += 1
        f.seek(0)
        f.writelines(l)
