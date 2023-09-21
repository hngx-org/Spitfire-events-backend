# pylint: disable=cyclic-import
"""_summary_

    Returns:
        _type_: _description_
    """
# pylint: disable=unused-import
import os
import requests
from google.oauth2 import id_token
from google.auth.transport import requests
from google.auth.exceptions import GoogleAuthError
from flask import jsonify, Blueprint, request, session
from Event.models.users import Users
from Event.errors.handlers import CustomError
from Event.utils import query_one_filtered, is_logged_in

auth = Blueprint(
    "auth", __name__, url_prefix="/api/auth"
)  # url_prefix includes /auth before all endpoints in blueprint

ANDROID_CLIENT_ID = os.environ.get("ANDROID_CLIENT_ID")
IOS_CLIENT_ID = os.environ.get("IOS_CLIENT_ID")


@auth.route("/", methods=["POST"])
def register_or_login():
    """Register and Login route for google authentication"""
    data = request.get_json()

    # lets collect the credential token from request body
    credential_token = data.get("token")
    if not credential_token:
        raise CustomError("Bad Request", 400, "invalid token")

    try:
        # we'll ask google to verify they issued this token,  give us user data
        id_info = id_token.verify_oauth2_token(
            id_token=credential_token, request=requests.Request()
        )
    except GoogleAuthError as error:
        print(error)  # remove before production after testing auth on mobile
        raise CustomError("Bad Request", 400, "invalid token")
    except ValueError:
        raise CustomError("Bad Request", 400, "invalid token")

    # lets check if the token was issued for us
    if id_info["aud"] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID]:
        raise CustomError("Forbidden", 403, "Token is of unknown origin")

    user = query_one_filtered(Users, id=id_info["sub"])
    if not user:
        user = Users(
            id=id_info["sub"],
            name=id_info["name"],
            email=id_info["email"],
            avatar=id_info["picture"],
        )
        user.insert()

    # # we have a valid user,lets create a login session
    session["user"] = {"id": user.id}

    return (
        jsonify(
            {
                "message": "success",
                "email": user.email,
                "name": user.name,
                "avatar": user.avatar,
            }
        ),
        200,
    )


# pylint: disable=broad-exception-caught
@auth.route("/@me")
def see_sess():
    """
    get the details of current logged in user
    """
    user_id = is_logged_in(session)
    try:
        user = query_one_filtered(Users, id=user_id)
        return (
            jsonify(
                {
                    "message": "Success",
                    "email": user.email,
                    "name": user.name,
                    "avatar": user.avatar,
                }
            ),
            200,
        )
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


@auth.route("/logout", methods=["GET", "POST"])
def logout_user():
    """Logout user by removing login session"""
    session.pop("user", None)
    return jsonify({"message": "success"}), 204
