#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
"""cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})"""
cors = CORS(app, resources={r"/*": {"origins": "54.237.68.51"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'Free Addis ERP Restful API',
    'uiversion': 1
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('FREE_API_HOST')
    port = environ.get('FREE_API_PORT')
    if not host:
        host = '54.237.68.51'
    if not port:
        port = '5002'
    app.run(host=host, port=port, threaded=True)
