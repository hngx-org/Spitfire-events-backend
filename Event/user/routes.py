from Event.models import Users, UserGroups, get_uuid
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
    group_id = Users.query.get(group_id)
    user_id = Groups.query.get(user_id)
    
    return jsonify({"message": "User remove from group successfully"}), 200

@users.route("/")
def get_active_signals():
    return


@users.route("/api/groups/:groupId/members/:userId", methods=['DELETE'])
def remove_group_member(group_id, user_id):
    """
    """
    # Check if passed params exist
    user_group = UserGroups.query.filter_by(group_id=group_id, user_id=user_id).first()
    # Return error if user not found
    if not user_group:
        response = {
                'error': 'Not found',
                'message': 'User not found in the group'
                }
        return jsonify(response)

    # Delete user from group and commit to database
    user_group.delete()
    # Return success message
    return jsonify({"message": "User removed from group successfully"}), 200
