#!/usr/bin/python3
""" FileStorage module """
import datetime
import json


class FileStorage:
    """FileStorage class for serializing instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                deserialized_objects = json.load(f)
                for key, obj_dict in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def classes(self):
        """Classes and their reference"""
        from models.user import User
        from models.base_model import BaseModel

        classes = {"User": User,
                "BaseModel": BaseModel}
        return classes
