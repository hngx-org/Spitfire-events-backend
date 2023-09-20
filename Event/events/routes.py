from flask import Blueprint, request, jsonify
from Event.models import Users, Groups
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)

events = Blueprint("events", __name__, url_prefix="/api/events")#url_prefix includes /events before all endpoints in blueprint



@events.route("/", methods=["POST"])
def add_provider():
    return


groups = Blueprint("groups", __name__, url_prefix="/api/groups")
@groups.route("/<string:groupId>", methods=["GET"])
def get_group_by_id(groupId):
    try:
        group = Groups.query.filter_by(group_id=groupId).first()
        
        if group:
            group_details = {
                "group_id": group.group_id,
                "title": group.title
            }
            return jsonify({
                "status": "success",
                "message":"Group details successfully fetched",
                "data": group_details
            })
        else:
            return jsonify({
                "status": "failed",
                "message": f"Group with groupId {groupId} not found"
            }),404
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
        return jsonify({
            'status': 'failed',
            'message': 'An error occurred while fetching group details'
        }), 500
    