#!/usr/bin/python3
"""Json method"""

import json


def save_to_json_file(my_obj, filename):
    """Define to_json_string function"""

    with open(filename, "w", encoding="utf8") as i:
        json.dump(my_obj, i)
