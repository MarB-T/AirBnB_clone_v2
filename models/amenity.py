#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float
<<<<<<< HEAD
=======
'''from models.place import place_amenity'''
>>>>>>> f1fda5ff14b50d998008ff680a19bb4cca1d5733


class Amenity(BaseModel, Base):
    """Amenity model/table"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
<<<<<<< HEAD
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity Clas"""
        super().__init__(*args, **kwargs)
=======
'''        place_amenities = relationship(
                'place', secondary=place_amenity, back_populates="amenities")'''
>>>>>>> f1fda5ff14b50d998008ff680a19bb4cca1d5733
