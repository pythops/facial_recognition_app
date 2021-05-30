from flask import Flask

from app.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from app.errors.handlers import errors
    from app.routes import detection

    app.register_blueprint(detection)
    app.register_blueprint(errors)

    return app
