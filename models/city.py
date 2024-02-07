#!/usr/bin/pypthon3
"""Defines the city class."""
from models.base_model import BaseModel

class city(BaseModel):
    """Represent a city.
    Attributes:
    state_id (str): Teh state id.
    name (str): The name of the city.
    """
    state_id = ""
    name = ""
