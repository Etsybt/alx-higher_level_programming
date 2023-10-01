#!/usr/bin/python3
"""functions that adds two integers"""


def add_integer(a, b=98):
    """
    adds two floats or integers.
    
    Args:
        a: integer or float.
        b: integer or float.

    Returns:
        int: a + b

    Raises:
        TypeError: if a or b isn't an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
