#!/usr/bin/python
""" holds class Category"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of Category """

    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Category"""
        super().__init__(*args, **kwargs)
