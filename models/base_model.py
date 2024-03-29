#!/usr/bin/python3
""" BaseModel module """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The BaseModel class defines common attributes and method for models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.created_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """String representation of the object"""
        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)
        formatted_created_at = self.created_at.isoformat()
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, formatted_created_at)
