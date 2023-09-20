from flask import Blueprint


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/")
def get_active_signals():
    return
