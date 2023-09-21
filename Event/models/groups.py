#!/usr/bin/env python3
"""Template for the Groups Class"""

from Event import db
from Event.models.base_model import BaseModel
from datetime import datetime


class Groups(BaseModel):
    """
    Model Schema for groups.

    Attributes:
        title (str):
            The title of the group.

    Methods:
        __init__(self, title):
            Constructor for the Groups class.
        __repr__(self):
            Representation of the Groups class.
        format(self):
            Returns a dictionary representation of the Groups object.
    """

    __tablename__ = "groups"

    title = db.Column(db.String(60), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(60), unique=True, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(60), unique=True, nullable=False, default=datetime.utcnow)

    def __init__(self, title):
        """Constructor for the Groups class."""
        self.title = title

    def __repr__(self):
        """Representation of the Groups class."""
        return "title: {}".format(self.title)

    def format(self):
        """Returns a dictionary representation of the Groups object."""
        return {"group_id": self.id,
                 "title": self.title,
                 "created_at": self.created_at,
                 "updated": self.updated_at}
