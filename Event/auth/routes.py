from flask import jsonify, Blueprint
from Event.models import User
from Event.utils import query_one_filtered



auth = Blueprint("auth", __name__, url_prefix="/auth")


# sample Endpoint gets user details from db
@auth.route("/@me")

def see_sess():
    try:
        user = query_one_filtered(User, id=1 )
        return jsonify(
            {
                "message": "Success",
                "email": user.email,
                "user_name": user.user_name,
                "is_active": user.is_active,
                "roles": user.roles.value,
                "created_on": user.date_created,
            }
        )
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

