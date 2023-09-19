from flask import Blueprint, request, jsonify
from Event.models import User
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

events = Blueprint("events", __name__, url_prefix="/events")#url_prefix includes /events before all endpoints in blueprint


@events.route("/", methods=["POST"])
def add_provider():
    return


# Get events based on event id
@events.route("/api/events/<string:eventId>", methods=["GET"])
def get_event(eventId):
    try:
        event = query_one_filtered(events, id=eventId)
        return jsonify(event.format()), 200
    except Exception as error:
        if not event:
            return jsonify({"error": "Event not found"}), 404
        else:
            return jsonify({
                "error": "An error occured",
                "error_message": error
                }), 500
