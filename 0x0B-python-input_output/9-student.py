#!/usr/bin/python3
"""defines Student class"""



class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """public instance attributes.
		
        Args:
            first_name: student's first_name.
            last_name: student's last_name.
            age: student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
	
    def to_json(self):
        """class dir

        Returns:
            dict: dictionnary representation
	"""
        return (self.__dict__.copy())
