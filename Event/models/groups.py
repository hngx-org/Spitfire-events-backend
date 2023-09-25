#!/usr/bin/env python3
"""Template for the Groups Class"""

from Event import db
from Event.models.base_model import BaseModel

# Association table between groups and events
group_events = db.Table('group_events',
    db.Column('group_id', db.String(60), db.ForeignKey("groups.id"), primary_key=True, nullable=False),
    db.Column('event_id', db.String(60), db.ForeignKey("events.id"), primary_key=True, nullable=False)
)
# Association table between groups and images
group_image = db.Table('group_image',
    db.Column('group_id', db.String(60), db.ForeignKey("groups.id"), primary_key=True, nullable=False),
    db.Column('image_id', db.String(60), db.ForeignKey("images.id"), primary_key=True, nullable=False)
)


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
    # creator_id = db.column(db.Strings(60), db.ForeignKey("users.id") nullable=False)

    # many to many relationships with groups
    events = db.relationship("Events", secondary=group_events, backref=db.backref("involved_groups", lazy=True), lazy="subquery")

    thumbnails = db.relationship("Images", secondary=group_image, backref=db.backref("group", lazy=True), lazy="subquery")

    def __init__(self, title):
        """Constructor for the Groups class."""
        self.title = title

    def __repr__(self):
        """Representation of the Groups class."""
        return "title: {}".format(self.title)

    def format(self):
        """Returns a dictionary representation of the Groups object."""
        return {"id": self.id,
                 "title": self.title,
                 "created_at": format(self.created_at),
                 "updated": format(self.updated_at)}
