#!/usr/bin/env python3
"""Template for the Comment Class"""

from Event import db
from Event.models.base_model import BaseModel
from datetime import datetime


# Association table between Comments and Images
comment_images = db.Table('comment_images',
    db.Column('comment_id', db.String(60), db.ForeignKey("comments.id"), primary_key=True,nullable=False),
    db.Column('image_id', db.String(60), db.ForeignKey("images.id"), primary_key=True, nullable=False)
)

class Comments(BaseModel):
    """
    Model schema for the comments in the events section
    Attributes:
            id (str):
                Primary key for the table
            event_id (str):
                Foreign key for the event table
            user_id (str):
                Foreign key for the user table
            body (str):
                The comment body
            image (str):
                The image associated with the comment
            event (Event):
                The relationship to the event table
            user (User):
                The relationship to the user table
    Methods:
            __init__(self,event_id,user_id, body, image ):
              Constructor for the EventComment class.
            __repr__(self):
              Representation of the EventComment class.
            insert(self): Inserts a new EventComment object into the db.
            update(self): Updates an existing EventComment object in the db.
            delete(self): Deletes an existing EventComment object from the db.
            format(self): Returns a dict repr of the EventComment obj.


        Examples:
            comment = Comments(event_id=1, user_id=1,
                               body="This is a comment",
                               image="https://www.google.com")
    """

    __tablename__ = "comments"

    # Define columns for the Users table
    event_id = db.Column(db.String(60), db.ForeignKey("events.id"), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    # Add relationships to Events and Users models

    # event = db.relationship("Events", backref=db.backref("comments", lazy=True))
    # user = db.relationship("Users", backref=db.backref("comments", lazy=True))
    images = db.relationship("Images", backref="comments", secondary=comment_images, lazy="dynamic")

    def __init__(self, event_id, user_id, body):
        """Initialize the Comment object"""
        self.body = body
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        """Return a string representation of the Comment object"""
        return "event_id: {}, user_id: {}, body: {}, created_at: {}, updated_at: {}".format(
            self.event_id, self.user_id, self.body, self.created_at, self.updated_at
        )

    def format(self):
        """Return a dictionary representation of the Comment object"""
        return {
            "id": self.id,
            "event_id": self.event_id,
            "user_id": self.user_id,
            "body": self.body,
            "created_at": self.body,
            "updated_at": self.updated_at,
            # "images": [image.format() for image in self.images]
        }
