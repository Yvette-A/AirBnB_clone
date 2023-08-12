#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ shows a city class inheriting BaseModel"""
    state_id = ""
    name = ""
