#!/usr/bin/python3

""" City class an instance of the Base class """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """
    Attributes:
         __tablename__ (str): name of the table
         id (int), name(str): a column in the named table
         state_id (int): foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
