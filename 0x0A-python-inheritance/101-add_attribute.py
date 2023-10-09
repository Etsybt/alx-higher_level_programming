#!/usr/bin/python3
"""defines a add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """function that adds a new attribute to an object if it’s possible.

    Args:
        obj: the object to which the attribute should be added.
        attr_name: the name of the attribute
        attr_value: the value of the attribute

    Raises:
        TypeError: if the attribute can't be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
