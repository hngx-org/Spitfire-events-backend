#!/usr/bin/env python3
"""Template for the User Class"""

from Event import db
from models.base_model import BaseModel


class Users(BaseModel):
    """User model"""
    __tablename__ = "users"

    # Define columns for the Users table
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access_token = db.Column(db.String(120), nullable=False)
    refresh_token = db.Column(db.String(120), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, avatar):
        """Initialize the User object"""
        self.name = name
        self.email = email
        self.avatar = avatar

    def __repr__(self):
        """Return a string representation of the User object"""
        return 'Name: {}, Email: {}'.format(self.name, self.email)

    # Override the format method to return event attributes as a dictionary
    def format(self):
        """Return a dictionary representation of the User object"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "avatar": self.avatar,
        }
