# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models import Users
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)

# url_prefix includes /events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")


@events.route("/", methods=["POST"])
def add_provider():
    """_summary_
    """
    return
