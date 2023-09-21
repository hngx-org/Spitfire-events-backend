"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""

from flask import Blueprint, request
from Event.models.groups import Groups

# from Event.utils import query_paginate_filtered, query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    """
        Retrieve and return active signals.

    Returns:
        str: A placeholder return value.
    """
    return


@users.route("/groups", methods=["POST"], strict_slashes=False)
def create_group():
    """
     Create a new group.

    Returns:
        str: A success message.
    """
    title = request.form.get("title")
    new_group = Groups(title=title)
    new_group.insert()
