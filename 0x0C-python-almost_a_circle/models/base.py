#!/usr/bin/python3
"""defines a Base class"""
import json
import csv


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
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries
        from a JSON string representation."""
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
                content_string = a_file.read()
            a_list = cls.from_json_string(content_string)
            list_instances = []
            for i in range(len(a_list)):
                list_instances.append(cls.create(**a_list[i]))
        except Exception as e:
            list_instances = []

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save instances to a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load instances from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        list_instances = []
        try:
            with open(filename, mode="r", newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(
                            row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(
                            row[3]), int(row[0]))
                    list_instances.append(obj)
        except FileNotFoundError:
            pass
        return list_instances
