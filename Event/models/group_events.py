#!/usr/bin/env python3
"""
This the base template for all IntresedeEvents object instances.
"""
from Event import db
from models.base_model import BaseModel


class GroupEvents(BaseModel):
    """InterestedEvents class"""
    __tablename__ = "group_events"
    group_id = (
            db.Column
            (
                db.String(120),
                db.ForeignKey("groups.id"),
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

    def __init__(self, group_id, event_id):
        self.group_id = group_id
        self.event_id = event_id
