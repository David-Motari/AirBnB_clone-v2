#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import SELECTED_STORAGE
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if SELECTED_STORAGE == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
