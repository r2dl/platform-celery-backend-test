import json
from flask import Response, Blueprint, request, jsonify
from tasks import create_task, celery
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


@primary_controller.route("/celery", methods=["POST"])
def celery_create_task():
    # content = request.json
    # task_type = content["type"]
    # task_name = content["name"]
    task = create_task.delay(request.json)
    return jsonify({"result_id": task.id}), 202


@primary_controller.route("/get_status", methods=["GET"])
def celery_status():
    id = request.args.get("id")
    task_result = AsyncResult(id)
    result = {"task_id": id, "status": task_result.status, "result": task_result.result}
    return jsonify(result), 200


@primary_controller.route("/get_tasks", methods=["GET"])
def get_celery_tasks():
    keys = r.keys()
    out = []
    for key in keys:
        this_key = key.decode("utf-8")
        if this_key.startswith("celery"):
            out.append(this_key)
    return jsonify({"tasks": out}), 200
