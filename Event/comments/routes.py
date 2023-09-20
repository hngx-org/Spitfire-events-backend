from flask import jsonify, Blueprint


comments = Blueprint("groups", __name__, url_prefix="/api/comments")


@comments.route("/")
def get_active_signals():
    return
