from flask import Flask, Response
from controllers import primary_controller
from flask_healthz import healthz



def create_app():
    app = Flask(__name__)
    app.register_blueprint(primary_controller)
    app.register_blueprint(healthz, url_prefix="/healthz")
    app.config.update(
        HEALTHZ={
            "live": "controllers.liveness",
            "ready": "controllers.readiness",
        }
    )
    return app
