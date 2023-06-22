#!/usr/bin/python3

""" State class an instance of the Base class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Attributes:
         __tablename__ (str): name of the table
         id (int), name(str): a column in the named table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
