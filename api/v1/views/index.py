#!/usr/bin/python3
""" Index """

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from models import storage

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    resp = {"status": "OK"}
    return jsonify(resp)


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
    amenities = storage.count(Amenity)
    cities = storage.count(City)
    places = storage.count(Place)
    reviews = storage.count(Review)
    states = storage.count(State)
    users = storage.count(User)
    return jsonify({
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
        })
