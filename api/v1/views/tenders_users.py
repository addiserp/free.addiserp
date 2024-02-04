#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Tender - User
"""
from models.tender import Tender
from models.user import User
from models import storage
from api.v1.views import app_views
from os import environ
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('tenders_users/<tender_id>/users', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/tenders_users/get_tenders_users.yml',
           methods=['GET'])
def get_tender_users(tender_id):
    """
    Retrieves the list of all User selects as favorie objects of a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)


    users = [user.to_dict() for user in tender.myfavorites]


    return jsonify(users)


@app_views.route('/tenders_users/<tender_id>/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/tenders_user/delete_tenders_users.yml',
           methods=['DELETE'])
def delete_tender_user(tender_id, user_id):
    """
    Deletes a User object of a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    user = storage.get(User, user_id)

    if not user:
        abort(404)


    if user not in tender.myfavorites:
        abort(404)
    tender.users.remove(user)


    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/tenders_users/<tender_id>/users/<user_id>',
                 methods=['POST'], strict_slashes=False)
@swag_from('documentation/tender_users/post_tenders_users.yml',
           methods=['POST'])
def post_tender_user(tender_id, user_id):
    """
    Link a User object to a Tender
    """
    tender = storage.get(Tender, tender_id)

    if not tender:
        abort(404)

    user = storage.get(User, user_id)
    if not user:
        abort(404)


    if user in tender.myfavorites:
        return make_response(jsonify(user.to_dict()), 200)
    else:
        tender.myfavorites.append(user)


    storage.save()
    return make_response(jsonify(user.to_dict()), 201)
