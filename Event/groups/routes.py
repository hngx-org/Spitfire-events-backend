"""
Module for removing a user from a group.
"""

from flask import Blueprint, jsonify
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
    return ""


@groups.route("/api/groups/<group_id>/members/<user_id>", methods=['DELETE'])
def remove_group_member(group_id, user_id):
    """
    Remove a user from a group.

    Parameters:
    group_id (str): The ID of the group.
    user_id (str): The ID of the user to be removed from the group.

    Returns:
    tuple: A tuple containing a response message and status code.
    """
    # Retrieve the group and user from the database
    group = Groups.query.get(group_id)
    user = Users.query.get(user_id)

    # Check if the group and user exist
    if group is None or user is None:
        return jsonify({"error": "Group or user not found"}), 404

    # Check if the user is a member of the group
    if user not in group.members:
        return jsonify({"error": "User is not a member of the group"}), 400

    # Remove the user from the group
    group.members.remove(user)
    db.session.commit()

    return jsonify({"message": "User removed from the group successfully"}), 200


@groups.route("/<int:group_id>", methods=["DELETE"])
def delete_group(group_id):
    try:
        # Retrieve the group from the database
        group = Groups.query.get(group_id)

        # Check if the group exists
        if group is None:
            return jsonify({"error": "Group not found"}), 404

        # Delete the group from the database
        db.session.delete(group)
        db.session.commit()

        return jsonify({"message": "Group deleted successfully"}), 200

    except Exception as e:
        # Handle any exceptions that may occur during deletion
        return jsonify({"error": str(e)}), 500

