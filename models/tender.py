#!/usr/bin/python
""" holds class Tender"""

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Text, BOOLEAN
from sqlalchemy import DateTime, Float, Table
from sqlalchemy.orm import relationship
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from models.category import Category



tender_category = Table('tender_category', Base.metadata,
                        Column('tender_id', String(60),
                                ForeignKey('tenders.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                            primary_key=True),
                        Column('category_id', String(60),
                                ForeignKey('categories.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                            primary_key=True))
my_favorite = Table('my_favorite', Base.metadata,
                        Column('tender_id', String(60),
                                ForeignKey('tenders.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                primary_key=True),
                        Column('user_id', String(60),
                                ForeignKey('users.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                primary_key=True))

class Tender(BaseModel, Base):
    """Representation of tender """

    __tablename__ = 'tenders'
    region_id = Column(String(60), ForeignKey('regions.id'),
                        nullable=False)
    biddoc_id = Column(String(60), ForeignKey('biddocs.id'),
                        nullable=False)
    language_id = Column(String(60), ForeignKey('languages.id'), nullable=False)
    name = Column(String(128), nullable=False)
    doc_price = Column(Integer, nullable=False, default=0)
    ann_date = Column(DateTime, default=datetime.utcnow)
    closing_date = Column(DateTime, default=datetime.utcnow)
    head_content = Column(Text, nullable=True)
    main_content = Column(Text, nullable=True)
    foot_content = Column(String(128), nullable=True)
    tender_version = Column(Integer, nullable=False, default=0)
    isactive = Column(BOOLEAN, nullable=False, default=True)
    categories = relationship("Category",
                                secondary=tender_category,
                                viewonly=False)
    myfavorites = relationship("User",
                                secondary=my_favorite,
                                viewonly=False)

    

    def __init__(self, *args, **kwargs):
        """initializes Tenders"""
        super().__init__(*args, **kwargs)
