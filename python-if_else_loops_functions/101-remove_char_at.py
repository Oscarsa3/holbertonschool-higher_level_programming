#!/usr/bin/python3
def remove_char_at(str, n):
    re = ''
    for i in range(len(str)):
        if i == n:
            i += 1
        else:
            re += str[i]
    return re
