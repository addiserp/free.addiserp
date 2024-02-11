#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import BaseModel, Base
from models.region import Region
from models.tender import Tender
from models.category import Category
from models.biddoc import Biddoc
from models.user import User
from models.utype import Utype
from models.language import Language


classes = {"Category": Category, "BaseModel": BaseModel, "Tender": Tender,
           "Region": Region, "Biddoc": Biddoc, "User": User,
           "Utype": Utype, "Language": Language}


class DBStorage:
    """interaacts with the MySQL database"""
    engine = None
    session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        FREE_MYSQL_USER = "free_dev1"
        FREE_MYSQL_PWD = "free_dev_pwd1"
        FREE_MYSQL_HOST = "localhost"
        FREE_MYSQL_DB = "free_dev_db1"
        FREE_ENV = getenv('FREE_ENV1')
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(FREE_MYSQL_USER,
                                             FREE_MYSQL_PWD,
                                             FREE_MYSQL_HOST,
                                             FREE_MYSQL_DB))
        if FREE_ENV == "test":
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.engine)
        sess_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.session.remove()

    def get(self, cls, id):
        """
            Get A method to retrieve one object:
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for v in all_cls.values():
            if (v.id == id):
                return v
        return None

    def count(self, cls=None):
        """
            count A method to count the number of objects in storage:
        """
        all_class = classes.values()

        if not cls:
            cnt = 0
            for c in all_class:
                cnt += len(models.storage.all(c).values())
        else:
            cnt = len(models.storage.all(cls).values())
        return cnt
