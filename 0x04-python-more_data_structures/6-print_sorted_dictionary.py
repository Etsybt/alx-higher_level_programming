#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_dictionary = list(a_dictionary.keys())
    key_dictionary.sort()

    for a in key_dictionary:
        print("{}: {}".format(a, a_dictionary.get(a)))
