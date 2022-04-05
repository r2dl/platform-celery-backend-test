import json
from flask import Response, Blueprint
from flask_healthz import HealthError

primary_controller = Blueprint("primary_controller", __name__)


@primary_controller.route("/health", methods=["GET"])
def health_check():
    return Response(
        response=json.dumps({"health_check": "passed"}, indent=4),
        status=200,
        mimetype="application/json",
    )


def liveness():
    try:
        # check connection to db if db exists
        print("container is healthy")
        pass
    except Exception:
        raise HealthError("Can't connect to microserver")


def readiness():
    try:
        print("ready to run")
        pass
    except Exception:
        raise HealthError("Can't start microserver")