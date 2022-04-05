from flask_healthz import HealthError


def liveness():
    try:
        pass
    except Exception:
        raise HealthError("Can't connect to microservice")


def readiness():
    try:
        pass
    except Exception:
        raise HealthError("Can't start microservice")
