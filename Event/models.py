from flask_sqlalchemy import SQLAlchemy
from Event import db
from uuid import uuid4


def get_uuid():
    # generates unique id
    return uuid4().hex


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    avatar = db.Column(db.String(200), nullable=False)

    def __init__(self, display_name, email, avatar):
        self.display_name = display_name

        self.email = email
        self.avatar = avatar

    def __repr__(self):
        return f'Display Name: {self.display_name}, Email: {self.email}'

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
            "user_id": self.user_id,
            "display_name": self.display_name,
            "email": self.email,
            "avatar": self.avatar
        }


class Event(db.Model):
    __tablename__ = "event"

    event_id = db.Column(db.Integer, primary_key=True, default=get_uuid)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    start_at = db.Column(db.DateTime(), nullable=False)
    end_at = db.Column(db.DateTime(), nullable=False)
    thumbnail = db.Column(db.String(200), nullable=False)

    def __init__(self, title, description, creator, location, start_at, end_at, thumbnail):
        self.title = title
        self.description = description
        self.creator = creator
        self.location = location
        self.start_at = start_at
        self.end_at = end_at
        self.thumbnail = thumbnail

    def __repr__(self):
        return f'Title: {self.title}, Description: {self.description}, Creator: {self.creator}, Location: {self.location}, Starts: {self.start_at}, Ends: {self.end_at}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
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


class Comments(db.Model):
    """Model schema for the comments in the events section

        Attributes:
            id (str):
                Primary key for the table
            event_id (int):
                Foreign key for the event table
            user_id (int):
                Foreign key for the user table
            body (str):
                The comment body
            image (str):
                The image associated with the comment
            event (Event):
                The relationship to the event table
            user (User):
                The relationship to the user table


        Methods:
            __init__(self,event_id,user_id, body, image ):
              Constructor for the EventComment class.
            __repr__(self):
              Representation of the EventComment class.
            insert(self): Inserts a new EventComment object into the database.
            update(self): Updates an existing EventComment object in the database.
            delete(self): Deletes an existing EventComment object from the database.
            format(self): Returns a dictionary representation of the EventComment object.


        Examples:
            comment = Comment(event_id=1, user_id=1, body="This is a comment", image="https://www.google.com")

    """
    __tablename__ = "comments"

    id = db.Column(db.String, primary_key = True, default=get_uuid) # Primary Table Key
    event_id = db.Column(db.String, db.ForeignKey('event.id'),default=get_uuid, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'),default=get_uuid, nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    # Add relationships to Event and User models
    event = db.relationship('Event', backref=db.backref('comments', lazy = True))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    images = db.relationship('Image', backref='comment', lazy='dynamic')

    def __init__(self, event_id, user_id, body):
        self.body = body
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        return f'event_id: {self.event_id}, user_id: {self.user_id},' \
                'body: {self.body}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "comment_id": self.id,
            "event_id": self.event_id,
            "user_id": self.user_id,
            "body": self.body,
            "images": [image.format() for image in self.images]
        }


class Images(db.Model):
    """
    Model Schema for images.

    Attributes:
        image_id (str):
            Primary key for the table.
        comment_id (int):
            Foreign key for the comment table.
        image_url (str):
            The URL or path to the image.
        comment (EventComment):
            The relationship to the EventComment table.

    Methods:
        __init__(self, comment_id, image_url):
            Constructor for the Image class.
        __repr__(self):
            Representation of the Image class.
        insert(self):
            Inserts a new Image object into the database.
        update(self):
            Updates an existing Image object in the database.
        delete(self):
            Deletes an existing Image object from the database.
        format(self):
            Returns a dictionary representation of the Image object.

    Examples:
        image = Image(comment_id=1, image_url="https://example.com/image.jpg")
    """
    __tablename__ = "images"

    id = db.Column(db.String, primary_key=True, default=get_uuid) # Primary key
    comment_id = db.Column(db.String, db.ForeignKey('comments.id'),default=get_uuid, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    # Relationship
    comment = db.relationship('Comment', back_populates='images')


    def __init__(self, comment_id, image_url):
        self.comment_id = comment_id
        self.image_url = image_url

    def __repr__(self):
        return f'comment_id: {self.comment_id}, image_url: {self.image_url}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "image_id": self.id,
            "comment_id": self.comment_id,
            "image_url": self.image_url
        }
