# pylint: disable=cyclic-import
"""_summary_

    Returns:
        _type_: _description_
    """
# pylint: disable=unused-import
from flask import jsonify, Blueprint
# from Event.models import Users
from Event.utils import query_one_filtered


# url_prefix includes /auth before all endpoints in blueprint
auth = Blueprint("auth", __name__, url_prefix="/api/auth")


# sample Endpoint gets user details from db
# pylint: disable=broad-exception-caught
@auth.route("/@me")
def see_sess():
    """_summary_
    """
    try:
        user = query_one_filtered(Users, id=1)
        return jsonify(
            {
                "message": "Success",
                "email": user.email,
                "user_name": user.user_name,
                "created_on": user.date_created
            }
        )
        # pylint: disable=unreachable
        # pylint: disable=pointless-string-statement
        """
        or
        return jsonify({"message:"success",
                        "user": user.format()
                        })
        """

    except Exception:
        return (
            jsonify(
                {
                    "error": "Internal server error",
                    "message": "It's not you it's us",
                }
            ),
            500,
        )
