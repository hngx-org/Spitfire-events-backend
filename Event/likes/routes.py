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
             methods=["GET"],
             )
def number_of_likes(comment_id):
    """
    Retrieves the number of likes for a given comment.

    Args:
        comment_id (string): The ID of the comment for which to retrieve the number of likes.

    Returns:
        JSON response: A JSON response containing the number of likes for the given comment.

    Example Usage:
        GET /likes/12345
        Input: comment_id = "12345"
        Output: 
        {
          "message": "Number of likes",
          "data": 5
        }
    """
    try:
        comment = query_one_filtered(Comments, id=comment_id)
        if not comment:
            return jsonify(
                {
                    "error": "Not Found",
                    "message": "Event Not Found",
                }
            )
        number_of_likes = len(comment.user_likes)
        return jsonify(
            {
                "message": "Number of likes", 
                "data": number_of_likes
            }
        ), 200
    
    except Exception as exc:
        return jsonify(
            {
                "error": "Forbidden",
                "message": "you are not allowed to perform such actions",
            }
        ), 403





# @likes.route("/<string:comment_id>",
#              methods=["POST"],
#              )
# def like_comment(comment_id):
#     """
#     Like a particular comment

#     Returns:
#         str: A success message.
#     """

#     #UNCOMMENT THIS IN PRODUCTION
#     # user_id = is_logged_in(session)  
#     # print(user_id)
#     user_id = "user3_id"


#     #THIS GETS THE COMMENT OBJECT    
#     try:
#         user = query_one_filtered(Users, id=user_id)
#         comment = query_one_filtered(Comments, id=comment_id)
#         if not comment or not user:
#             return jsonify(
#                 {
#                     "error": "Not Found",
#                     "message": "Event Not Found",
#                 }
#             )
#         number_of_likes = len(comment.user_likes)
#         return jsonify(
#             {
#                 "message": "Number of likes", 
#                 "data": number_of_likes
#                 }
#                 ), 200
    
#     except Exception as exc:
#         return jsonify(
#             {
#                 "error": "Forbidden",
#                 "message": "you are not allowed to oerform such actions",
#             }
#         ), 403

