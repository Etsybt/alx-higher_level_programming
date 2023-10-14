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
        """defines width.

        Returns:
            int: the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setting width.

        Args:
            value (int): value.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines height.

        Returns:
            int: the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setting height.

        Args:
            value (int): value.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """attribute.

        Returns:
            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setting x.

        Args:
            value (int): value.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Attribute.

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setting y.

        Args:
            value (int): value.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the rectangle's area.

        Returns:
            int: area.
        """
        return self.height * self.width

    def display(self):
        """print in stdout the Rectangle
        instance with the character #.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """prints a str.

        Returns:
            str.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """gives args to attributes.

        Args:
            args (int): args to be assigned.
            kwargs (dict): key-worded argument.
        """
        if args is not None and len(args) != 0:
            for n in range(len(args)):
                if n == 0:
                    self.id = args[n]
                elif n == 1:
                    self.__width = args[n]
                elif n == 2:
                    self.__height = args[n]
                elif n == 3:
                    self.__x = args[n]
                elif n == 4:
                    self.__y = args[n]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """returns a dict representation of a rectangle.

        Returns:
            dict.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
