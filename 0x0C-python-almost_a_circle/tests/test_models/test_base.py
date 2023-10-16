#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing Class"""

    def test_base_init(self):
        """testing."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

    def test_to_json_string(self):
        """testing"""
        b = Base()
        b_json = b.to_json_string(
                [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}])
        self.assertEqual(
                b_json,
                '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
                )

    def test_from_json_string(self):
        """testing"""
        b = Base()
        b_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = b.from_json_string(b_json)
        self.assertEqual(
                data, [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}])


if __name__ == '__main__':
    unittest.main()
