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

@users.route("/groups", methods=['POST'], strict_slashes=False)
def create_group():
    """just testing"""
    title = request.form.get('title')
    new_group = Groups(title=title)
    new_group.insert()

    return 'success'
