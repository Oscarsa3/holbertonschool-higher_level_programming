#!/usr/bin/python3
def uppercase(str):
    a = 0
    mayu = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            mayu += chr(ord(str[i]) - 32)
        else:
            mayu += str[i]
        a += 1
    print("{}".format(mayu))
