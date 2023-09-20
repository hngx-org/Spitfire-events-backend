from Event.models.users import Users
from Event.models.base_model import get_uuid
from flask import jsonify, Blueprint, request


from Event.utils import query_paginate_filtered, query_one_filtered
from Event import db
import os


users = Blueprint("users", __name__)


@users.route("/users")
def get_active_signals():
    return jsonify({"message": "User table sucessfully tested"})


@users.route("/users", methods=["POST"], strict_slashes=False)
def add_user():
    if not request.json:
        return jsonify({"message": "Invalid request"}), 400

    data = request.get_json()
    print((dir(data)))
    name = data.get("name")
    email = data.get("email")
    avatar = data.get("avatar")
    print("Hello")
    user = Users(name, email, avatar)
    print("Im here")
    print(user)
    return jsonify("HI")

    # if not name or not email or not avatar:
    #     return jsonify({"message": "Invalid request"}), 400

    # db.session.add(user)
    # db.session.commit()

    # return jsonify({"message": "User created successfully"}), 200
