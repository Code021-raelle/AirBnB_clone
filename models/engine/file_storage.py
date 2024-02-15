#!/usr/bin/python3
""" FileStorage module """
import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class for serializing instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        cls = BaseModel
                    elif cls_name == 'User':
                        cls = User
                    elif cls_name == 'Place':
                        cls = Place
                    elif cls_name == 'State':
                        cls = State
                    elif cls_name == 'City':
                        cls = City
                    elif cls_name == 'Amenity':
                        cls = Amenity
                    elif cls_name == 'Review':
                        cls = Review
                    else:
                        continue
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
