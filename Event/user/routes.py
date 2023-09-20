# pylint: disable=cyclic-import
"""_summary_
    """
# pylint: disable=unused-import
from flask import jsonify, Blueprint
from Event.models import Users
from Event.utils import query_paginate_filtered, query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    """_summary_
    """
    return
