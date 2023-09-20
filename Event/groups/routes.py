from flask import jsonify, Blueprint
from Event.models import Groups

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
    return
