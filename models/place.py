#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float
import models
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False))

class Place(BaseModel):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_unit = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review', cascade="all, delete-orphan", backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                back_populates="place_amenities", viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


    @property
    def reviews(self):
        """Review instances """
        review_inst = models.storage.all('Review').values()
        all_revs = []
        for inst in review_inst:
            if inst.place_id == self.id:
                all_revs.append(inst)
        return all_revs


    if getenv('HBNB_MYSQL_DB') == 'FileStorage':
        @property
        def amenities(self):
            """ Returns a list of amenity instances """
            for amenity in self.amenity_ids:
                amenity_inst = models.storage.all('Review').values()
                all_amenities = []
                for inst in amenity_inst:
                    all_amenities.append[inst]
            return all_amenities

        @amenities.setter
        def amenities(self, obj):
            """ set  """
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)



    def __init__(self, *args, **kwargs):
        """Initialize the place class """
        super().__init__(*args, **kwargs)
