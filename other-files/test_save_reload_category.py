#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.category import Category

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Category --")
my_category = Category()
my_category.name = "Agricalture"
my_category.save()
print(my_category)

print("-- Create a new Category 2 --")
my_category2 = Category()
my_category2.name = "Software"
my_category2.save()
print(my_category2)

print("-- Create a new Category 3 --")
my_category3 = Category()
my_category3.name = "Consulting"
my_category3.save()
print(my_category3)