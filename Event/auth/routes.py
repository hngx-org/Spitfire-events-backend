from flask import jsonify, Blueprint
from Event.models import Users
from Event.utils import query_one_filtered


auth = Blueprint("auth", __name__, url_prefix="/auth")#url_prefix includes /auth before all endpoints in blueprint


# sample Endpoint gets user details from db
@auth.route("/@me")
def see_sess():
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
        """
        or
        return jsonify({"message:"success",
                        "user": user.format()
                        })
        """

    except Exception as e:
        return (
            jsonify(
                {
                    "error": "Internal server error",
                    "message": "It's not you it's us",
                }
            ),
            500,
        )
