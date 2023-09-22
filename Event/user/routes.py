"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""


from flask import Blueprint, request, jsonify
from Event.models.groups import Groups
from Event import db
from Event.utils import query_one_filtered
from Event.models.users import Users
from Event.models.events import Events
# from Event.models.interested_events import InterestedEvents

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

# Checked
# GET /api/users/<string:user_id>: Get user profile
@users.route("/<string:user_id>", strict_slashes=False)
def get_user_info(user_id: str):
    """gets the user info for the profile page

    Args:  
        user_id (str): the id of the user

    Returns:
        str: details of the user info.

    """
    try:
        user = query_one_filtered(Users, id=user_id)
        # Check if the user is a member of the group
        if user is None:
            return jsonify({"error": "User not found"}), 404
        user_details = user.format()
        return jsonify({
            "status": "success",
            "message": f"user {user_id} details fetched successfully",
            "data": user_details
        })
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return jsonify({
            "status": "failed",
            "message": "your request could not be completed",
            "error": str(error)
        }), 400

# Checked
# PUT /api/users/<string:user_id>: Update user profile
@users.route("/<string:user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id: str):
    """updates the user details

    Args:  
        user_id (str): the id of the user

    Returns:
        str: the new user info.

    """
    try:
        data = request.get_json()
        user = query_one_filtered(Users, id=user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        for key, value in data.items():
            if key == 'id' or key == 'created_at':
                continue
            setattr(user, key, value)
        user.update()
        return jsonify({
            "status": "success",
            "message": f"user {user_id} details updated successfully",
            "data": user.format()
        })
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return jsonify({
            "status": "failed",
            "message": "your request could not be completed",
            "error": str(error)
        }), 400
  

# Checked
# POST /api/users/<string:user_id>/interests/<string:event_id>: Show interests
@users.route("/<string:user_id>/interests/<string:event_id>",
             methods=["POST"], strict_slashes=False)
def create_interest(user_id, event_id):
    """Create interest in an event"""
    try:
        user = query_one_filtered(Users, id=user_id)
        event = query_one_filtered(Events, id=event_id)

        if not user:
            return jsonify({"Error": "User not found"}), 404

        if not event:
            return jsonify({"Error": "Event not found"}), 404

        user.interested_events.append(event)
        user.update()

        return jsonify({"message": "Interest registered"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
