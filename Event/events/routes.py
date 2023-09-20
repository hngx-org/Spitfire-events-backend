from flask import Blueprint, request, jsonify
from Event.models import Users, Events
from Event.utils import (
    query_one_filtered
)


events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint



@events.route("/<id>", methods=["DELETE"])
def delete_event(id):
    try:
        del_event = query_one_filtered(table=Events, id=id)

        if del_event:
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 204
    except Exception as error:
        return jsonify(error={"Not Found": "Event not found"}), 404
