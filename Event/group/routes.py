from Event.models.groups import Groups
from Event.models.base_model import get_uuid
from flask import jsonify, Blueprint

from Event.utils import query_paginate_filtered, query_one_filtered
from Event import db
import os


groups = Blueprint("groups", __name__)


@groups.route("/groups")
def get_active_signals():
    return jsonify({"message": "Group table Successfully Created"})
