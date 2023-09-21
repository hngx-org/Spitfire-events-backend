#!/usr/bin/env python3
"""Template for the EventThumbnail Class"""

from Event import db
from Event.models.base_model import BaseModel


class EventThumbnail(BaseModel):
    """
        Model Schema for EventThumbnail.

    """
    __tablename__ = "event_thumbnails"

    image_id = db.Column(db.String(128), db.ForeignKey("images.id"), nullable=False)
    event_id = db.Column(db.String(128), db.ForeignKey("events.id"), nullable=False)

    def __init__(self, image_id, event_id):
        """_summary_

        Args:
            comment_id (_type_): _description_
            event_id (_type_): _description_
        """
        self.image_id = image_id
        self.event_id = event_id

    def __repr__(self):
        """
        Return a string representation of the EventThumbnail object.
        This method is automatically called when the object is printed or
        when the `repr()` function is used. It returns a formatted string
        containing the EventThumbnail object's identifier.
        """
        return "id: {}, image_id: {}, event_id: {}".format(self.id, self.image_id, self.event_id)