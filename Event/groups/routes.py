from flask import jsonify, Blueprint, request
from Event.models import Groups


groups = Blueprint("groups", __name__, url_prefix="/api/groups")

@groups.route("/<int:group_id>", methods=["PUT"])
def update_group(group_id):
    """
    Update an existing group.

    This route allows updating an existing group's title by providing the group_id in the URL.
    The 'title' parameter must be included in the JSON request body to specify the updated title.

    Args:
        group_id (int): The unique identifier for the group to be updated.

    Returns:
        json: A JSON object containing the updated group information and a success message.

    Raises:
        400 Bad Request: If the 'title' parameter is missing in the request.
        404 Not Found: If the group with the provided group_id is not found.
        500 Internal Server Error: If any server error occurs during the update process.
    """
    try:
        data = request.get_json()
        if 'title' not in data:
            return jsonify({"error": "Missing 'title' in request"}), 400
        
        group = Groups.query.get(group_id)

        if not group:
            return jsonify({"error": f"Group with ID {group_id} not found"}), 404

        group.title = data['title']

        group.update()

        return jsonify({"message": "Group updated successfully", "group": group.format()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500