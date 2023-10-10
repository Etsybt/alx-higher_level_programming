#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a Student class."""
	    
    def __init__(self, first_name, last_name, age):
        """Initialize a Student object.
		
        Args:
            first_name (str): student's first_name.
            last_name (str): student's last_name.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
	
    def to_json(self):
        """Return a dictionary representation of the Student."""
        return self.__dict__
