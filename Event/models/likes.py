#!/usr/bin/env python3
"""Template for the Like Class"""

from Event import db
from Event.models.base_model import BaseModel


class Likes(BaseModel):
    """
    Model Schema for Likes

    """
    __tablename__ = "likes"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False)

    def __init__(self, user_id, event_id, comment_id):
        self.user_id = user_id
        self.event_id = event_id
        self.comment_id = comment_id

    def __repr__(self):
        """Return a string representation of the Like object"""
        return "User: {}, Event: {}, Comment: {}".format(self.user_id, self.event_id, self.comment_id)

    def format(self):
        """Return a dictionary representation of the Like object"""
        return {
            "user_id": self.user_id,
            "event_id": self.event_id,
            "comment_id": self.comment_id
        }