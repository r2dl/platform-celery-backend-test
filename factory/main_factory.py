from flask import Flask, Response
from controllers import primary_controller
from main_service.main_service_routes import main_service


def create_app():
    app = Flask(__name__)
    app.register_blueprint(primary_controller)
    app.register_blueprint(main_service)
    return app
