#!/usr/bin/env python3
"""Template for the GroupImage Class"""

from Event import db
from Event.models.base_model import BaseModel

class GroupImage(BaseModel):
    """Group Image Class"""

    __tablename__ = "group_images"

    group_id = db.Column(db.String(128), db.ForeignKey("groups.id"), nullable=False)
    image_id = db.Column(db.String(128), db.ForeignKey("images.id"), nullable=False)

    def __init__(self, group_id, image_id):
        self.group_id = group_id
        self.image_id = image_id

    def __repr__(self):
        """
        Return a string representation of the GroupImage object.
        This method is automatically called when the object is printed or
        when the `repr()` function is used. It returns a formatted string
        containing the GroupImage object's identifier.

        Returns:
            str: A string representation of the GroupImage object.
        """
        return "id: {}, group_id: {}, image_id: {}".format(self.id, self.group_id, self.image_id)

    def format(self):
        """
        Return a dictionary representation of the GroupImage object.
        This method is automatically called when the object is printed or
        when the `format()` function is used. It returns a dictionary
        containing the GroupImage object's attributes.
        """
        return {
            "id":self.id if self.id else "",
            "group_id": self.group_id,
            "image_id": self.image_id
        }

