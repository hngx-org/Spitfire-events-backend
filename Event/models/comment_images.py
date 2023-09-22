#!/usr/bin/env python3
"""Template for the CommentImages Class"""

from Event import db
from Event.models.base_model import BaseModel


# class CommentImages(db.Model):
#     """CommentImages class"""
#     __tablename__ = "comment_images"

#     comment_id = db.Column(db.String(60), db.ForeignKey("comments.id"),
#                            primary_key=True, nullable=False)
#     image_id = db.Column(db.String(60), db.ForeignKey("images.id"),
#                          primary_key=True, nullable=False)

#     def __init__(self, comment_id, image_id):
#         """_summary_

#         Args:
#             comment_id (_type_): _description_
#             image_id (_type_): _description_
#         """
#         self.comment_id = comment_id
#         self.image_id = image_id

#     def insert(self):
#         """Insert the current object into the database"""
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         """Update the current object in the database"""
#         db.session.commit()

#     def delete(self):
#         """Delete the current object from the database"""
#         db.session.delete(self)
#         db.session.commit()


#     def __repr__(self):
#         """
#         Return a string representation of the CommentImages object.
#         This method is automatically called when the object is printed or
#         when the `repr()` function is used. It returns a formatted string
#         containing the CommentImages object's identifier.

#         Returns:
#             str: A string representation of the CommentImages object.
#         """
#         return "id: {}, comment_id: {}, image_id: {}".format(self.id, self.comment_id, self.image_id)

#     def format(self):
#         """
#         Return a dictionary representation of the CommentImages object.
#         This method is automatically called when the object is printed or
#         when the `format()` function is used. It returns a dictionary
#         containing the CommentImages object's attributes.
#         """
#         return {
#             "comment_id": self.comment_id,
#             "image_id": self.image_id
#         }
    
# comment_images = db.Table('comment_images',
#     comment_id = db.Column(db.String(60), db.ForeignKey("comments.id"), primary_key=True, nullable=False),
#     image_id = db.Column(db.String(60), db.ForeignKey("images.id"), primary_key=True, nullable=False)
# )