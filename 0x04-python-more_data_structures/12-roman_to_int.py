#!/usr/bin/python3
def roman_to_int(roman_string):
    r_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        t = 0
        p_value = 0
        for c in reversed(roman_string):
            value = r_num[c]
            if value < p_value:
                t = t - value
            else:
                t = t + value
                p_value = value
        return t
