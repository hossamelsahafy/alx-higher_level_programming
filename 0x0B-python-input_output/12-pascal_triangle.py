#!/usr/bin/python3
"""Define function"""


def pascal_triangle(n):
    """Define pascal_triangle"""

    if not isinstance(n, int):
        raise TypeError("n must be integer")
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        r = [1]
        l_r = triangle[i - 1]
        r.extend([sum(p) for p in zip(l_r, l_r[1:])])
        r.append(1)
        triangle.append(r)
    return triangle
