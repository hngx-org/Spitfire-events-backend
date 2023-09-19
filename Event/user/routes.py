from Event.models import User
from flask import jsonify, Blueprint

from Event.utils import query_paginate_filtered, query_one_filtered
from Event import db
import os


users = Blueprint("users", __name__)


@users.route("/")
def get_active_signals():
    return
