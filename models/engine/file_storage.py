
import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                ojdict = json.load(f)
                for i in ojdict.values():
                    cls = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls)(**i))
        except FileNotFoundError:
            pass

