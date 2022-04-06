import json
from flask import Response, Blueprint, request
from main_service.main_service_functions import get_results, delete_results, post_results

main_service = Blueprint("main_service", __name__)


@main_service.route("/", methods=["GET", "POST", "DELETE"])
def main_services():
    if request.method == "GET":
        return Response(response=json.dumps(get_results(), indent=4), status=200, mimetype="application/json")
    if request.method == "POST":
        return Response(response=json.dumps(post_results(), indent=4), status=201, mimetype="application/json")
    if request.method == "DELETE":
        return Response(response=json.dumps(delete_results(), indent=4), status=202, mimetype="application/json")
