#!/usr/bin/env python3
"""Template for the Images Class"""

from Event import db
from Event.models.base_model import BaseModel


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
        image = Images(comment_id=1, image_url="https://example.com/image.jpg")
    """

    __tablename__ = "images"

    comment_id = db.Column(
        db.String(120), db.ForeignKey("comments.id"), nullable=False
    )
    image_url = db.Column(db.String(255), nullable=False)

    def __init__(self, comment_id, image_url):
        """_summary_

        Args:
            comment_id (_type_): _description_
            image_url (_type_): _description_
        """
        self.comment_id = comment_id
        self.image_url = image_url

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "comment_id: {}, image_url: {}".format(
            self.comment_id, self.image_url
        )

    def format(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "image_id": self.id,
            "comment_id": self.comment_id,
            "image_url": self.image_url,
        }
