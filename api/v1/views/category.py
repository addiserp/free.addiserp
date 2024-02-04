#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """
from models.category import Category
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
@swag_from('documentation/category/get_category.yml', methods=['GET'])
def get_categories():
    """
    Retrieves the list of all Category objects
    """
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return jsonify(list_categories)


@app_views.route('/categories/<category_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/category/get_id_category.yml', methods=['get'])
def get_category(category_id):
    """ Retrieves a specific Category """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)

    return jsonify(category.to_dict())


@app_views.route('/categories/<category_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/category/delete_category.yml', methods=['DELETE'])
def delete_category(category_id):
    """
    Deletes a Category Object
    """

    category = storage.get(Category, category_id)

    if not category:
        abort(404)

    storage.delete(category)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
@swag_from('documentation/category/post_category.yml', methods=['POST'])
def post_category():
    """
    Creates a Category
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Category(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/categories/<category_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/category/put_category.yml', methods=['PUT'])
def put_category(category_id):
    """
    Updates a Category
    """
    category = storage.get(Category, category_id)

    if not category:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(category, key, value)
    storage.save()
    return make_response(jsonify(category.to_dict()), 200)
