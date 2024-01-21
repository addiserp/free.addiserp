#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.tender import Tender
from datetime import datetime

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Tender --")
my_tender = Tender()
my_tender.name = "tender 1"
my_tender.region_id = "a770f7f1-f229-4a16-86e8-c9654409e932"
my_tender.ann_date = ""
my_tender.closing_date = ""
my_tender.head_content = "top contentts 1"
my_tender.main_content = "main contentts 1"
my_tender.foot_content = "foot contentts 1"
my_tender.tender_version = 1
my_tender.biddoc_id = "311969bf-d266-42c3-b097-8345b13c06a0"
my_tender.save()
print(my_tender)

print("-- Create a new Tender 2 --")
my_tender2 = Tender()
my_tender2.name = "tender 2"
my_tender2.region_id = "c9325781-b1ce-4ce0-9c7a-20b32c5babe7"
my_tender2.ann_date = ""
my_tender2.closing_date = ""
my_tender2.head_content = "top contentts 2"
my_tender2.main_content = "main contentts 2"
my_tender2.foot_content = "foot contentts 2"
my_tender2.tender_version = 2
my_tender2.biddoc_id = "7061f4a6-13bd-4dc7-a7cb-6d64b4a3f82b"
my_tender2.save()
print(my_tender2)
