#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    number = 0 # count of eleùments

    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end='')
            number += 1
        except (ValueError, TypeError):
            continue

    print()

    return number
