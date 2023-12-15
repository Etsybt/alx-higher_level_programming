#!/usr/bin/python3
"""contains the class definition of a State and an instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """inherits from Base

    Attributes:
        id(int): state's id
        name: state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
