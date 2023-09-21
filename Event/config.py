"""
summary
"""
import os
import datetime
from dotenv import load_dotenv


load_dotenv(".env")


# pylint: disable=invalid-name
class App_Config:
    """_summary_"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "test")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SESSION_TYPE = "sqlalchemy"
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_HTTPONLY = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)

    def nothing(self):
        """_summary_"""

    def another(self):
        """_summary_"""
