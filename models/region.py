#!/usr/bin/python3
""" holds class State"""
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.tender import Tender


class Region(BaseModel, Base):
    """Representation of region """
    if models.storage_t == "db":
        __tablename__ = 'regions'
        name = Column(String(128), nullable=False)
        tenders = relationship("Tender",
                               backref="region",
                               cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes region"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def tenders(self):
            """getter for list of tenders instances related to the region"""
            tender_list = []
            all_tenders = models.storage.all(Tender)
            for tender in all_tenders.values():
                if tender.region_id == self.id:
                    tender_list.append(tender)
            return tender_list
