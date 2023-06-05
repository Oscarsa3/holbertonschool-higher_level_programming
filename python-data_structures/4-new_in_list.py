#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        copy = my_list.copy()
        copy[idx] = element
        return copy
