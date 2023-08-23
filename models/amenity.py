#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.place import place_amenity
<<<<<<< HEAD

=======
>>>>>>> dc9d1beef273acaf4f63833c60c6f23ee3e270c0


class Amenity(BaseModel, Base):
    """Amenity model/table"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                'place', secondary=place_amenity, back_populates="amenities")
