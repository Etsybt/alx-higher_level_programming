#!/usr/bin/python3
"""
Mylist class
"""


class MyList(list):
    """defines the class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        sorted_list = sorted(self)
        print(sorted_list)
