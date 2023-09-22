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
    Methods:
        __init__(self, user_id, group_id):
            Constructor for the UserGroups class.
        __repr__(self):
            Representation of the UserGroups class.
        insert(self):
            Inserts a new UserGroups object into the database.
        update(self):
            Updates an existing UserGroups object in the database.
        delete(self):
            Deletes an existing UserGroups object from the database.
        format(self):
            Returns a dictionary representation of the UserGroups object.

    Examples:
        usergroup = UserGroups(user_id=1, group_id=1f)
    """

    __tablename__ = "user_groups"
    user_id = db.Column(db.String(120), db.ForeignKey("users.id"), nullable=False)
    group_id = db.Column(db.String(120), db.ForeignKey("groups.id"), nullable=False)

    def __init__(self, user_id, group_id):
        """_summary_

        Args:
            user_id (_type_): _description_
            group_id (_type_): _description_
        """
        self.user_id = user_id
        self.group_id = group_id

    def format(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "id: {}, user_id: {}, group_id: {} ".format(
            self.id, self.user_id, self.group_id
        )
