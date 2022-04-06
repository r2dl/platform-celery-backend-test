from flask import Flask, Response
from main_service.main_service_routes import main_service
from controllers.controllers import primary_controller
from flask_healthz import healthz


def create_app():
    app = Flask(__name__)
    app.register_blueprint(primary_controller)
    app.register_blueprint(main_service)
    app.register_blueprint(healthz, url_prefix="/healthz")
    app.config.update(
        HEALTHZ={
            "live": "controllers.healthz.liveness",
            "ready": "controllers.healthz.readiness",
        }
    )
    return app
