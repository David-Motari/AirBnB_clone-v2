#!/usr/bin/python3
"""This is the amenity class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


s = getenv("HBNB_TYPE_STORAGE")
if s == "db":
    class Amenity(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
            name: input name
        """
        name = ""
