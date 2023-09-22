# #!/usr/bin/env python3
# """
# This the base template for all IntresedeEvents object instances.
# """
# from Event import db
# from Event.models.base_model import BaseModel


# class InterestedEvents(BaseModel):
#     """
#     Model Schema for InterestedEvents.

#     Attributes:
#         user_id (str):
#             Foreign key for the user table.
#         event_id (str):
#             Foreign key for the event table.
#     """

<<<<<<< HEAD
    __tablename__ = "interested_events"
    user_id = db.Column(db.String(120), db.ForeignKey("users.id"), nullable=False)
    event_id = db.Column(db.String(120), db.ForeignKey("events.id"), nullable=False)
=======
#     __tablename__ = "interested_events"
#     user_id = db.Column(
#         db.String(120), db.ForeignKey("users.id"), nullable=False
#     )
#     event_id = db.Column(
#         db.String(120), db.ForeignKey("events.id"), nullable=False
#     )
>>>>>>> 57eac9d02887492d8a99bcc3ee6c9792a534c016

#     def __init__(self, user_id, event_id):
#         """Initialize the InterestedEvents object"""
#         self.user_id = user_id
#         self.event_id = event_id

#     def format(self):
#         """Return a dictionary representation of the InterestedEvents object"""
#         return {"user_id": self.user_id, "event_id": self.event_id}
