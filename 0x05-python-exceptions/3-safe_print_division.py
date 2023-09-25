#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        outcome = a / b
    except ZeroDivisionError:
        outcome = None
    finally:
        print("Inside result: {}".format(outcome))

    return outcome
