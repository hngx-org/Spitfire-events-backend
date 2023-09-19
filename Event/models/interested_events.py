#!/usr/bin/env python3
"""
This the base template for all IntresedeEvents object instances.
"""
from Event import db
from models.base_model import BaseModel


class InterestedEvents(BaseModel):
    """InterestedEvents class"""
    __tablename__ = "interested_events"
    user_id = (
            db.Column
            (
                db.String(120),
                db.ForeignKey("users.id"),
                nullable=False
            )
        )
    event_id = (
            db.Column
            (
                db.String(120),
                db.ForeignKey("events.id"),
                nullable=False
            )
        )

    def __init__(self, user_id, event_id):
        self.user_id = user_id
        self.event_id = event_id
