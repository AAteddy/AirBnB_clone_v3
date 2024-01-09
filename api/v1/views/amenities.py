#!/usr/bin/python3
"""State objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models.amenity import Amenity
from flask import abort, request, jsonify
from models import storage


@app_views.route("/amenities", strict_slashes=False, methods=["GET"])
@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["GET"])
def amenity(amenity_id=None):
    """show amenity and amenity with id using GET method"""
    amenity_list = []
    if amenity_id is None:
        all_objs = storage.all(Amenity).values()
        for k in all_objs:
            amenity_list.append(k.to_dict())
        return jsonify(amenity_list)
    else:
        res = storage.get(Amenity, amenity_id)
        if res is None:
            abort(404)
        return jsonify(res.to_dict())


@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["DELETE"])
def amenity_delete(amenity_id):
    """delete method with Amenity Id"""
    obj = storage.get(Amenity, amenity_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", strict_slashes=False, methods=["POST"])
def create_amenity():
    """create a new Post method req"""
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["PUT"])
def update_amenity(amenity_id):
    """update method with Amenity Id"""
    obj = storage.get(Amenity, amenity_id)
    if obj is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    obj.name = data.get("name", obj.name)
    obj.save()
    return jsonify(obj.to_dict()), 200
