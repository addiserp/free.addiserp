#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Tender - Category
"""
from models.tender import Tender
from models.category import Category
from models import storage
from api.v1.views import app_views
from os import environ
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('tenders/<tender_id>/categories', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/tender_category/get_tenders_categories.yml',
           methods=['GET'])
def get_tender_categories(tender_id):
    """
    Retrieves the list of all Category objects of a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)


    categories = [category.to_dict() for category in tender.categories]


    return jsonify(categories)


@app_views.route('/tenders/<tender_id>/categories/<category_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/tender_category/delete_tender_categories.yml',
           methods=['DELETE'])
def delete_tender_category(tender_id, category_id):
    """
    Deletes a Category object of a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    category = storage.get(Category, category_id)

    if not category:
        abort(404)


    if category not in tender.categories:
        abort(404)
    tender.categories.remove(category)


    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/tenders/<tender_id>/categories/<category_id>',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/tender_category/post_tender_categories.yml',
           methods=['POST'])
def post_tender_category(tender_id, category_id):
    """
    Link a Category object to a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    category = storage.get(Category, category_id)
    if not category:
        abort(404)


    if category in tender.categories:
        return make_response(jsonify(category.to_dict()), 200)
    else:
        tender.categories.append(category)


    storage.save()
    return make_response(jsonify(category.to_dict()), 201)
