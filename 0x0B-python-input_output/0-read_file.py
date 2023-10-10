#!/usr/bin/python3
"""define a read_file fnction"""


def read_file(filename=""):
    """read a filr"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
