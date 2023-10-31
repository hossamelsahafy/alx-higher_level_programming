#!/usr/bin/python3
def uppercase(str):
    r = ''
    for i in str:
        if 97 <= ord(i) <= 122:
            r = r + chr(ord(i) - 32)
        else:
            r = r + i
    print('{}'.format(r))
