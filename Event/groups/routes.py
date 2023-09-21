"""
Module for removing user from a group.
"""

from flask import Blueprint, jsonify, request
from Event.models import Users, Groups
from Event import db


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/")
def get_active_signals():
    """
        Retrieve and return active signals.

    Returns:
        str: A placeholder return value.
    """
    return

@groups.route("/api/groups/<group_id>/members/<user_id>", methods=['DELETE'])
def remove_group_member(group_id, user_id):
    """
    Remove a user from a group.

    Parameters:
    group_id (str): The ID of the group.
    user_id (str): The ID of the user to be removed from the group.

    Returns:
    tuple: A tuple containing response message and status code.
    """
    # Retrieve the group and user from the database
    group_id = Users.query.get(group_id)
    user_id = Groups.query.get(user_id)

    # Check if the group and user exist
    if group_id is None or user_id is None:
        return jsonify({"error": "Group or user not found"}), 404

    # Check if the user is a member of the group
    if user_id not in group_id.members:
        return jsonify({"error": "User is not a member of the group"}), 400

    # Remove the user from the group
    group_id.members.remove(user_id)
    db.session.commit()

    return jsonify({"message": "User removed from group successfully"}), 200


@groups.route("/", methods=["POST"])
def create_group():
    """
    Create a new group.

    This route expects a JSON request containing a 'title' key to create a new group.
    The 'title' is used to create a new group instance and insert it into the database.

    Returns:
        JSON response with information about the created group or an error message.
    """
    try:
        # Attempt to extract JSON data from the incoming request.
        data = request.get_json()

        # Check if the 'title' key is present in the JSON data.
        if "title" not in data:
            return jsonify({"error": "Missing 'title' in request"}), 400

        # Extract the 'title' from the JSON data.
        title = data["title"]

        # Create a new group instance with the provided 'title'.
        new_group = Groups(title=title)

        # Insert the new group into the database.
        new_group.insert()

        # Return a JSON response indicating successful group creation.
        return (
            jsonify(
                {"message": "Group created successfully", "group": new_group.format()}
            ),
            201,
        )

    # Handle exceptions and return an error response if any occur.
    except Exception as e:
        return jsonify({"error": str(e)}), 500
