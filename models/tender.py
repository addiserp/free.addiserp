#!/usr/bin/python
""" holds class Tender"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship


class Tender(BaseModel, Base):
    """Representation of tender """
    if models.storage_t == "db":
        __tablename__ = 'tenders'
        region_id = Column(String(60), ForeignKey('regions.id'),
                           nullable=False)
        name = Column(String(128), nullable=False)
        ann_date = Column(DateTime, default=datetime.utcnow)
        closing_date = Column(DateTime, default=datetime.utcnow)
        head_content = Column(String(128), nullable=True)
        main_content = Column(String(128), nullable=True)
        foot_content = Column(String(128), nullable=True)
        tender_version = Column(Integer, nullable=False, default=0)
        biddoc_id = Column(String(60), ForeignKey('biddocs.id'), nullable=False)
        """ places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
        """
    else:
        region_id = ""
        name = ""
        ann_date = ""
        closing_date = ""
        head_content = ""
        main_content = ""
        foot_content = ""
        tender_version = 0
        biddoc_id = ""
    def __init__(self, *args, **kwargs):
        """initializes Tenders"""
        super().__init__(*args, **kwargs)
