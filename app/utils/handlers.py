from flask import Blueprint

from .errors import error_response

handlers = Blueprint('handlers', __name__)


@handlers.app_errorhandler(404)
def error_404(error):
    return error_response(404, error.description)


@handlers.app_errorhandler(405)
def error_405(error):
    return error_response(405, error.description)


@handlers.app_errorhandler(500)
def error_500(error):
    return error_response(500, error.description)


@handlers.app_errorhandler(503)
def error_503(error):
    return error_response(503, error.description)
