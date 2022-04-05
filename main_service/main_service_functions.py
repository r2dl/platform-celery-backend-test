from main_service.models import example_model


def get_results():
    return {"results": example_model()}


def delete_results():
    return {"results": "deleted"}

