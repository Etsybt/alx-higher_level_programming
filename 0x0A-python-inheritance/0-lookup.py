#!/usr/bin/python3
"""defines the method lookup"""



def lookup(att):
    """function that returns the list of available attributes and methods of an object"""	
    return (dir(att))
