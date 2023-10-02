#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Defiines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialising the date.

        Args:
            width: the rectangle's width.
            height: the rectangle's height.
        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """returns the rectangle's width"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter for width.

        Args:
            value: width of the rectangle.

        Raise:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the rectangle's height"""

        return self.__height
  
    @height.setter
    def height(self, value):
        """
        Property setter for height.

        Args:
            value: the rectangle's height.

        Raise:
            TypeError: height must be an integer.
            ValueError: height must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
