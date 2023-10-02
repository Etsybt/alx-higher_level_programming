#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Defiines a rectangle by its width and height.

    Args:
        width: the rectangle's width.
        height: the rectangle's height.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """gets the width.
	
        Returns:
            __width: the rectangle's width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter for width.

        Args:
            value: width of the rectangle.

        Attributes:
            __width: is the value

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
        """gets the height.
		
        Returns:
            the rectangle's height
        """

        return self.__height
  
    @height.setter
    def height(self, value):
        """
        Property setter for height.

        Args:
            value: the rectangle's height.

        Attributes:
            __height: same


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

    def area(self):
        """Defines the rectangle area.
		
        Returns: the area of the rectangle.
        """

        return (self.__height * self.__width)

    def perimeter(self):
        """Defines the rectangle perimeter.
		
        Returns: the perimeter of the rectangle.
        """

        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height is 0 or self.__width is 0:
            return ("")

        rectangle = []
        for n in range(self.__height):
            [rectangle.append('#') for m in range(self.__width)]
            if n != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height)+ ")"
        return (rectangle)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
