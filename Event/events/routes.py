# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.models.events import Events
from Event.utils import query_all_filtered, query_all, query_one_filtered, format_date, format_time


# url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")


# POST /api/events: Create a new event
@events.route("/", methods=["POST"])
def create_event():
    """
    Create a new event.

    This function handles a POST request to create a new event. It extracts the necessary data from the request's JSON payload, converts the date and time strings to datetime objects, creates an instance of the `Events` model with the extracted data, inserts the event into the database, and returns a JSON response with the created event.

    :return: A JSON response with the following fields:
             - `msg` (string): A message indicating the success of the event creation.
             - `event` (string): A string representation of the created event.
    """


    event = Events(
                    title=request.json['title'],
                   description=request.json['description'],
                   location= request.json['location'],
                   start_date= format_date(
                                                request.json['start_date'],
                                                ),
                   start_time= format_time(
                                                request.json['start_time']
                                                ),  
                   end_date= format_date(
                                                request.json['end_date']
                                                ),
                   end_time=format_time(
                                                request.json['end_time']
                                                ),
                   thumbnail=request.json['thumbnail'],
                   creator=request.json['creator'],
                )
    result = format(event)            
    try:
        event.insert()
    except:
        return {"message": "An error occurred creating the event."}, 400
    return jsonify({
        'msg': "Event Created",
        'event': result }), 201


# DELETE /api/events/:eventId: Delete an event
@events.route("/<id>", methods=["DELETE"])
def delete_event(id):
    """
    Delete an event.

    Args:
        id (str): The id of the event to be deleted.

    Returns:
        If the event is successfully deleted, a success response with status code 204 and a JSON body indicating the event was deleted.
        If the event does not exist, a not found error response with status code 404 and a JSON body indicating the event was not found.
    """

    try:
        del_event = query_one_filtered(table=Events, id=id)

        if del_event:
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 204
    except Exception as error:
        return jsonify(error={"Not Found": "Event not found"}), 404


# GET /api/events: Get a list of events
@events.route("/", methods=["GET"])
def all_events():
    """
    Retrieves all events from the database and returns them as a JSON response.

    Returns:
        json: A JSON response containing all events created.
    """
    all_events = query_all(Events)
    return jsonify(all_events.format()), 200

        
# Get events based on event id
@events.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    """
    Get event based on its ID.

    Args:
        event_id (str): The ID of the event to retrieve.

    Returns:
        tuple: A tuple with the response message and status code.

    Example Usage:
        GET /events/123

    This code snippet demonstrates how to make a GET request to retrieve the event with ID 123.
    The expected output is a JSON response containing the event details if it exists, or an error message if the event is not found.
    """
    try:
        event = query_one_filtered(table=Events, id=event_id)
        if event:
            return jsonify(event.format()), 200

    except Exception as error:
        return jsonify({"error": "Event not found"}), 404


# PUT /api/events/:eventId: Update event details
@events.route("/<event_id>", methods=["PUT"])
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
        db_data = query_all_filtered(Events, id=event_id)
        if not db_data:
            return jsonify({"message": "Event not Found"}), 404
        for k, v in req.items():
            setattr(db_data, k, v)
        Events.update()
        return jsonify({
            "message": "item updated",
            "Event_id": event_id,
            "Event": req}), 201
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@events.route("/<string:event_id>/comments", methods=["GET", "POST"])
def add_comments(event_id):
    """
    Add a comment to an event discussion or fetch all comments for an event.

    Args:
        event_id (str): The ID of the event causing the discussion.

    Returns:
        For POST requests:
            dict: A JSON response with the status, message, and data containing the newly created comment ID and body.
        For GET requests:
            dict: A JSON response with the status, message, and data containing a list of all comments associated with the event.
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
                                "error": str(error)
                            }
                        ), 400

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
                        "message": "Comment data could not be saved",
                        "error": str(error)
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
        # print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occured while fetching all comments",
                    "error": str(error)
                }
            ),
            400,
        )
