#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.biddoc import Biddoc

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Biddoc --")
my_biddoc = Biddoc()
my_biddoc.name = "tender doc1"
my_biddoc.url = "https//wwww.doc.com/file1"
my_biddoc.save()
print(my_biddoc)

print("-- Create a new Biddoc 2 --")
my_biddoc2 = Biddoc()
my_biddoc2.name = "tender doc2"
my_biddoc2.url = "https//wwww.doc.com/file2"
my_biddoc2.save()
print(my_biddoc2)

print("-- Create a new Biddoc 3 --")
my_biddoc3 = Biddoc()
my_biddoc3.name = "tender doc3"
my_biddoc3.url = "https//wwww.doc.com/file3"
my_biddoc3.save()
print(my_biddoc3)