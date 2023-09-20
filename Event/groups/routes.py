from Event.models import Groups
from flask import jsonify, Blueprint

from Event.utils import query_paginate_filtered, query_one_filtered


groups = Blueprint("groups", __name__, url_prefix="/api/groups")


@groups.route("/<id>", methods=["GET"])
def get_group(id):
    try: 
        get_group= query_one_filtered(table=Groups, id=id)
        
        if not get_group:
            return jsonify({"message" : "Group not found"}), 404
        return jsonify(get_group), 200
    except Exception as e:
        #Handle other errors
        jsonify({"error" : e}), 400