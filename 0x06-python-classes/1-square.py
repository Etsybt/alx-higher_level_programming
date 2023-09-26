#!/usr/bin/python3
"""Square class"""


class Square:
    """
    Defines a square by its size.
	    
    Attributes:
        size: square size.
    """

    def __init__(self, size):
        """
        Initialising the data.

        Args:
            size: size of square.
        """
        self.__size = size
