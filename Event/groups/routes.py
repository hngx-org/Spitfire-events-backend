from flask import jsonify, Blueprint
from Event.utils import query_paginate_filtered, query_one_filtered
"""
Module for removing user from a group.
"""
from Event.models import Users, Groups
from Event import db


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/<id>", methods=["GET"])
def get_group(id):
    try: 
        get_group= query_one_filtered(table=Groups, id=id)
        
        if not get_group:
            return jsonify({"message" : "Group not found"}), 404
        return jsonify(get_group), 200
    except Exception as e:
        #Handle other errors
        jsonify({"error" : e}), 400

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
