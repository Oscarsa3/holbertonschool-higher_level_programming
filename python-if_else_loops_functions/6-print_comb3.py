#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i == x - 1 and x == 9:
            print("{}{}".format(i, x))
        elif i != x and x > i:
            print("{}{}, ".format(i, x), end='')
