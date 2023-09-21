"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""

from flask import Blueprint, request, jsonify, abort
from Event import db
from Event.models.groups import Groups
from Event.models.interested_events import InterestedEvents
from Event.models.users import Users
from Event.models.events import Events
from Event.utils import query_one_filtered

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


@users.route("/<string:userId>/interests/<string:eventId>",
             methods=["POST"], strict_slashes=False)
def create_interest(userId, eventId):
    """Create interest in an event"""
    try:
        user = query_one_filtered(Users, id=userId)
        event = query_one_filtered(Events, id=eventId)

        if not user:
            abort(404, description="User not found")

        if not event:
            abort(404, description="Event not found")

        new_interest = InterestedEvents(user_id=user.id, event_id=event.id)
        new_interest.insert()
        
        return jsonify({"success": "Interest registered"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
