#!/usr/bin/python3
"""
Mylist class
"""


class MyList(list):
    """defines the class"""
    pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(list(self)))
