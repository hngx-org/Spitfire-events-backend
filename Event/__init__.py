from Event.config import App_Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
import os


db = SQLAlchemy()


def create_app(config_class=App_Config):
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-
    app = Flask(__name__)
    app.config["SESSION_SQLALCHEMY"] = db
    app.config.from_object(App_Config)
    # Initialize CORS
    CORS(app, supports_credentials=True)
    # Initialize SQLAlchemy
    db.init_app(app)

    # register endpoint(blueprints)
    from Event.api import apis

    app.register_blueprint(apis)

    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app
