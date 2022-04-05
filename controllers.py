import json
from flask import Response, Blueprint
from main_service import main_service


primary_controller = Blueprint("primary_controller", __name__)


@primary_controller.route("/health", methods=["GET"])
def health_check():
    return Response(
        response=json.dumps({"health_check": "passed"}, indent=4),
        status=200,
        mimetype="application/json",
    )


@primary_controller.route("/service", methods=["GET"])
def service():
    response = json.dumps(main_service())
    return Response(response=response, status=200, mimetype="application/json")
