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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
	    
    def area(self):
        """Defines the square area.

        Returns: the area of the square.
        """
        return self.__size ** 2
