from flask import Flask


def create_app(config_file=None, test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    if config_file:
        app.config.from_pyfile(config_file)

    if test_config:
        app.config.from_object(test_config)

    from app.routes import app_bp
    from app.errors.handlers import errors

    app.register_blueprint(app_bp)
    app.register_blueprint(errors)

    return app
