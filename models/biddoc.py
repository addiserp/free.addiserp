#!/usr/bin/python3
""" holds class biddoc"""
import models
from models.base_model import BaseModel, Base
from models.tender import Tender
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Biddoc(BaseModel, Base):
    """Representation of biddoc """
    if models.storage_t == "db":
        __tablename__ = 'biddocs'
        name = Column(String(128), nullable=False)
        url = Column(String(128), nullable=True)
        tenders = relationship("Tender",
                               backref="biddoc",
                               cascade="all, delete, delete-orphan")
    else:
        name = ""
        url = ""

    def __init__(self, *args, **kwargs):
        """initializes bid docs"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def tenders(self):
            """getter for list of tenders instances related to the biddocs"""
            tender_list = []
            all_tenders = models.storage.all(Tender)
            for tender in all_tenders.values():
                if tender.biddoc_id == self.id:
                    tender_list.append(tender)
            return tender_list
