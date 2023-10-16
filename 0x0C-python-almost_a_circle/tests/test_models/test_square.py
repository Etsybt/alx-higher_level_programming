#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """class testing."""

    def test_square_size(self):
        """testing."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 8
        self.assertEqual(s.size, 8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_square_update(self):
        """testing."""
        s = Square(3, 1, 1, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(10, 5)
        self.assertEqual(s.size, 5)
        s.update(10, 5, 6)
        self.assertEqual(s.x, 6)
        s.update(10, 5, 6, 7)
        self.assertEqual(s.y, 7)

    def test_square_to_dictionary(self):
        """testing."""
        s = Square(4, 2, 1, 10)
        expected_dict = {'id': 10, 'size': 4, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
