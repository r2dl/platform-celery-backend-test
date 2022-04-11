import json
from flask import Response, Blueprint, request
from main_service.main_service_functions import (
    get_results,
    delete_results,
    post_results,
)
from tasks import create_task, celery
from celery.result import AsyncResult
import redis


main_service_queue = Blueprint("main_service_queue", __name__)

@main_service_queue.route("/queue_task", methods=["POST"])
def queue_task():
    task = create_task.delay(request.json)
    return Response(
        response=json.dumps({"result_id": task.id}, indent=4),
        status=202,
        mimetype="application/json",
    )

@main_service_queue.route("/status", methods=["GET"])
def status():
    id = request.args.get("id")
    task_result = AsyncResult(id)
    return Response(
        response=json.dumps({"task_id": id, "status": task_result.status, "result": task_result.result}, indent=4),
        status=202,
        mimetype="application/json",
    )

@main_service_queue.route("/all_tasks", methods=["GET"])
def all_tasks():
    keys = r.keys()
    out = []
    for key in keys:
        this_key = key.decode("utf-8")
        if this_key.startswith("celery"):
            out.append(this_key)
    return Response(
        response=json.dumps({"task_list": out}, indent=4),
        status=202,
        mimetype="application/json",
    )
