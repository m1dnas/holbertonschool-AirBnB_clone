#!/usr/bin/python3


import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name = obj.__class__.__name__
        key = "{}.{}".format(name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        objdict = {}
        
        for key, obj in self.__objects.items():
            objdict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                ojdict = json.load(f)
                for i in ojdict.values():
                    cls = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls)(**i))
        except FileNotFoundError:
            pass

