#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.region import Region

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new region --")
my_region = Region()
my_region.name = "Addis Ababa"
my_region.save()
print(my_region)

print("-- Create a new region 2 --")
my_region2 = Region()
my_region2.name = "Adama"
my_region2.save()
print(my_region2)

print("-- Create a new region 2 --")
my_region3 = Region()
my_region3.name = "Dire dewa"
my_region3.save()
print(my_region3)