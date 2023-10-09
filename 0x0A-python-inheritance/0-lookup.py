#!/usr/bin/python3
def lookup(obj):
    return [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
