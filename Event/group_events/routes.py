from flask import Blueprint, request, jsonify
from Event.models.group_events import GroupEvents
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db


group_events = Blueprint("group_events", __name__) #url_prefix includes /events before all endpoints in blueprint


@group_events.route("/group_events")
def add_provider():
    return jsonify({"message":"GroupEvents table successfully created"})
