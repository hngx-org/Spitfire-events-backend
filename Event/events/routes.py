from flask import Blueprint, request, jsonify
from Event.models import Users
from Event.models import Events
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
    query_all
)
from Event import db

events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint


#Get all events
@events.route("/", methods=["GET"])
def all_events():
    try:
        all_events = query_all(Events)       
        return jsonify(all_events), 200
    
    except Exception as e:
        if not all_events:
            # No events found
            return jsonify({"message": "No events found"}), 404
        else:
            return jsonify({
                "error": "An error occured",
                "error_message": e
                }), 400
        