#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
import uuid


class Place(BaseModel):
    """ A place to stay """
    def __init__(self, *args, **kwargs):
        """ Initializes the state """
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])
