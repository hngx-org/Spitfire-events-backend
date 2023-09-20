from flask import Blueprint, request, jsonify
from Event.models.likes import Likes
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db


likes = Blueprint("likes", __name__) #url_prefix includes /events before all endpoints in blueprint


@likes.route("/likes")
def add_provider():
    return jsonify({"message": "Likes table successfully created"})
