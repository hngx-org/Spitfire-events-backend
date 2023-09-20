from Event.models import User, UserGroups
from flask import jsonify, Blueprint

from Event.utils import query_paginate_filtered, query_one_filtered


users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    return


@users.route("/api/groups/:groupId/members/:userId", methods=['DELETE'])
def remove_group_member(group_id, user_id):
    group_id = User.query.get(group_id)
    user_id = UserGroups.query.get(user_id)
    
    return jsonify({"message": "User remove from group successfully"}), 200
