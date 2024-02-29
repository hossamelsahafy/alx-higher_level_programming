#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mi = (lo + hi) // 2
        if list_of_integers[mi] > list_of_integers[mi + 1]:
            hi = mi
        else:
            lo = mi + 1

    return list_of_integers[lo]
