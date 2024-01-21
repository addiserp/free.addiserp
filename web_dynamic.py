#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.region import Region
from models.tender import Tender
from models.category import Category
from models.biddoc import Biddoc
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ Free Addis is alive! """
    regions = storage.all(Region).values()
    regions = sorted(regions, key=lambda k: k.name)
    st_ct = []

    """for region in regions:
        st_ct.append([region, sorted(region.tenders, key=lambda k: k.name)])
    """
    catagories = storage.all(Category).values()
    catagories = sorted(catagories, key=lambda k: k.name)

    tenders = storage.all(Tender).values()
    tenders = sorted(tenders, key=lambda k: k.name)

    return render_template('main-layout.html',
                           cata=catagories,
                           )


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
