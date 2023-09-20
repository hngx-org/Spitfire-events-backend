from flask import Blueprint, request, jsonify
from Event.models.events import Events
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

# events = Blueprint("events", __name__, url_prefix="/events")#url_prefix includes /events before all endpoints in blueprint
events = Blueprint("events", __name__) #url_prefix includes /events before all endpoints in blueprint


@events.route("/events")
def add_provider():
    return jsonify({"message":"Events table successfully created"})
