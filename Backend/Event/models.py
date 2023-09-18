from datetime import datetime
from Event import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        db.String(34), primary_key=True, unique=True, nullable=False, default=get_uuid
    )
    user_name = db.Column(db.String(345), unique=True, nullable=False)
    email = db.Column(db.String(345), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(
        self,
        user_name,
        email,
        password,
    ):
        self.user_name = user_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"user_name({self.user_name}), email({self.email}), date_created({self.date_created}))"

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
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "date_created": self.date_created,
        }
    
class EventComment(db.Model):
    event_id = db.Column(db.String(34), db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.String(34), db.ForeignKey('users.id'), primary_key=True)
    body = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    # Define relationships
    event = db.relationship('Event', backref='comments')
    user = db.relationship('User', backref='comments')
