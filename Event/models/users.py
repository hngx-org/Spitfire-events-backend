#!/usr/bin/env python3
"""Template for the User Class"""

from Event import db
from Event.models.base_model import BaseModel
from datetime import datetime


# Association table between Events and Users
interested_events = db.Table('interested_events',
    db.Column('user_id', db.String(60), db.ForeignKey("users.id"), primary_key=True, nullable=False),
    db.Column('event_id', db.String(60), db.ForeignKey("events.id"), primary_key=True, nullable=False)
)
# Association table between Users and Groups
user_groups = db.Table('user_groups',
    db.Column('user_id', db.String(60), db.ForeignKey("users.id"), primary_key=True, nullable=False),
    db.Column('group_id', db.String(60), db.ForeignKey("groups.id"), primary_key=True, nullable=False)
)
# Association table between Users and Comments
likes = db.Table('likes',
    db.Column('user_id', db.String(60), db.ForeignKey("users.id"), primary_key=True, nullable=False),
    db.Column('comment_id', db.String(60), db.ForeignKey("comments.id"), primary_key=True, nullable=False)
)



class Users(BaseModel):
    """User model"""

    __tablename__ = "users"

    # Override the id attribute to have a different type
    id = db.Column(
        db.String(60), primary_key=True, unique=True, nullable=False
    )

    # Define columns for the Users table
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    # one to many relationships
    comments = db.relationship("Comments", backref=db.backref("commenter", lazy=True), 
                           cascade="all, delete-orphan")
    # created_groups = db.relationship("Groups", backref=db.backref("creator", lazy=True), 
    #                        cascade="all, delete-orphan")
    # many to many relationships
    user_groups = db.relationship("Groups", backref=db.backref("members", lazy=True),
                                  secondary=user_groups, cascade="delete")
    interested_events = db.relationship("Events", backref=db.backref("interested_users", lazy=True),
                                        secondary=interested_events, cascade="delete")
    likes = db.relationship("Comments", backref=db.backref("user_likes", lazy=True),
                            secondary=likes, cascade="delete")

    def __init__(self, id, name, email, avatar):
        """_summary_

        Args:
            id (_type_): _description
            name (_type_): _description_
            email (_type_): _description_
            avatar (_type_): _description_
        """
        self.id = id
        self.name = name
        self.email = email
        self.avatar = avatar

    def __repr__(self):
        """Return a string representation of the User object"""
        return "Id: {}, Name: {}, Email: {}".format(
            self.id, self.name, self.email
        )

    # Override the format method to return event attributes as a dictionary
    def format(self):
        """Return a dictionary representation of the User object"""
        return {
            "id":self.id if self.id else "",
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
            "created_at": format(self.created_at),
            "updated_at": format(self.updated_at)
        }
