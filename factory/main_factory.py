from flask import Flask
from controllers.controllers import primary_controller
from flask_healthz import healthz


def create_app():
    app = Flask(__name__)
    app.register_blueprint(primary_controller)
    app.register_blueprint(healthz, url_prefix="/healthz")
    app.config.update(
        HEALTHZ={
            "live": "controllers.healthz.liveness",
            "ready": "controllers.healthz.readiness",
        }
    )
    return app
