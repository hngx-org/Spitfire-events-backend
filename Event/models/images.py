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
        url (str):
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
    
    def __init__(self, url):
        """_summary_

        Args:
            comment_id (str): foreign key
            url (str): source url of the saved image
        """
        self.url = url

    def __repr__(self):
        """object representation

        Returns:
            _type_: _description_
        """
        return "url: {}, created_at: {}, updated_at: {}".format(
            self.url, self.created_at, self.updated_at
        )

    def format(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "id": self.id,
            "url": self.url,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
