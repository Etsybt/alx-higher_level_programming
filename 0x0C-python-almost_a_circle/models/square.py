#!/usr/bin/python3
"""defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor.

        Args:
            size (int): the square's size.
            x (int): attribute.
            y (int): attribute.
            id (int): id.
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """print a str.

        Returns:
            str.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def size(self):
        """def size.

        Returns:
            size (int): the square's size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """setting size.

        Args:
            value (int): value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """gives args attributes.

        Args:
            args (int): args to be assigned attr.
            kwargs (dict): key-worded argument.
        """
        if args is not None and len(args) != 0:
            for n in range(len(args)):
                if n == 0:
                    self.id = args[n]
                elif n == 1:
                    self.width = args[n]
                    self.height = args[n]
                elif n == 2:
                    self.x = args[n]
                elif n == 3:
                    self.y = args[n]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """return dict representation of a Square.

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
