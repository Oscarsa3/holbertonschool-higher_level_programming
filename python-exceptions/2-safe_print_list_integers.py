#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        con = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                con += 1
    except TypeError:
        return i
    print()
    return con
