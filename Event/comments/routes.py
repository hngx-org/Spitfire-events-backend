# pylint: disable=cyclic-import
"""_summary_

    Returns:
        _type_: _description_
    """
from flask import Blueprint


comments = Blueprint("comments", __name__, url_prefix="/api/comments")


@comments.route("/")
def get_active_signals():
    """_summary_
        """
    return
