from datetime import datetime
from Event import db
from uuid import uuid4

# generates unique id (optional)
def get_uuid():
    return uuid4().hex


# sample Table class to follow
class User(db.Model):
    __tablename__ = "users" #explicitly name tables
    id = db.Column(
        db.String(34), primary_key=True, unique=True, nullable=False, default=get_uuid
    )
    user_name = db.Column(db.String(345), unique=True, nullable=False)
    email = db.Column(db.String(345), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # class constructor/initializer for ide class properties suggestion
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
            "email": self.email,
            "user_name": self.user_name,
            "date_created": self.date_created,
        }


class UserGroup(db.Model):
    '''class that models the UserGroup table'''
    __table__name = 'UserGroup'
    UserID = db.Column(db.Integer, db.models.ForeignKey("User.UserID"), primary_key=True)
    GroupID = db.Column(db.Integer, db.models.ForeignKey("Group.GroupID"), primary_key=True)

    def save(self):
        '''add a new user'''
        db.session.add(self)
        db.session.commit()

    def delete(self):
        '''remove a user'''
        db.session.delete(self)
        db.session.commit()
