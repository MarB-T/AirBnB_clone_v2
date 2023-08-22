#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base
from models.state import State
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes the class City"""
        Super().__init__(*args, **kwargs)
