#!/usr/bin/python3

def magic_calculation(a, b):
    outcome = 0

    for n in range(1, 4):
        try:
            if n > a:
                raise Exception("Too far")
            outcome += a ** b / n
        except:
            outcome = b + a
            break

    return outcome
