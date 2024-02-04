#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Tenders """
from models.biddoc import Biddoc
from models.category import Category
from models.language import Language
from models.region import Region
from models.tender import Tender
from models.user import User
from models.utype import Utype
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/regions/<region_id>/tenders', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/tender/get_tenders.yml', methods=['GET'])
def get_tenders(region_id):
    """
    Retrieves the list of all Tender objects of a Region
    """
    region = storage.get(Region, region_id)

    if not region:
        abort(404)

    tenders = [tender.to_dict() for tender in region.tenders]

    return jsonify(tenders)


@app_views.route('/tenders/<tender_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tender/get_tender.yml', methods=['GET'])
def get_tender(tender_id):
    """
    Retrieves a Tender object
    """
    tender = storage.get(Tender, tender_id)
    if not tender:
        abort(404)

    return jsonify(tender.to_dict())


@app_views.route('/tenders/<tender_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/tender/delete_tender.yml', methods=['DELETE'])
def delete_tender(tender_id):
    """
    Deletes a Tender Object
    """

    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    storage.delete(tender)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/regions/<region_id>/tenders', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/tender/post_tender.yml', methods=['POST'])
def post_tender(region_id):
    """
    Creates a Tender
    """
    region = storage.get(Region, region_id)

    if not region:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data["region_id"] = region_id
    instance = Tender(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/tenders/<tender_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/tender/put_tender.yml', methods=['PUT'])
def put_tender(tender_id):
    """
    Updates a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'region_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(tender, key, value)
    storage.save()
    return make_response(jsonify(tender.to_dict()), 200)


@app_views.route('/tenders_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/tender/post_search.yml', methods=['POST'])
def tenders_search():
    """
    Retrieves all Tender objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):

        regions = data.get('regions', None)
        categories = data.get('categories', None)

    if not data or not len(data) or (
            not regions and
            not categories):
        tenders = storage.all(Tender).values()
        list_tenders = []
        for tender in tenders:
            list_tenders.append(tender.to_dict())
        return jsonify(list_tenders)

    list_tenders = []

    if regions:
        region_obj = [storage.get(Region, c_id) for c_id in regions]
        for region in region_obj:
            if region:
                for tender in region.tenders:
                    if tender not in list_tenders:
                        list_tenders.append(tender)

    if categories:
        if not list_tenders:
            list_tenders = storage.all(Tender).values()
        categories_obj = [storage.get(Category, a_id) for a_id in categories]
        list_tenders = [tender for tender in list_tenders
                        if all([am in tender.categories
                               for am in categories_obj])]

    tenders = []
    for p in list_tenders:
        d = p.to_dict()
        d.pop('categories', None)
        tenders.append(d)

    return jsonify(tenders)
