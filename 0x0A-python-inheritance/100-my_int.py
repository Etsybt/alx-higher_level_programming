#!/usr/bin/python3
"""Class Myint."""


class MyInt(int):
    """defines Myint based on int"""

    def __eq__(self, sign):
        """inverts == to !="""
        return super().__ne__(sign)

    def __ne__(self, sign):
        """inverts != to =="""
        return super().__eq__(sign)
