# pylint: disable=cyclic-import
"""_summary_

    Returns:
        _type_: _description_
    """
from flask import Blueprint


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/")
def get_active_signals():
    """_summary_
        """
    return
