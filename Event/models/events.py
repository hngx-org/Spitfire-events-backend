#!/usr/bin/env python3
"""Base Template for the events class"""
from Event import db
from Event.models.base_model import BaseModel


class Events(BaseModel):
    """Event model"""

    __tablename__ = "events"

    # Define columns for the Events table
    title = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(225), nullable=False)
    creator = db.Column(
        db.String(60), db.ForeignKey("users.id"), nullable=False
    )
    location = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    start_time = db.Column(db.Time(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    end_time = db.Column(db.Time(), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)

    def __init__(
        self,
        title,
        description,
        creator,
        location,
        start_date,
        start_time,
        end_date,
        end_time,
        thumbnail,
    ):
        """Initialize the Event object"""
        self.title = title
        self.description = description
        self.creator = creator
        self.location = location
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.thumbnail = thumbnail

    def __repr__(self):
        """Return a string representation of the Event object"""
        return (
            "Title: {}, Description: {}, Creator: {}, Location: {}, "
            "Start Date: {}, Start Time: {}, "
            "End Date: {}, End Time: {}"
        ).format(
            self.title,
            self.description,
            self.creator,
            self.location,
            self.start_date,
            self.start_time,
            self.end_date,
            self.end_time,
        )

    # Override the format method to return event attributes as a dictionary
    def format(self):
        """Return a dictionary representation of the Event object"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "location": self.location,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "thumbnail": self.thumbnail,
        }
