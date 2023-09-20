from flask import Blueprint, request, jsonify
from Event.models.comments import Comments
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)
from Event import db


comments = Blueprint("comments", __name__) #url_prefix includes /events before all endpoints in blueprint


@comments.route("/comments")
def add_provider():
    return jsonify({"message":"Comments table successfully created"})
