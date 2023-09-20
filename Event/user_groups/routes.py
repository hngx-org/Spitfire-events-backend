from flask import Blueprint, request, jsonify
from Event.models.user_groups import UserGroups
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

# events = Blueprint("events", __name__, url_prefix="/events")#url_prefix includes /events before all endpoints in blueprint
user_groups = Blueprint("user_groups", __name__) #url_prefix includes /events before all endpoints in blueprint


@user_groups.route("/user_groups")
def add_provider():
    return jsonify({"message":"UserGroups table successfully created"})
