from flask_sqlalchemy import SQLAlchemy
from Event import db
from uuid import uuid4


def get_uuid():
    # generates unique id
    return uuid4().hex


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(60), primary_key=True, unique=True,
                   default=get_uuid, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access_token = db.Column(db.String(120), nullable=False),
    refresh_token = db.Column(db.String(120), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, avatar):
        self.name = name
        self.email = email
        self.avatar = avatar

    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}'

    # safely add record/object to db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # safely update record/object in db
    def update(self):
        db.session.commit()

    # safely delete record/object from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # output object properties in clean dict format
    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "avatar": self.avatar
        }


class Events(db.Model):
    __tablename__ = "events"

    id = db.Column(db.String(60), primary_key=True, default=get_uuid)
    title = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(225), nullable=False)
    creator = db.Column(db.String(60), db.ForeignKey(
        "users.id"), nullable=False)
    location = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    start_time = db.Column(db.Time(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    end_time = db.Column(db.Time(), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, creator, location, start_date, start_time, end_date, end_time, thumbnail):
        self.title = title
        self.description = description
        self.creator = creator
        self.location = location
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.thumbnail = thumbnail

    def __repr__(self):
        return f'Title: {self.title}, Description: {self.description}, Creator: {self.creator}, Location: {self.location}, Start Date: {self.start_date}, Start Time: {self.start_time}, End Date: {self.end_date},  End Time: {self.end_time}'

    # safely add record/object to db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # safely update record/object to db
    def update(self):
        db.session.commit()

    # safely delete record/object to db
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # output object properties in clean dict format
    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "location": self.location,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "thumbnail": self.thumbnail
        }
