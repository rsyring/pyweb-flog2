from flask import Blueprint

public = Blueprint('public', __name__)


@public.route('/hello')
def hello():
    return 'Hello DerbyPy!'
