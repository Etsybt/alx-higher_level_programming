#!/usr/bin/python3

def magic_calculation(a, b):
    outcome = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception("Too far")
            outcome += (a ** b) / n
        except Exception:
            outcome = b + a
            break
    return outcome
