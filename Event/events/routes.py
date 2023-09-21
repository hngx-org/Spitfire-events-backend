# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.models import Events
from Event.utils import query_all_filtered, query_all, query_one_filtered


# url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")

# DELETE /api/events/:eventId: Delete an event
@events.route("/<id>", methods=["DELETE"])
def delete_event(id):
    """Delete an event
    Args:
        id (str): The id of the event
    """

    try:
        del_event = query_one_filtered(table=Events, id=id)

        if del_event:
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 204
    except Exception as error:
        return jsonify(error={"Not Found": "Event not found"}), 404

        
# Get events based on event id
@events.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    """
        Get event using event_id
        Args:
            event_id: Id of event to get
        Returns:
            a tuple with response message and status code
    """
    try:
        event = query_one_filtered(table=Events, id=event_id)  
        if event:
            return jsonify(event.format()), 200
    
    except Exception as error:
        return jsonify({"error": "Event not found"}), 404


# PUT /api/events/:eventId: Update event details
events.route("/<event_id>", methods=["PUT"])
def update_event(event_id: str) -> tuple:
    """
    Updates an event in the database based on the provided event ID and request data.
    Args:
        event_id (str): The ID of the event to be updated.
    Returns:
        tuple: A JSON response with a message and a status code.
    Raises:
        Exception: If an error occurs during the update process.
    """
    try:
        req = request.get_json()
        db_data = query_one_filtered(Events, id=event_id)
        
        if not db_data:
            return jsonify({"message": "Event not Found"}), 404
        for k, v in req.items():
            setattr(db_data, k, v)
        Events.update()
        return jsonify({"message": "item updated"}), 201
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


# POST /api/events/<str:event_id>/comments: Add a comment to an event
# GET /api/events/<str:event_id>/comments: Get comments for an event
@events.route("/<string:event_id>/comments", methods=["GET", "POST"])
def add_comments(event_id):
    """Add a comment to an event discussion
    Args:
        event_id (str): The id of the event causing the discussion

    Returns:
        str: the id of the newly created comment for POST

        list: a list of all comments attached to an event
    """
    if request.method == "POST":
        try:
            data = request.get_json()
            user_id = data.get("user_id")
            body = data.get("body")
            image_url_list = data.get("image_url_list", None)
            new_comment = Comments(
                event_id=event_id, user_id=user_id, body=body
            )
            new_comment.insert()
            # save images if they exist
            if image_url_list is not None:
                for image_url in image_url_list:
                    new_image = Images(new_comment.id, image_url)
                    try:
                        new_image.insert()
                    except Exception as error:
                        print(f"{type(error).__name__}: {error}")
                        return jsonify(
                            {
                                "status": "failed",
                                "message": "Failed to save to database",
                            }
                        )

            return jsonify(
                {
                    "status": "success",
                    "message": "Comment saved successfully",
                    "data": {"id": new_comment.id, "body": new_comment.body},
                }
            )
        except Exception as error:
            print(f"{type(error).__name__}: {error}")
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "Error: Comment data could not be saved",
                    }
                ),
                400,
            )

    # GET comments
    try:
        all_comments = query_all_filtered("comments", event_id=event_id)
        return jsonify(
            {
                "status": "success",
                "message": "all comments successfully fetched",
                "data": [comment.format() for comment in all_comments]
                if all_comments
                else [],
            }
        )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occured while fetching all comments",
                }
            ),
            400,
        )
