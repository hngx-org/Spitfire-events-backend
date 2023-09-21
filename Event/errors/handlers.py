# pylint: disable=cyclic-import
"""_summary_

    Returns:
        _type_: _description_
    """
from flask import Blueprint, jsonify
from Event import db

# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
error = Blueprint("error", __name__)


class CustomError(Exception):
    """Exception class for custom errors"""

    def __init__(self, error, code, message):
        """constructor for custom error class

        Args:
            error (_type_): Error Name
            code (_type_): HTTP error code
            message (_type_): error message
        """
        self.error = error
        self.code = code
        self.message = message


# pylint: disable=broad-exception-caught
@error.teardown_app_request
def clean_up(exc):
    """_summary_

    Args:
        exc (_type_): _description_
    """
    try:
        db.session.remove()
    except Exception:
        pass


@error.app_errorhandler(CustomError)
def custom_error(error):
    """app error handler for custom errors"""
    return (
        jsonify({"error": error.error, "message": error.message}),
        error.code,
    )


@error.app_errorhandler(400)
def bad_request(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify({"error": error.name, "message": error.description}), 400


@error.app_errorhandler(404)
def resource_not_found(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify({"error": error.name, "message": error.description}), 404


@error.app_errorhandler(405)
def method_not_allowed(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (
        jsonify({"error": error.name, "message": error.description}),
        405,
    )


@error.app_errorhandler(422)
def cant_process(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify({"error": error.name, "message": error.description}), 422


# pylint: disable=function-redefined
@error.app_errorhandler(429)
def cant_process(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify({"error": error.name, "message": error.description}), 429


@error.app_errorhandler(500)
def server_error(error):
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify({"error": error.name, "message": "Its not you its us"}), 500
