#!/usr/bin/python3
""" Index """
from models.biddoc import Biddoc
from models.category import Category
from models.language import Language
from models.region import Region
from models.tender import Tender
from models.user import User
from models.utype import Utype
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Biddoc, Category, Language, Region, Tender, User, Utype]
    names = ["biddocs", "categories", "languages", "regions",
             "tenders", "users", "utype"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
