"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""

from flask import Blueprint, jsonify, request
from Event.models.users import Users
from Event.utils import query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    """
        Retrieve and return active signals.

    Returns:
        str: A placeholder return value.
    """
    return


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
        user = query_one_filtered(Users, user_id=user_id)
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
        user = query_one_filtered(Users, user_id=user_id)
        for key, value in data.items():
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
