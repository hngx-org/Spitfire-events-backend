# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.models.events import Events
# from Event.models.comment_images import CommentImages
from Event.utils import query_all_filtered, query_all, query_one_filtered, format_date, format_time


# url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")

# checked
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
    # destructure the request dict to kwargs
    try:
        data = {item for item in dict(request.json).items() if 'thumbnail' not in item}
        print(f"data: {dict(data)}")
        event = Events(**dict(data))
        result = format(event)            
        event.insert()
        thumbnail = request.json['thumbnail']
        new_image = Images(url=thumbnail)
        new_image.insert()
        event.thumbnail.append(new_image)
        event.update()
    except:
        return {"message": "An error occurred creating the event."}, 400
    return jsonify({
        'message': "Event Created",
        'data': result 
    }), 201

# to check later
# DELETE /api/events/:eventId: Delete an event
@events.route("/<string:id>", methods=["DELETE"])
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
        del_event = query_one_filtered(Events, id=id)
        print(del_event)
        if del_event:
            print('in')
            del_event.delete()
            return jsonify(response={"success": "Event deleted"}), 200
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return jsonify(error="an error has occured, couldn't complete request"), 400
    
    # if no event was found and no error was raised
    return jsonify(error={"Not Found": "Event not found"}), 404

# checked
# GET /api/events: Get a list of events
@events.route("/", methods=["GET"])
def all_events():
    """
    Retrieves all events from the database and returns them as a JSON response.

    Returns:
        json: A JSON response containing all events created.
    """
    try:
        all_events = query_all(Events)
    except Exception:
        return jsonify({"error": "events not found"})
    
    return jsonify({
        "status": "success", 
        "message": "events returned succesfully", 
        "data": format(all_events)
    }), 200

# Checked  
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
            return jsonify({
                "status": "success", 
                "message": "event returned succesfully", 
                "data": format(event)
            }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 404

# checked
# PUT /api/events/:eventId: Update event details
@events.route("/<string:event_id>", methods=["PUT"])
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
            print(db_data)
            if k == 'creator_id':
                continue
            setattr(db_data, k, v)
        db_data.update()
        return jsonify({
            "message": "item updated",
            "Event_id": event_id,
            "data": format(db_data)}), 201
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}")
        return jsonify({"error": str(exc)}), 400

# checked
@events.route("/<string:event_id>/comments", methods=["GET", "POST"])
def add_comments(event_id: str):
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
            new_comment = Comments(event_id=event_id, user_id=user_id,
                                   body=body)
            new_comment.insert()
            # save images if they exist
            if image_url_list is not None:
                for image_url in image_url_list:
                    new_image = Images(url=image_url)
                    try:
                        new_image.insert()
                        # comment_image = CommentImages(comment_id=new_comment.id,
                        #                               image_id=new_image.id)
                        # comment_image.insert()
                        new_comment.images.append(new_image)
                        new_comment.update()
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
        all_comments = query_all_filtered(Comments, event_id=event_id)
        if all_comments is None:
            return jsonify({"status": "failed", "message": "comments not found"}), 404
        # if found
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
                    "error": str(error)
                }
            ),
            400,
        )
