from flask import Blueprint, request, jsonify
from Event.models import Users, Events
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

# url_prefix includes /events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/events")


@events.route("/api/events/<id>", methods=["DELETE"])
def delete_event(id):
    del_event = query_one_filtered(Events, id)
    if del_event:
        del_event.delete()
        return jsonify(response={"success": "Event deleted."}), 200
    else:
        return jsonify(error={"Not Found": "Event not found."}), 404
