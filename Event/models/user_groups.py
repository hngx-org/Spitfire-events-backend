#!/usr/bin/env python3
"""
This the base template for UserGroup object instances.
"""
from Event import db
from Event.models.base_model import BaseModel


class UserGroups(BaseModel):
    """
    Model Schema for usergroups.

    Attributes:
        user_id (str):
            Foreign key for the user table.
        group_id (str):
            Foreign key for the group table.
    """

    __tablename__ = "user_groups"
    user_id = db.Column(
        db.String(120), db.ForeignKey("users.id"), nullable=False
    )
    group_id = db.Column(
        db.String(120), db.ForeignKey("groups.id"), nullable=False
    )

    def __init__(self, user_id, group_id):
        """Initialize the UserGroup object"""
        self.user_id = user_id
        self.group_id = group_id

    def format(self):
        """Return a dictionary representation of the UserGroup object"""
        return {"user_id": self.user_id, "group_id": self.group_id}
