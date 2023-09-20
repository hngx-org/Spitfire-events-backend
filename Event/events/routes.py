from flask import Blueprint, request, jsonify
from Event.models import Users, Comments, Images
from Event.utils import (
    query_one_filtered,
    query_all_filtered,
    query_paginate_filtered,
    query_paginated,
)

#url_prefix includes /api/events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events") 

"""
POST /api/events/<event_id>/comments: Add a comment to an event
GET /api/events/<event_id>/comments: Get comments for an event
"""
@events.route("/<event_id>/comments", methods=["GET", "POST"])
def add_comments(event_id):
    """Add a comment to an event discussion
    Args:
        event_id (str): The id of the event causing the discussion

    Returns: 
        str: the id of the newly created comment for POST

        list: a list of all comments attached to an event
    """
    if request.method == 'POST':
        try:
            user_id = request.get_json().get('user_id')
            body = request.get_json().get('body')
            image_url_list = request.get_json().get('image_url_list', None)
            print('here')
            new_comment = Comments(event_id=event_id, user_id=user_id, body=body)
            new_comment.insert()
            # save images if they exist
            if image_url_list is not None:
                for image_url in image_url_list:
                    new_image = Images(new_comment.id, image_url)
                    new_image.insert()

            return jsonify({
                'status': 'success',
                'message': 'Comment saved successfully',
                'data': {
                    'id': new_comment.id,
                    'body': new_comment.body
                }
            })
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
            return jsonify({
                'status': 'failed',
                'message': 'Comment data could not be saved, an error occured',
            }), 400
    
    # GET comments
    try:
        all_comments = query_all_filtered('comments', event_id=event_id)
        return jsonify({
            'status': 'success',
            'message': 'all comments successfully fetched',
            'data': all_comments
        })
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return jsonify({
            'status': 'failed',
            'message': 'An error occured while fetching all comments'
        }), 400


# """
# POST /api/comments/<comment_id>/images: Add an image to a comment
# GET /api/comments/<comment_id>/images: Get images for a comment
# """
# @events.route("/<comment_id>/images", methods=["GET", "POST"])
# def add_images(comment_id):
#     """Add an image or images to a comment in an event discussion
#         Args:
#             comment_id (str): The id of the comment in the discussion
#     """
#     if request.method == 'POST':
#         try:
#             image_url = request.get_json().get('image_url')
#             new_image = Images(comment_id, image_url)
#             new_image.insert()
#             return jsonify({
#                 'status': 'success',
#                 'message': 'Image saved successfully',
#                 'data': {
#                     'id': new_image.id,
#                     'image_url': new_image.image_url
#                 }
#             })
#         except Exception as error:
#             print(f'{type(error).__name__}: {error}')
#             return jsonify({
#                 'status': 'failed',
#                 'message': 'image data could not be saved, an error occured',
#             }), 400
    
#     # GET images
#     try:
#         all_images = query_all_filtered('images', comment_id=comment_id)
#         return jsonify({
#             'status': 'success',
#             'message': 'all images successfully fetched',
#             'data': all_images
#         })
#     except Exception as error:
#         print(f'{type(error).__name__}: {error}')
#         return jsonify({
#             'status': 'failed',
#             'message': 'An error occured while fetching all images'
#         }), 400
