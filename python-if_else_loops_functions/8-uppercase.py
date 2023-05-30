#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    a = 0
    while a < i:
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            print(f"{chr(ord(str[a]) - 32)}", end='')
        else:
            print(f"{str[a]}", end='')
        a += 1
    print()
