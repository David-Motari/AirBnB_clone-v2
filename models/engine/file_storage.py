#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            new_object = {}
            for key, value in FileStorage.__objects.items():
                if type(value).__name__ == cls:
                    new_object[key] = value
            return new_object
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj if not None fron attribute __objects"""
        if obj is not None:
            obj_to_del = f"{type(obj).__name__}.{obj.id}"
            objcts = self.all(obj.__class__.__name__)
            if objcts.get(obj_to_del):
                del self.__objects[obj_to_del]
            self.save()
        else:
            return

    def close():
        """calls reload method for deserialization"""
        self.reload()
