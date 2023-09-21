# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.utils import query_all_filtered

# url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")


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

# import Events model
from Event.models.events import Events

# POST /api/events: Create a new event
@events.route("/", methods=["POST"])
def create_event():
    try:
        data = request.get_json()
        # Extract event data from JSON request
        title = data.get("title")
        description = data.get("description")
        creator = data.get("creator")
        location = data.get("location")
        start_date = data.get("start_date")
        start_time = data.get("start_time")
        end_date = data.get("end_date")
        end_time = data.get("end_time")
        thumbnail = data.get("thumbnail")
        # Create a new event object
        new_event = Events(
            title=title, 
            description=description, 
            creator=creator,
            location=location,
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            thumbnail=thumbnail
            )
        new_event.insert()  # Insert the event into the database
        return jsonify(
            {
                "status": "success",
                "message": "Event created successfully",
                "data": {"id": new_event.id},
            }
        ), 201  # Return HTTP status code 201 (Created)
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return jsonify(
            {"status": "failed", "message": "Error: Event could not be created"}, 400
        )

# GET /api/events: Get a list of events
@events.route("/", methods=["GET"])
def get_events():
    try:
        all_events = query_all_filtered("events")
        return jsonify(
            {
                "status": "success",
                "message": "Events retrieved successfully",
                "data": [event.format() for event in all_events] if all_events else [],
            }
        )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occurred while fetching events",
                }
            ),
            400,
        )

# GET /api/events/:eventId: Get event details
@events.route("/<string:event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event = Events.query.get(event_id)
        if event:
            return jsonify(
                {
                    "status": "success",
                    "message": "Event details retrieved successfully",
                    "data": event.format(),
                }
            )
        else:
            return (
                jsonify(
                    {"status": "failed", "message": "Event not found"},
                ),
                404,  # Return HTTP status code 404 (Not Found)
            )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occurred while fetching event details",
                }
            ),
            400,
        )

# PUT /api/events/:eventId: Update event details
@events.route("/<string:event_id>", methods=["PUT"])
def update_event(event_id):
    try:
        event = Events.query.get(event_id)
        if event:
            data = request.get_json()
            # Update event data from JSON request
            event.title = data.get("title", event.title)
            event.description = data.get("description", event.description)
            event.creator = data.get("creator", event.creator)
            event.location = data.get("location", event.location)
            event.start_date = data.get("start_date", event.start_date)
            event.start_time = data.get("start_time", event.start_time)
            event.end_date = data.get("end_date", event.end_date)
            event.end_time = data.get("end_time", event.end_time)
            event.thumbnail = data.get("thumbnail", event.thumbnail)

            event.update()  # Update the event in the database
            return jsonify(
                {
                    "status": "success",
                    "message": "Event updated successfully",
                    "data": event.format(),
                }
            )
        else:
            return (
                jsonify(
                    {"status": "failed", "message": "Event not found"},
                ),
                404,
            )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occurred while updating event details",
                }
            ),
            400,
        )

# DELETE /api/events/:eventId: Delete an event
@events.route("/<string:event_id>", methods=["DELETE"])
def delete_event(event_id):
    try:
        event = Events.query.get(event_id)
        if event:
            event.delete()  # Delete the event from the database
            return jsonify(
                {
                    "status": "success",
                    "message": "Event deleted successfully",
                    "data": {"id": event.id},
                }
            )
        else:
            return (
                jsonify(
                    {"status": "failed", "message": "Event not found"},
                ),
                404,
            )
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occurred while deleting the event",
                }
            ),
            400,
        )
