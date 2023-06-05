#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ma = my_list[0]
        i = 0
        while i < len(my_list):
            if ma < my_list[i]:
                ma = my_list[i]
            i += 1
        return ma
