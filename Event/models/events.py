#!/usr/bin/env python3
"""Base Template for the events class"""
from Event import db
from Event.models.base_model import BaseModel
from datetime import datetime


# Association table between Events and Images
event_thumbnail = db.Table('event_thumbnail',
    db.Column('image_id', db.String(60), db.ForeignKey("images.id"), primary_key=True, nullable=False),
    db.Column('event_id', db.String(60), db.ForeignKey("events.id"), primary_key=True, nullable=False)
)


class Events(BaseModel):
    """_summary_

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_
    """

    __tablename__ = "events"

    # Define columns for the Events table
    title = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(225), nullable=False)
    creator_id = db.Column(
        db.String(60), db.ForeignKey("users.id"), nullable=False
    )
    location = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    start_time = db.Column(db.Time(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    end_time = db.Column(db.Time(), nullable=False)
    comments = db.relationship("Comments", backref=db.backref("event", lazy=True), 
                                cascade="all, delete-orphan")
    thumbnail = db.relationship("Images", secondary=event_thumbnail,
                             backref=db.backref("event", lazy=True), lazy="subquery")


    def __init__(
        self,
        title,
        description,
        creator_id,
        location,
        start_date,
        start_time,
        end_date,
        end_time,
    ):
        """_summary_

        Args:
            title (_type_): _description_
            description (_type_): _description_
            location (_type_): _description_
            start_date (_type_): _description_
            start_time (_type_): _description_
            end_date (_type_): _description_
            end_time (_type_): _description_
        """
        self.title = title
        self.description = description
        self.creator_id = creator_id
        self.location = location
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time

    def __repr__(self):
        """Return a string representation of the Event object"""
        return (
            "Title: {}, Description: {}, Creator Id: {}, Location: {}, "
            "Start Date: {}, Start Time: {}, "
            "End Date: {}, End Time: {}"
        ).format(
            self.title,
            self.description,
            self.creator_id,
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
            "creator_id": self.creator_id,
            "location": self.location,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
