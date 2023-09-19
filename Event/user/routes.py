from Event.models import Users, Groups, get_uuid
from flask import jsonify, Blueprint, request

from Event.utils import query_paginate_filtered, query_one_filtered
from Event import db
import os


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    return

@users.route("/groups", methods=['POST'], strict_slashes=False)
def create_group():
    """just testing"""
    title = request.form.get('title')
    new_group = Groups(title=title)
    new_group.insert()

    return 'success'
