#!/usr/bin/python3
"""Dbase storage engine that uses SQLAlchemy"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """A class for db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """iinitializes the class dbstorage"""
        eng = 'mysql+mysqldb://{}:{}@{}/{}'\
                .format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST', 'localhost'),
                getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(eng, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dict of objects present"""


    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads objects in dbase"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

