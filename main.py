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


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ Free Addis is alive! """
    
    return render_template('main-layout.html',cache_id=str(uuid.uuid4()))

@app.route('/contacts', strict_slashes=False)
def contact():
    """ Free Addis erp contacts page! """
    
    return render_template('pages-contact.html',cache_id=str(uuid.uuid4()))

@app.route('/login', strict_slashes=False)
def login():
    """ Free Addis erp loginpage page! """
    
    return render_template('pages-login.html',cache_id=str(uuid.uuid4()))

@app.route('/register', strict_slashes=False)
def register():
    """ Free Addis erp loginpage page! """
    
    return render_template('pages-register.html',cache_id=str(uuid.uuid4()))

@app.route('/profile', strict_slashes=False)
def profile():
    """ Free Addis erp profile page! """
    
    return render_template('users-profile.html',cache_id=str(uuid.uuid4()))

@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """ Free Addis erp dashboard page! """
    
    return render_template('pages-dashboard.html',cache_id=str(uuid.uuid4()))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
