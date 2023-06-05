#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new = my_list.copy()
        i = 0
        while i < len(my_list):
            if my_list[i] % 2 == 0:
                new[i] = True
            else:
                new[i] = False
            i += 1
        return new
