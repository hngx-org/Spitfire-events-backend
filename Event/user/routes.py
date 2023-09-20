from Event.models import Users, Groups, get_uuid
from flask import jsonify, Blueprint, request

from Event.utils import query_paginate_filtered, query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    return

@users.route("/groups", methods=['POST'], strict_slashes=False)
def create_group():
    """just testing"""
    title = request.form.get('title')
    new_group = Groups(title=title)
    new_group.insert()

    return 'success'

@users.route("/api/groups/:groupId/members/:userId", methods=['DELETE'])
def remove_group_member(group_id, user_id):
    """
    Remove a user from a group.

    Parameters:
    group_id (str): The ID of the group.
    user_id (str): The ID of the user to be removed from the group.

    Returns:
    tuple: A tuple containing response message and status code.
    """
    group_id = Users.query.get(group_id)
    user_id = Groups.query.get(user_id)

    return jsonify({"message": "User remove from group successfully"}), 200
