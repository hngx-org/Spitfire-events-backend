from Event.models import Users, Groups, get_uuid
from flask import jsonify, Blueprint, request

from Event.utils import query_paginate_filtered, query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    return
