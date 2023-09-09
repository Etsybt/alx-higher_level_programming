#!/usr/bin/python3
def no_c(my_string):
    alt = [char for char in my_string if char != 'c' and char != 'C']
    return ("".join(alt))
