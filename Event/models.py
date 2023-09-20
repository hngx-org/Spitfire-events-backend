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
    access_token = db.Column(db.String(120), nullable=True),
    refresh_token = db.Column(db.String(120), nullable=True)
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


class Groups(db.Model):
    __tablename__ = "groups"
    

    group_id = db.Column(db.String(36), primary_key=True, default=get_uuid, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'Group ID: {self.group_id}, Title: {self.title}'
    
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
            "id": self.group_id,
            "title": self.title
        }
        



class Comments(db.Model):
    """Model schema for the comments in the events section

        Attributes:
            id (str):
                Primary key for the table
            event_id (str):
                Foreign key for the event table
            user_id (str):
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
            comment = Comments(event_id=1, user_id=1, body="This is a comment", image="https://www.google.com")

    """
    __tablename__ = "comments"

    id = db.Column(db.String, primary_key = True, default=get_uuid) # Primary Table Key
    event_id = db.Column(db.String(36), db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'),  nullable=False)
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
        id (str):
            Primary key for the table.
        comment_id (str):
            Foreign key for the comment table.
        image_url (str):
            The URL or path to the image.
        comment (Comment):
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
        image = Images(comment_id=1, image_url="https://example.com/image.jpg")
    """
    __tablename__ = "images"

    id = db.Column(db.String, primary_key=True, default=get_uuid) # Primary key
    comment_id = db.Column(db.String(36), db.ForeignKey('comments.id'), nullable=False)
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


class UserGroups(db.Model):
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
    __tablename__ = "usergroups"

    user_id = db.Column(db.String(36), db.ForeignKey('users.id'),  nullable=False)
    group_id = db.Column(db.String(36), db.ForeignKey('groups.id'),  nullable=False)

    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

    def __repr__(self):
        return f'user_id: {self.user_id}, group_id: {self.group_id}'

    
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
            "group_id": self.group_id,
            "title": self.title
        }
        
        
        


    def format(self):
        return {
            "user_id": self.user_id,
            "group_id": self.group_id
        }

