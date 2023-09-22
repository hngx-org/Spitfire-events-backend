"""
Module for removing user from a group.
"""

from flask import Blueprint, jsonify, request
from Event.models.users import Users
from Event.models.groups import Groups
from Event import db
from Event.utils import query_one_filtered


groups = Blueprint("groups", __name__, url_prefix="/api/groups")

@groups.route("/<string:groupId>/members/<string:userId>",methods=["POST"])
def add_user_to_group(groupId, userId):
    try:
        group = query_one_filtered(Groups,id=groupId)
        user = query_one_filtered(Users,id=userId)

        # Check if the group and user exist
        if group is None or user is None:
            return jsonify({"error": "Group or user not found"}), 404

        newgroup=user.user_groups
        if group.id in [group.id for group in newgroup ]:
            return jsonify({"error":"forbidden","message":"User already in group"}),403
        newgroup.append(group)

        user.user_groups=newgroup
        user.update()
        
        return jsonify({ "id": group.id, "message": "User added to Group"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@groups.route("/<string:group_id>", methods=["GET"])
def get_group_by_id(group_id):
    """
    Get details of a group by its group ID.

    Args:
        groupId (str): The ID of the group to fetch.

    Returns:
        dict: A JSON response with group details.
    """
    try:
        group = query_one_filtered(Groups,id=group_id)

        if group:
            # Create a dictionary with group details
            group_details = {"id": group.id, "title": group.title}
            return jsonify(
                {
                    "status": "success",
                    "message": "Group details successfully fetched",
                    "data": group_details,
                }
            ), 200
        else:
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": f"Group with groupId {group_id} not found",
                    }
                ),
                404,
            )
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occurred while fetching group details",
                }
            ),
            400,
        )


@groups.route("/<string:group_id>", methods=["PUT"])
def update_group(group_id):
    """
    Update an existing group.

    This route allows updating an existing group's title by providing
    the group_id in the URL.
    The 'title' parameter must be included in the JSON request body to
    specify the updated title.

    Args:
        group_id (int): The unique identifier for the group to be updated.

    Returns:
        json: A JSON object containing the updated group information
        and a success message.

    Raises:
        400 Bad Request: If the 'title' parameter is missing in the request.
        404 Not Found: If the group with the provided group_id is not found.
        400 Internal Server Error: If any server error occurs
        during the update process.
    """
    try:
        data = request.get_json()
        if "title" not in data:
            return jsonify({"error": "Missing 'title' in request"}), 400

        group = query_one_filtered(Groups,id=group_id)

        if not group:
            return (
                jsonify({"error": f"Group with ID {group_id} not found"}),
                404,
            )

        group.title = data["title"]

        group.update()

        return (
            jsonify(
                {
                    "message": "Group updated successfully",
                    "group": group.format(),
                }
            ),
            201,
        )

    except Exception as error:  # pylint: disable=broad-except
        return jsonify({"error": str(error)}), 400


# Define the route to remove a user from a group
@groups.route("/<string:group_id>/members/<string:user_id>", methods=["DELETE"])
def remove_user_from_group(group_id, user_id):
    """
    Remove a user from a group.

    Parameters:
    group_id (str): The ID of the group.
    user_id (str): The ID of the user to be removed from the group.

    Returns:
    tuple: A tuple containing response message and status code.
    """
    try:
        # Check if the group and user exist in the database
        group = query_one_filtered(Groups,id=group_id)
        user = query_one_filtered(Users,id=user_id)

        if group is None or user is None:
            return jsonify({"message": "Group or user not found"}), 404

        user_groups=user.user_groups
        if group_id not in [group.id for group in user_groups ]:
            return jsonify({"error":"forbidden","message":"User is not a member of this group"}),403

        for key,group in enumerate(user.user_groups):
            if group_id==group.id:
                user_groups.pop(key)
        user.user_groups=user_groups
        user.update()

        return jsonify({"message": "User removed from group successfully","group_id":group_id}), 204

    except Exception as e:
        # Handle any potential errors
        return jsonify({"error": str(e)}), 500


@groups.route("/create", methods=["POST"])
def create_group():
    """
    Create a new group.

    This route expects a JSON request containing a 'title' key
    to create a new group.
    The 'title' is used to create a new group instance and
    insert it into the database.

    Returns:
        JSON response with information about the created
        group or an error message.
    """
    try:
        # Attempt to extract JSON data from the incoming request.
        data = request.get_json()

        # Check if the 'title' key is present in the JSON data.
        if "title" not in data:
            return jsonify({"error": "Missing 'title' in request"}), 400

        # Extract the 'title' from the JSON data.
        title = data["title"]

        # Create a new group instance with the provided 'title'.
        new_group = Groups(title=title)

        # Insert the new group into the database.
        new_group.insert()

        # Return a JSON response indicating successful group creation.
        return (
            jsonify(
                {
                    "message": "Group created successfully",
                    "data": new_group.format(),
                }
            ),
            201,
        )

    # Handle exceptions and return an error response if any occur.
    except Exception as error:
        return jsonify({"message": "group creation failed", "error": str(error)}), 400

      
@groups.route("/<string:group_id>", methods=["DELETE"])
def delete_group(group_id):
    """
    Delete a group by its ID.

    Parameters:
    group_id (int): The ID of the group to be deleted.

    Returns:
    tuple: A tuple containing response message and status code.
    """
    try:
        # Retrieve the group from the database
        group = query_one_filtered(Groups,id=group_id)

        # Check if the group exists
        if group is None:
            return jsonify({"error": "Group not found"}), 404

        # Delete the group from the database
        group.delete()

        return jsonify({"message": "Group deleted successfully"}),204

    except Exception as e:
        # Handle any exceptions that may occur during deletion
        return jsonify({"error": str(e)}), 400
