#!/usr/bin/python3
"""sets new engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Handles storage using a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        mysql_user = os.getenv('HBNB_MYSQL_USER')
        mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        mysql_database = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_ENV')

        db_url = (
            f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/"
            f"{mysql_database}"
            )

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def all(self, cls=None):
        """Query objects from the current database session"""
        if cls is None:
            return {
                    obj.__class__.__name__ + '.' + obj.id: obj
                    for obj in (
                        self.__session.query(User).all() +
                        self.__session.query(State).all() +
                        self.__session.query(City).all() +
                        self.__session.query(Amenity).all() +
                        self.__session.query(Place).all() +
                        self.__session.query(Review).all()
                        )
                    }
        else:
            return {
                    obj.__class__.__name__ + '.' + obj.id: obj
                    for obj in self.__session.query(cls).all()
                    }

    def new(self, obj):
        """Add an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session_factory()
