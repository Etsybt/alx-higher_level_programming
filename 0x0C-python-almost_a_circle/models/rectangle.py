#!/usr/bin/python3
"""defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor.

        Args:
            width (int): the rectangle's width.
            height (int): the rectangle's height.
            x (int): attribute.
            y (int): attribute.
            id (int): attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.height * self.width

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))
