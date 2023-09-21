"""Comments route module"""
from flask import jsonify, Blueprint, request
from Event.utils import query_all_filtered
from Event.models.images import Images


comments = Blueprint("comments", __name__, url_prefix="/api/comments")


# POST /api/comments/<comment_id>/images: Add an image to a comment
# GET /api/comments/<comment_id>/images: Get images for a comment
@comments.route("/<comment_id>/images", methods=["GET", "POST"])
def add_images(comment_id):
    """Add an image or images to a comment in an event discussion
    Args:
        comment_id (str): The id of the comment in the discussion
    """
    if request.method == "POST":
        try:
            image_url = request.get_json().get("image_url")
            new_image = Images(comment_id, image_url)
            new_image.insert()
            return jsonify(
                {
                    "status": "success",
                    "message": "Image saved successfully",
                    "data": {
                        "id": new_image.id,
                        "image_url": new_image.image_url,
                    },
                }
            )
            # pylint: disable=broad-exception-caught
        except Exception as error:
            print(f"{type(error).__name__}: {error}")
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "Error: image data could not be saved",
                    }
                ),
                400,
            )

    # GET images
    try:
        all_images = query_all_filtered("images", comment_id=comment_id)
        return jsonify(
            {
                "status": "success",
                "message": "all images successfully fetched",
                "data": [comment.format() for comment in all_images]
                if all_images
                else [],
            }
        )
                    # pylint: disable=broad-exception-caught
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return (
            jsonify(
                {
                    "status": "failed",
                    "message": "An error occured while fetching all images",
                }
            ),
            400,
        )
