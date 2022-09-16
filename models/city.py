#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.__init__ import storage
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import getenv


SELECTED_STORAGE = getenv("HBNB_TYPE_STORAGE")
if SELECTED_STORAGE == "db":
    class City(BaseModel, Base):
        """This is the class for City Attributes"""
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")
else:
    class City(BaseModel):
        """
        This is the class for City
        """
        state_id = ""
        name = ""
