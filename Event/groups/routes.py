"""
Module for removing user from a group.
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


@groups.route("/api/groups/<int:groupId>", methods=["DELETE"])
def delete_group(groupId):
    try:
        # Find the group by its ID
        group_to_delete = Group.query.get(groupId)

        if not group_to_delete:
            return jsonify({"error": "Group not found"}), 404

        # Delete the group from the database
        db.session.delete(group_to_delete)
        db.session.commit()

        return jsonify({"message": "Group deleted successfully"}), 200

    except Exception as e:
        # Handle any exceptions that may occur (e.g., database errors)
        return jsonify({"error": str(e)}), 500

