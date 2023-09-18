from flask import Blueprint, jsonify
from Event import db

error = Blueprint("error", __name__)


@error.teardown_app_request
def clean_up(exc):
    try:
        db.session.remove()
    except:
        pass


@error.app_errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.name, "message": error.description}), 400


@error.app_errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": error.name, "message": error.description}), 404


@error.app_errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify({"error": error.name, "message": error.description}),
        405,
    )


@error.app_errorhandler(422)
def cant_process(error):
    return jsonify({"error": error.name, "message": error.description}), 422


@error.app_errorhandler(429)
def cant_process(error):
    return jsonify({"error": error.name, "message": error.description}), 429


@error.app_errorhandler(500)
def server_error(error):
    return jsonify({"error": error.name, "message": "Its not you its us"}), 500
