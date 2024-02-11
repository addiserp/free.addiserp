#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage
from models.language import Language
from api.v1.views import app_views


@app_views.route('/languages', methods=['GET'], strict_slashes=False)
@swag_from('documentation/language/get_language.yml', methods=['GET'])
def get_Languages():
    """
    Retrieves the list of all Language objects
    """
    all_Languages = storage.all(Language).values()
    list_Languages = []
    for language in all_Languages:
        list_Languages.append(language.to_dict())
    return jsonify(list_Languages)


@app_views.route('/languages/<language_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/Language/get_id_Language.yml', methods=['get'])
def get_Language(language_id):
    """ Retrieves a specific Language """
    language = storage.get(Language, language_id)
    if not language:
        abort(404)

    return jsonify(language.to_dict())


@app_views.route('/languages/<language_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/language/delete_language.yml', methods=['DELETE'])
def delete_Language(language_id):
    """
    Deletes a Language Object
    """

    language = storage.get(Language, language_id)

    if not language:
        abort(404)

    storage.delete(language)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/languages', methods=['POST'], strict_slashes=False)
@swag_from('documentation/Language/post_language.yml', methods=['POST'])
def post_language():
    """
    Creates a Language
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Language(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/languages/<language_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/language/put_language.yml', methods=['PUT'])
def put_language(language_id):
    """
    Updates a Language
    """
    language = storage.get(Language, language_id)

    if not language:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(language, key, value)
    storage.save()
    return make_response(jsonify(language.to_dict()), 200)

