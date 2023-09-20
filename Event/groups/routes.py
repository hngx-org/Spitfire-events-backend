"""
Module for removing user from a group.
"""

from flask import Blueprint, jsonify
from Event.models import Users, Groups
from Event import db


groups = Blueprint("groups", __name__, url_prefix="/api/groups")



@groups.route("/<string:groupId>", methods=["GET"])
def get_group_by_id(groupId):
    """
    Get details of a group by its group ID.

    Args:
        groupId (str): The ID of the group to fetch.

    Returns:
        dict: A JSON response with group details.
    """
    try:
        group = Groups.query.filter_by(group_id=groupId).first()
        
        if group:
            # Create a dictionary with group details
            group_details = {
                "group_id": group.group_id,
                "title": group.title
            }
            return jsonify({
                "status": "success",
                "message": "Group details successfully fetched",
                "data": group_details
            })
        else:
            return jsonify({
                "status": "failed",
                "message": f"Group with groupId {groupId} not found"
            }), 404
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
        return jsonify({
            'status': 'failed',
            'message': 'An error occurred while fetching group details'
        }), 500
        


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
