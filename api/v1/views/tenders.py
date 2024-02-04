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

@app_views.route('/tender_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/place/post_search.yml', methods=['POST'])
def tender_search():
    """
    Retrieves all tender objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        categories = data.get('htmlcata', None)
        regions = data.get('regions', None)
        languages = data.get('languages', None)

    if not data or not len(data) or (
            not categories and
            not regions and
            not languages):
        tenders = storage.all(Tender).values()
        list_tenders = []
        for tender in tenders:
            list_tenders.append(tenders.to_dict())
        return jsonify(list_tenders)

    list_tenders = []
    if categories:
        categories_obj = [storage.get(Category, s_id) for s_id in categories]
        for category in categories_obj:
            if category:
                for tend in category.tenders:
                    if regions:
                        for tendera in tenders.regions:
                            list_tenders.append(tendera)
    """
    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for place in city.places:
                    if place not in list_places:
                        list_places.append(place)

    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]
    """
    places = []
    for p in list_tenders:
        d = p.to_dict()
        d.pop('languages', None)
        places.append(d)

    return jsonify(places)