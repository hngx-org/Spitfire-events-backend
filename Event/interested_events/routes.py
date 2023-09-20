from flask import Blueprint, request, jsonify
from Event.models.interested_events import InterestedEvents
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db


interested_events = Blueprint("interested_events", __name__) #url_prefix includes /events before all endpoints in blueprint


@interested_events.route("/interested_events")
def add_provider():
    return jsonify({"message":"InterestedEvents table successfully created"})