from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

# events = Blueprint("events", __name__, url_prefix="/events")#url_prefix includes /events before all endpoints in blueprint
images = Blueprint("images", __name__) #url_prefix includes /events before all endpoints in blueprint


@images.route("/images")
def add_provider():
    return jsonify({"message":"Images table successfully created"})
