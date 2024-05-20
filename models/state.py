#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import uuid
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class  that  inherits from BaseModel and Base"""
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City',
            backref='State',
            cascade='all, delete-orphan'
            )

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances"""
        from models.city import City
        all_cities = storage.all(City)
        state_cities = []
        for City in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
