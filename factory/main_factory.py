from flask import Flask, Response
from controllers import primary_controller


def create_app():
    app = Flask(__name__)
    app.register_blueprint(primary_controller)
    return app
