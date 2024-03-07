#!/usr/bin/python3
"""This module creates a FileStorage class """

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class FileStorage:
    """This class serializes instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method for return the dictionary of __object"""
        return self.__objects

    def new(self, obj):
        """Method for set a new object with key <obj class name>"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Method for serialize all objects in a JSON file"""
        new_dictionary = {}

        for key in self.__objects:
            new_dictionary[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dictionary, file)

    def reload(self):
        """Method for deserialize a JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                json_file = json.load(file)
                for key, value in json_file.items():
                    class_name, object_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
