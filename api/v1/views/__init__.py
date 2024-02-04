#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.category import *
from api.v1.views.tenders import *
from api.v1.views.regions import *
from api.v1.views.biddocs import *
from api.v1.views.users import *
from api.v1.views.tenders_categories import *
from api.v1.views.tenders_users import *
