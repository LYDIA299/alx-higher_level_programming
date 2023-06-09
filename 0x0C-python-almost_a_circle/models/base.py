#!/usr/bin/python3

"""Defines the Base class."""
import json


class Base():
    """Base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor.
        @ id(int): id for objects.
        """

        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        @ list_dictionaries: a list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        @ list_objs: a list of instances who inherits of Base.
        """

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_obj_dict = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(list_obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        @ json_string: string representing a list of dictionaries.
        """

        if json_string is None or len(json_string) == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy_instance = cls(1, 2)
            else:
                dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        ret_list = []
        try:
            with open(filename, encoding='utf-8') as f:
                str_list = Base.from_json_string(f.read())
                for x in str_list:
                    """@ x: is a dictionary."""
                    ret_list.append(cls.create(**x))
            return ret_list
        except IOError:
            return []
