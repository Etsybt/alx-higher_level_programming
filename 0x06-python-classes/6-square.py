#!/usr/bin/python3
"""Square class"""


class Square:
    """
    defines a square.

    Attributes:
        size: square size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialising the data.

        Args:
            size: size of square.
        """
        self.size = size
        self.position = position
  
    @property
    def size(self):
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

    @property
    def position(self):
        """
        returns the square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        property setter for position

        Args:
            value: poition

        Raise:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ gives the square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square using '#' characters"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
