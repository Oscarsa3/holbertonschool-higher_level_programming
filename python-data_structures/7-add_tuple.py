#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tupla_c = (a, b)
    return tupla_c
