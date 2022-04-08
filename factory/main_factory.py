from flask import Flask, Response
from flask_cors import CORS
from main_service.main_queue_routes import main_service_queue
from main_service.main_service_routes import main_service
from controllers.controllers import primary_controller
from flask_healthz import healthz


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_service_queue)
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
