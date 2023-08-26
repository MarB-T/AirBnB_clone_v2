#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class State"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter method that returns a list of city instances"""
            city_instance = models.storage.all("City").values()
            city_list = []
            for city in city_instance:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
