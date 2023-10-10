#!/usr/bin/python3
"""defines a write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return (len(text))
