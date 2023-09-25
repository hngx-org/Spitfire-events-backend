"""Comments route module"""
from flask import jsonify, Blueprint, request, session
from Event.utils import is_logged_in, query_one_filtered
from Event.models.images import Images
from Event.models.comments import Comments

"""_summary_

    Returns:
        _type_: _description_
    """


comments = Blueprint("comments", __name__, url_prefix="/api/comments")


# POST /api/comments/<comment_id>/images: Add an image or images to a comment
# GET /api/comments/<comment_id>/images: Get all images for a comment
@comments.route("/<comment_id>/images", methods=["GET", "POST"])
def add_images(comment_id):
    """Add an image or images to a comment in an event discussion
    Args:
        comment_id (str): The id of the comment in the discussion
    """
    is_logged_in(session)
    if request.method == "POST":
        response = []
        try:
            comment = query_one_filtered(Comments, id=comment_id)
            image_url_list = request.get_json().get("image_url_list")
            for image_url in image_url_list:
                new_image = Images(url=image_url)
                new_image.insert()
                comment.images.append(new_image)
                comment.update()
                response.append(new_image.format())
            return jsonify(
                {
                    "message": "Image saved successfully",
                    "data": response,
                }
            ), 201
        except Exception as error:
            return jsonify(
                    {
                        "message": "Error: image data could not be saved",
                        "error": "Bad Request"
                    }
                ),  400
    # GET images
    try:
        comment = query_one_filtered(Comments, id=comment_id)
        all_images = comment.images
        return jsonify(
            {
                "message": "all images successfully fetched",
                "data": [image.format() for image in all_images]
                if all_images
                else [],
            }
        ), 200
    except Exception as error:
        return jsonify(
                    {
                        "message": "An error occured while fetching all images",
                        "error": "Bad Request"
                    }
            ), 400
