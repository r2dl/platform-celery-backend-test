import json
from flask import Response, Blueprint, request, jsonify
from celery.tasks import create_task, celery
from celery.result import AsyncResult
import redis

primary_controller = Blueprint("primary_controller", __name__)

r = redis.StrictRedis(host="redis", port="6379", db=0)


@primary_controller.route("/health", methods=["GET"])
def health_check():
    return Response(
        response=json.dumps({"health_check": "passed"}, indent=4),
        status=200,
        mimetype="application/json",
    )

