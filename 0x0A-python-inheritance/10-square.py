#!/usr/bin/python3
"""defines a Square class based on the parentClass Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle 


class Square(Rectangle):
    """defines a square class"""

    def __init__(self, size):
        """defines the square by its size.
        
        Args:
            size (int): the square's size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """defines the square's area"""
        return (self.__size ** 2)
