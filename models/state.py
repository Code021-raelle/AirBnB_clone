#!/usr/bin/python3
"""Module for state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State"""
        super().__init__(*args, **kwargs)
