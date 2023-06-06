#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    unicos = set(my_list)
    for numero in unicos:
        new.append(numero)
    return sum(new)
