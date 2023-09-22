# #!/usr/bin/env python3
# """Template for the Like Class"""

# from Event import db
# from Event.models.base_model import BaseModel


# class Likes(BaseModel):
#     """
#     Model Schema for Likes

#     """

#     __tablename__ = "likes"
    
#     comment_id = db.Column(db.String(60), db.ForeignKey("comments.id"), primary_key=True, nullable=False)
#     user_id = db.Column(db.String(60), db.ForeignKey("users.id"), primary_key=True, nullable=False)

#     def __init__(self, comment_id, user_id):
#         self.comment_id = comment_id
#         self.user_id = user_id

#     def __repr__(self):
#         """Return a string representation of the Like object"""
#         return "Comment: {}, User: {},".format(
#             self.comment_id, self.user_id,
#         )

#     def format(self):
#         """Return a dictionary representation of the Like object"""
#         return {
#             "comment_id": self.comment_id,
#             "user_id": self.user_id
#         }
