#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        b = sentence[0]
        tupla = (a, b)
        return tupla
    a = 0
    b = "None"
    tupla = (a, b)
    return tupla
