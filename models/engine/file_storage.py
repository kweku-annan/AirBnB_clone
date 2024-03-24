#!/usr/bin/python3
"""This module contains a class that serializes instances to JSON
file and deserializes JSON file to instances"""

import json
import os


class FileStorage:
    """This class serializes instances to JSON file and deserializes
    JSON file to instances. It has the following class attributes:
    
    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dictionary): Empty dictionary but will store all 
            objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__class__.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        file_path = self.__class__.__file_path
        if os.path.exists(file_path):
            reload_object = self.reload()
            for k, v in self.__class__.__objects.items():
                reload_object[k] = v.to_dict()
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(reload_object, file)
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump({
                    k: v.to_dict() for k, v in self.__class__.__objects.items()
                },
                      file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        exists."""
        if os.path.exists(self.__class__.__file_path):
            with open(self.__class__.__file_path, 'r', encoding='utf-8') as file:
                python_object = json.load(file)
                if isinstance(python_object, dict):
                    self.__class__.__object = python_object
            return (self.__class__.__object)
        else:
            pass
