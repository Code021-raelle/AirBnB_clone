#!/usr/bin/python3
""" Test for BaseModel module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_init(self):
        """Test initial state of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__))

    def test_save(self):
        """Test the save method updates the updated_at attribute."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        expected_keys = [
                'id', 'created_at', 'updated_at',
                '__class__', 'name', 'my_number'
                ]
        self.assertCountEqual(my_model_json.keys(), expected_keys)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
