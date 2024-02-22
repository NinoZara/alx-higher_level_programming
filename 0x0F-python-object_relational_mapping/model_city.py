#!/usr/bin/python3
""" contains the class definition of a City and an instance"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
        """Represents a City class that inherits from Base"""
            __tablename__ = 'cities'
                id = Column(Integer, unique=True, nullable=False, primary_key=True)
                    name = Column(String(128), nullable=False)
                        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
