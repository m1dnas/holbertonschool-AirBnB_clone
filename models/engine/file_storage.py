#!/usr/bin/python3
"""serializes instances to JSON and vice versa"""

import json
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class that serializes and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the object with the obj key"""
        name = obj.__class__.__name__
        key = "{}.{}".format(name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes to a JSON file"""
        objdict = {}

        with open(self.__file_path, 'w') as f:
            for key, obj in self.__objects.items():
                objdict[key] = obj.to_dict()
            json.dump(objdict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        data_dict = {}
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
