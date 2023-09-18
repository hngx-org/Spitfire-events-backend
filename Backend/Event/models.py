from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from Event import db


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    avatar = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Display Name: {self.display_name}, Email: {self.email}'

    def user_insert(self):
        db.session.add(self)
        db.session.commit()

    def user_update(self):
        self.verified = True
        db.session.commit()

    def user_delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "user_id": self.user_id,
            "display_name": self.display_name,
            "email": self.email,
            "avatar": self.avatar
        }


class Event(db.Model):
    __tablename__ = "event"

    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey(
        User.user_id))
    location = db.Column(db.String(), nullable=False)
    start_at = db.Column(db.DateTime(), nullable=False)
    end_at = db.Column(db.DateTime(), nullable=False)
    thumbnail = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Title: {self.title}, Description: {self.description}, Creator: {self.creator}, Location: {self.location}, Starts: {self.start_at}, Ends: {self.end_at}'

    def events_to_dict(self):
        # Dictionary Comprehension to loop through the table
        return {column.name: getattr(self, column.event_id, column.title, column.description, column.creator, column.location, column.start_at, column.end_at, column.thumbnail) for column in self.__table__.columns}

    def event_insert(self):
        self.creator.verified = True
        db.session.add(self)
        db.session.commit()

    def event_update(self):
        self.creator.verified = True
        db.session.commit()

    def event_delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "location": self.location,
            "start_at": self.start_at,
            "end_at": self.end_at,
            "thumbnail": self.thumbnail
        }
