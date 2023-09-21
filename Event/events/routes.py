# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models.images import Images
from Event.models.comments import Comments
from Event.models import Events
from Event.utils import query_all_filtered, query_all

# url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")


# POST /api/events: Create a new event
@events.route("/", methods=["POST"])
def create_event():

    title = request.json['title']
    description = request.json['description']
    location = request.json['location']
    start_date = request.json['start_date']
    start_time = request.json['start_time']
    end_date = request.json['end_date']
    end_time = request.json['end_time']
    thumbnail = request.json['thumbnail']
    creator = request.json['creator']

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    start_time = datetime.strptime(start_time,'%H:%M')
    end_time = datetime.strptime(end_time,'%H:%M')
    
    event = Events(title=title,description=description,location=location,start_date=start_date,start_time=start_time,  end_date=end_date,end_time=end_time,thumbnail=thumbnail,creator=creator)

    result = format(event)            
    try:
        event.insert()
    except:
        return {"message": "An error occurred creating the event."}, 400
    return jsonify({
        'msg': "Event Created",
        'event': result }), 201  


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
