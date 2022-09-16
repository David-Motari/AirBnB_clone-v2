#!/usr/bin/python3
"""This is the amenity class"""
from models import place
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


SELECTED_STORAGE = environ.get("HBNB_TYPE_STORAGE")
if SELECTED_STORAGE == "db":
    class Amenity(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "PlaceAmenity", backref="amenities", cascade="all, delete")

       # def __init__(self, **kwargs):
           # setattr(self, "id", str(uuid4()))
           # for k, v in kwargs.items():
               # setattr(self, k, v)
else:
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
            name: input name
        """
        name = ""
