from flask import Blueprint, render_template
from flask_wtf.csrf import CSRFError

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('error.html', title='CSRF Error'), 400


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('error.html', title='Not Found'), 404


@errors.app_errorhandler(405)
def error_405(error):
    return render_template('error.html', title='Not Allowed'), 405


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('error.html', title='Unauthorized Access'), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('error.html', title='Server Error'), 500
