#!/usr/bin/env python3
"""Template for the Images Class"""

from Event import db
from Event.models.base_model import BaseModel
from datetime import datetime


class Images(BaseModel):
    """
    Model Schema for images.

    Attributes:
        id (str):
            Primary key for the table.
        comment_id (str):
            Foreign key for the comment table.
        image_url (str):
            The URL or path to the image.

    Methods:
        __init__(self, comment_id, image_url):
            Constructor for the Image class.
        __repr__(self):
            Representation of the Image class.
        format(self):
            Returns a dictionary representation of the Image object.
    Examples:
        image = Images(comment_id=1, url="https://example.com/image.jpg")
    """

    __tablename__ = "images"

    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Datetime(), nullable=False, default=datetime.utcnow)

    def __init__(self, comment_id, url):
        """_summary_

        Args:
            comment_id (str): foreign key
            url (str): source url of the saved image
        """
        self.comment_id = comment_id
        self.url = url

    def __repr__(self):
        """object representation

        Returns:
            _type_: _description_
        """
        return "comment_id: {}, url: {}".format(
            self.comment_id, self.url
        )

    def format(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "image_id": self.id,
            "comment_id": self.comment_id,
            "url": self.url,
        }
