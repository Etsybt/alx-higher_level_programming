#!/usr/bin/python3
"""defines a Mylist class"""


class MyList(list):
    """defines the class by the print_sorted function."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
