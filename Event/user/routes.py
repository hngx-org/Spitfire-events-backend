"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""


from flask import Blueprint, request, jsonify, session
from Event import db
from Event.utils import query_one_filtered, is_logged_in
from Event.models.users import Users
from Event.models.events import Events


users = Blueprint("users", __name__, url_prefix="/api/users")



# Checked
# GET /api/users/<string:user_id>: Get user profile
@users.route("/")
def get_user_info():
    """gets the user info for the profile page

    Args:
        user_id (str): the id of the user

    Returns:
        str: details of the user info.

    """
    user_id = is_logged_in(session)
    try:
        user = query_one_filtered(Users, id=user_id)
        # Check if the user is a member of the group
        if user is None:
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "User not found",
                    }
                ),
                404,
            )
        user_details = user.format()
        return (
            jsonify(
                {"message": f"user  details fetched successfully", "data": user_details}
            ),
            200,
        )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "message": "your request could not be completed",
                    "error": "Bad Request",
                }
            ),
            400,
        )


# Checked
# PUT /api/users/<string:user_id>: Update user profile
@users.route("/", methods=["PUT"], strict_slashes=False)
def update_user():
    """updates the user details

    Args:
        user_id (str): the id of the user

    Returns:
        str: the new user info.

    """
    user_id = is_logged_in(session)
    try:
        data = request.get_json()
        user = query_one_filtered(Users, id=user_id)
        if user is None:
            return jsonify({"error": "Not Found", "message": "User not found"}), 404
        for key, value in data.items():
            if key == "id" or key == "created_at":
                continue
            setattr(user, key, value)
        user.update()
        return (
            jsonify(
                {
                    "message": f"user {user_id} details updated successfully",
                    "data": user.format(),
                }
            ),
            201,
        )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "message": "your request could not be completed",
                    "error": "Bad Request",
                }
            ),
            400,
        )


# Checked
# POST /api/users/<string:user_id>/interests/<string:event_id>: Show interests
@users.route(
    "/interests/<string:event_id>",
    methods=["POST"],
    strict_slashes=False,
)
def create_interest(event_id):
    """Create interest in an event"""
    user_id = is_logged_in(session)
    try:
        user = query_one_filtered(Users, id=user_id)
        event = query_one_filtered(Events, id=event_id)

        if not user or not event:
            return (
                jsonify({"Error": "Not Found", "message": "User or Event not found"}),
                404,
            )
        if event not in user.interested_events:
            user.interested_events.append(event)
            user.update()

            return (
                jsonify(
                    {
                        "message": "Interest registered",
                        "data": f"{user_id} has shown interest in {event_id}",
                    }
                ),
                201,
            )
        # else return interest shown already
        return (
            jsonify(
                {
                    "message": "Interest cannot be registered twice",
                    "error": f"{user_id} has shown interest in {event_id} previously",
                }
            ),
            201,
        )

    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({"error": "Bad Request", "message": "Something went wrong"}), 400


# DELETE /api/users/userId/interests/eventId
@users.route("/interests/<string:event_id>", methods=["DELETE"])
def delete_user_interest(event_id):
    """Delete interest in event
    Args:
        user_id: The id of the user
        event_id: the id of the event to be deleted
    Returns:
        str: success msessage
    """
    user_id = is_logged_in(session)
    try:
        user = query_one_filtered(Users, id=user_id)
        event = query_one_filtered(Events, id=event_id)
        if not user or not event:
            return jsonify({"error": "Not Found", "message": "Interest not found"}), 404
        new_interested_events = user.interested_events

        for key, interest in enumerate(user.interested_events):
            if event.id == interest.id:
                new_interested_events.pop(key)
        user.interested_events = new_interested_events
        user.update()

        return jsonify({"message": "Interest deleted", "data": "No content"}), 204
    except Exception as error:
        print(str(error))
        return jsonify({"error": "Bad Request", "message": "Something went wrong"}), 400
