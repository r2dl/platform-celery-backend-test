from flask_healthz import HealthError


def liveness():
    try:
        pass
    except Exception:
        raise HealthError("Cannot connect to microservice")


def readiness():
    try:
        pass
    except Exception:
        raise HealthError("Cannot start microservice")
