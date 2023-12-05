#!/usr/bin/python3
"""json method"""
import json


def load_from_json_file(filename):
    """Define load_from_json_file"""
    with open(filename, "r", encoding="utf8") as i:
        return json.load(i)
