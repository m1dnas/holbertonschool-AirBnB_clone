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
        odict = FileStorage.__objects
        
        for key, obj in FileStorage.__objects.items():
            odict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(odict, f)

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

