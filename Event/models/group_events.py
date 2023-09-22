#!/usr/bin/env python3
"""
This the base template for GrouopEvents object instances.
"""
from Event import db
from Event.models.base_model import BaseModel


class GroupEvents(BaseModel):
    """
    Model Schema for GrproupEvents.

    Attributes:
        group_id (str):
            Foreign key for the group table.
        event_id (str):
            Foreign key for the event table.
    """

    __tablename__ = "group_events"
    group_id = db.Column(db.String(120), db.ForeignKey("groups.id"), nullable=False)
    event_id = db.Column(db.String(120), db.ForeignKey("events.id"), nullable=False)

    def __init__(self, group_id, event_id):
        self.group_id = group_id
        self.event_id = event_id

    def format(self):
        """Return a dictionary representation of the Group object"""
        return {"group_id": self.group_id, "event_id": self.event_id}
