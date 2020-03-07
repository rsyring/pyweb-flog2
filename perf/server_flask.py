import flask

flask_app = flask.Flask(__name__)


@flask_app.route('/')
def home():
    return 'benchmark flask'


if __name__ == '__main__':
    flask_app.run(debug=None)

# hide notes
if False:
    pass
    # ab -t 5 -c 1 = 876 / sec
    # ab -t 5 -c 5 = 946 / sec
    # ab -t 5 -c 5 = 967 / sec

    # waitress
    # ab -t 5 -c 5 = 1965 / sec

    # gunicorn meinheld
    # ab -t 5 -c 5 = 13,066 / sec
