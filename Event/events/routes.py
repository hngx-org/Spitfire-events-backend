from flask import Blueprint, request, jsonify
from Event.models import User
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db

events = Blueprint("events", __name__, url_prefix="/events")


@events.route("/", methods=["POST"])
def add_provider():
    return
