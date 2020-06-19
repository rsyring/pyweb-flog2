from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_ext(app):
    db.init_app(app)
