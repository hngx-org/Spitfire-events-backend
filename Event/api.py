"""Create an api blueprint"""
from flask import Blueprint

apis = Blueprint("apis", __name__, url_prefix="/api")



# register endpoint(blueprints)
from Event.user.routes import users
from Event.auth.routes import auth
from Event.events.routes import events
from Event.errors.handlers import error

apis.register_blueprint(users)
apis.register_blueprint(auth)
apis.register_blueprint(events)
apis.register_blueprint(error)