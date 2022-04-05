import json
from flask import Response, Blueprint

primary_controller = Blueprint("primary_controller", __name__)


@primary_controller.route("/health", methods=["GET"])
def health_check():
    return Response(
        response=json.dumps({"health_check": "passed"}, indent=4),
        status=200,
        mimetype="application/json",
    )

