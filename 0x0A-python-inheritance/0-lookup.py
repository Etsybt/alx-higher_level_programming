#!/usr/bin/python3
""" defines the method lookup"""


def lookup(obj):
    """function that returns the list of available attributes and methods of an object"""	
    return (dir(obj))
