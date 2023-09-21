#!/usr/bin/env python3
"""Template for the User Class"""

from Event import db
from Event.models.base_model import BaseModel


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
    access_token = db.Column(db.String(120), nullable=False)
    refresh_token = db.Column(db.String(120), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)

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
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
        }
