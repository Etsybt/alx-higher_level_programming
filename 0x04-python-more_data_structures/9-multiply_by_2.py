#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copied = a_dictionary.copy()
    key_dictionary = list(copied.keys())

    for a in key_dictionary:
        copied[a] *= 2

    return copied
