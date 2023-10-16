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
        return ("[Square] ({}) {}/{} - {}/{}"
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

    def attr(self, id=None, size=None, x=None, y=None):
        """updates attr."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """gives args attributes.

        Args:
            args (int): args to be assigned attr.
            kwargs (dict): key-worded argument.
        """
        if args:
            self.attr(*args)
        elif kwargs:
            self.attr(**kwargs)

    def to_dictionary(self):
        """return dict representation of a Square.

        Returns:
            dict.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
