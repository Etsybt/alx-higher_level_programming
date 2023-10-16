#!/usr/bin/python3
"""defines a Base class"""
import json


class Base:
    """class Base defined"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor.

        Args:
            id (int): attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            cls: str.
            list_objs: list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from a JSON string representation."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary
        Returns:
            an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Returns:
            list of instances
        """
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()  # str of list of dictionaries
            a_list = cls.from_json_string(content_string)  # str to list
            list_instances = []
            for i in range(len(a_list)):  # a_list[i]: dictionary of attributes
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances
