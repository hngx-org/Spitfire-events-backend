"""
Module containing user-related routes for the Events-App, Team Spitfire.
"""

from flask import Blueprint, session, jsonify
from Event.models.users import Users, likes
from Event.models.comments import Comments
from Event.utils import query_all_filtered, is_logged_in, query_one_filtered
from Event import db

likes = Blueprint("likes", __name__, url_prefix="/api/likes")

@likes.route("/<string:comment_id>",
             methods=["POST"],
             strict_slashes=False
             )
def like_comment(comment_id):
    """
    Like a particular comment

    Returns:
        str: A success message.
    """
    # user_id = is_logged_in(session)  #PIN ON THIS
    # print(user_id)
    user_id = "user3_id"

    comment = query_one_filtered(Comments, id=comment_id)
    print(comment)
    user = query_one_filtered(Users, id=user_id)
    print(user)
    if comment in user.likes:
        user.like.pop()
        return jsonify({"message": "Unliked", "comment_id": comment_id}), 201
    # if not like:
    user.likes.append(comment)
    user.update()
    return jsonify({"message": "liked successfully", "comment_id": comment_id}), 201

    
# @likes.route("/<string:comment_id>", methods=["GET"], strict_slashes=False)
# def get_total_likes(comment_id):
#     """
#     Get the total number of likes for a particular comment

#     Returns:
#         str: the count of likes
#     """
#     total_likes = (query_all_filtered(table=Likes, comment_id=comment_id)
#                    .count()
#                    )
#     return jsonify({"message": "success", "total_likes": total_likes}), 200
