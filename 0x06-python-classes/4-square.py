#!/usr/bin/python3
"""Square class"""


class Square:
    """
    defines a square.

    Attributes:
        size: square size.
    """

    def __init__(self, size=0):
        """Initialising the data.

        Args:
            size: size of square.
        """
        self.__size = size
    
    def area(self):
        """Defines the square area.

        Returns: the area of the square.
        """
        return self.__size ** 2

    @property
    def size(size):
        """returns the square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter for size

        Args:
            value: size of square

        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
