from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def get_active_signals():
    """_summary_
    """
    return
