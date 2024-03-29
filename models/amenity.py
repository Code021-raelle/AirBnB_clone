#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity"""
        super().__init__(*args, **kwargs)
