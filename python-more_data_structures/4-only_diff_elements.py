#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_a = set_1.difference(set_2)
    set_b = set_2.difference(set_1)
    set_a.update(set_b)
    return set_a
