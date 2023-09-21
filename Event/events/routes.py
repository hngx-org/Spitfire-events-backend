# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.models.events import Events
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
# UPDATE EVENTS
@events.route("/<string:event_id>", methods=["PUT"])
def update_event(event_id):
    """
    Update event details.
    Args:
        event_id (str): The id of the event to be updated.
    Returns:
        Response: JSON response indicating the success or failure of the update.
    """
    try:
        event = Events.query.get(event_id)
        if event is None:
            return jsonify({'error': 'Event not found'}), 404
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        event.location = data.get('location', event.location)
        event.start_date = data.get('start_date', event.start_date)
        event.start_time = data.get('start_time', event.start_time)
        event.end_date = data.get('end_date', event.end_date)
        event.end_time = data.get('end_time', event.end_time)
        event.thumbnail = data.get('thumbnail', event.thumbnail)
        event.update()
        return jsonify({
            'status': 'success',
            'message': 'Event updated successfully',
            'data': {
                'id': event.id,
                'title': event.title,
                'description': event.description,
                'location': event.location,
                'start_date': event.start_date,
                'start_time': event.start_time,
                'end_date': event.end_date,
                'end_time': event.end_time,
                'thumbnail': event.thumbnail
            }
        }), 200
    except ValueError as ve:
        return jsonify({'error': f'Invalid JSON data: {str(ve)}'}), 400
    except Exception as error:
        return jsonify({'error': f'Error updating event: {str(error)}'}), 500
