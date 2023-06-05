#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ma = my_list[0]
        for i in range(len(my_list) - 1):
            if ma < my_list[i]:
                ma = my_list[i]
        return ma;
    return None
