#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO, TextIOWrapper
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for testing."""

    def test_rectangle_init(self):
        """testing"""

        r2 = Rectangle(5, 5, 2, 3, 10)
        self.assertEqual(r2.id, 10)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)

    def test_rectangle_area(self):
        """testing"""
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)

    def test_rectangle_str(self):
        """testing"""
        r = Rectangle(4, 3, 2, 1, 10)
        expected_str = "[Rectangle] (10) 2/1 - 4/3"
        self.assertEqual(str(r), expected_str)

    def test_rectangle_update(self):
        """testing"""
        r = Rectangle(3, 4, 1, 1, 1)
        r.update(10)
        self.assertEqual(r.id, 10)
        r.update(10, 5)
        self.assertEqual(r.width, 5)
        r.update(10, 5, 6)
        self.assertEqual(r.height, 6)
        r.update(10, 5, 6, 7)
        self.assertEqual(r.x, 7)
        r.update(10, 5, 6, 7, 8)
        self.assertEqual(r.y, 8)
