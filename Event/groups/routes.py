rom Event.models import User
from flask import jsonify, Blueprint

from Event.utils import query_paginate_filtered, query_one_filtered


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@users.route("/")
def get_active_signals():
    return