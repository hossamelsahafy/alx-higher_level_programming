#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        value = int(value)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError, NameError) as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return False
