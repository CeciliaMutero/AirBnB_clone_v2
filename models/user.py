#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base



class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

engine = create_engine('mysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
