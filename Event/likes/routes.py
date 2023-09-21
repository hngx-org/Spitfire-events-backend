"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""

from flask import Blueprint, session, jsonify
from Event.models.likes import Likes
from Event.utils import query_all_filtered, is_logged_in
from Event import db

likes = Blueprint("likes", __name__, url_prefix="/api/likes")

@likes.route("/<str: comment_id>",
             methods=["POST"],
             strict_slashes=False
             )
def like_comment(comment_id):
    """
    Like a particular comment

    Returns:
        str: A success message.
    """
    user_id = is_logged_in(session)
    
    like = (
            db.session.execute(
                db.select(Likes)
                .filter_by(comment_id=comment_id)
                .filter_by(user_id=user_id))
            .scalar_one_or_none()
            )
    if not like:
        new_like = Likes(comment_id=comment_id,
                         user_id=user_id,
                         )
        new_like.insert()
    else:
        like.delete()
    return jsonify({"message": "success", "comment_id": comment_id}), 200

@likes.route("/<str: comment_id>", methods=["GET"], strict_slashes=False)
def get_total_likes(comment_id):
    """
    Get the total number of likes for a particular comment

    Returns:
        str: the count of likes
    """
    total_likes = (query_all_filtered(table=Likes, comment_id=comment_id)
                   .count()
                   )
    return jsonify({"message": "success", "total_likes": total_likes}), 200
