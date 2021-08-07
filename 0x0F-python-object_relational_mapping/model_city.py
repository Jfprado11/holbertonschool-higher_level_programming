#!/usr/bin/python3
""" contains the class definition of a
City form base in mdel_state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """cretes a table for states"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
