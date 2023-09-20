from Event.models import Users, Groups
from Event import db
from flask import jsonify, Blueprint, request


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    '''get active signals'''
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

    return jsonify({"message": "User remove from group successfully"}), 200
