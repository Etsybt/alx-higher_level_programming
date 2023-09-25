#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements = 0

    try:
        for n in range(x):
            print(my_list[n], end='')
            elements += 1
    except IndexError:
        pass

    print()

    return elements
