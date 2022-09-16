#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base, BaseModel
from models.__init__ import storage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os

SELECTED_STORAGE = os.environ.get("HBNB_TYPE_STORAGE")
if SELECTED_STORAGE == "db":
    class State(BaseModel, Base):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan")

       # def __init__(self, *args, **kwargs):
           # super().__init__(*args, **kwargs)

else:
    name = ""
    @property
    def cities(self):
        all_cities = models.storage.all("City")
        temp = []
        for c_id in all_cities:
            if all_cities[c_id].state_id == self.id:
                temp.append(all_cities[c_id])
        return temp
