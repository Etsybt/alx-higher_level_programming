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

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
