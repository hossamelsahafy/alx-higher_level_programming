#!/usr/bin/python3
"""define function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, \
        after each line containing a specific string"""

    with open(filename, "r+") as f:
        li = f.readlines()
        i = 0
        while i < len(li):
            if search_string in li[i]:
                li.insert(i + 1, new_string)
                i += 1
            i += 1
        f.seek(0)
        f.writelines(li)
