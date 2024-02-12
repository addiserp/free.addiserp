#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from os import environ
import uuid
from models import storage
from models.region import Region
from models.tender import Tender
from models.category import Category
from models.language import Language
from models.biddoc import Biddoc


app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
# FREE_MYSQL_USER=free_dev FREE_MYSQL_PWD=free_dev_pwd FREE_MYSQL_HOST=localhost FREE_MYSQL_DB=free_dev_db FREE_TYPE_STORAGE=db

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ Free Addis is alive! """
    languages = storage.all(Language).values()
    languages = sorted(languages, key=lambda k: k.name)

    regions = storage.all(Region).values()
    regions = sorted(regions, key=lambda k: k.name)

    catagories = storage.all(Category).values()
    catagories = sorted(catagories, key=lambda k: k.name)
    
    tenders = storage.all(Tender).values()
    tenders = sorted(tenders, key=lambda k: k.name)
    
    return render_template('main-layout.html', categories=catagories,
                           languages=languages, regions=regions,
                           tenders=tenders)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
