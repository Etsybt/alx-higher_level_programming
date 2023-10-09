#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class defined"""

    def area(self):
        """defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): the name of the parameter.
            value (int): the param to validate.
        Raises:
            TypeError: if value isn't an int.
            ValueError: if value is less or equal than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
